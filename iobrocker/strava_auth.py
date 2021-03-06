#  Copyright (c) 2021. Sergei Sazonov. All Rights Reserved

from datetime import datetime

import requests
from flask_login import current_user

from config import Config
from hardio import db
from hardio.models import Users


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def prep_app_auth_url():
    params = {
        "client_id": Config.STRAVA_APP_CLIENT_ID,
        "redirect_uri": Config.STRAVA_APP_REDIRECT_URI,
        "response_type": "code",
        "scope": "read_all,profile:read_all,activity:read_all,activity:write",
        "approval_prompt": "force"
    }
    base_url = Config.STRAVA_AUTH_URL
    return requests.Request('GET', base_url, params=params).prepare().url


def check_strava_auth_code(args):
    return 'code' in args and len(args['code']) == 40


def check_auth_scopes(args):
    if 'scope' not in args:
        return False
    scope = args['scope'].split(',')
    return sorted(scope) == sorted(Config.STRAVA_REQUIRED_SCOPES)


def check_strava_auth_return(args):
    result = check_strava_auth_code(args) and check_auth_scopes(args)
    return result


def store_athlete_access_token(auth_response, user: Users = None):
    if not user:
        user = current_user
    user.strava_access_token = auth_response['access_token']
    user.strava_token_expires_at = datetime.fromtimestamp(auth_response['expires_at'])
    user.strava_refresh_token = auth_response['refresh_token']
    db.session.commit()


def refresh_access_token(user_id: int) -> None:
    user = Users.query.filter_by(id=user_id).first()
    params = {
        "client_id": Config.STRAVA_APP_CLIENT_ID,
        "client_secret": Config.STRAVA_APP_CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": user.strava_refresh_token
        }
    base_url = 'https://www.strava.com/api/v3/oauth/token'
    response = requests.post(base_url, params=params).json()
    store_athlete_access_token(response, user=user)


def is_token_expired(expiration: datetime) -> bool:
    now = datetime.utcnow()
    return (expiration - now).days < 0 or (expiration - now).seconds < 3600


def retrieve_known_athlete(auth_response):
    base_url = 'https://www.strava.com/api/v3/athlete'  # todo = move to config
    response = requests.get(base_url, auth=BearerAuth(auth_response['access_token']))   # todo - add try/except
    store_athlete_access_token(auth_response)
    return response.json()


def exchange_auth_code_for_token(auth_code):
    params = {
        "client_id": Config.STRAVA_APP_CLIENT_ID,
        "client_secret": Config.STRAVA_APP_CLIENT_SECRET,
        "code": auth_code,
        "grant_type": "authorization_code"
    }
    base_url = Config.STRAVA_TOKEN_EXCHANGE_URL
    response = requests.post(base_url, params=params)
    return response.json()


def retrieve_first_time_coming_athlete(auth_code):
    auth_response = exchange_auth_code_for_token(auth_code)
    store_athlete_access_token(auth_response)
    return retrieve_known_athlete(auth_response)


def retrieve_strava_athlete(auth_code, token=None):
    if token:
        return retrieve_known_athlete(token)
    return retrieve_first_time_coming_athlete(auth_code)

#todo implement strava de-authorize
