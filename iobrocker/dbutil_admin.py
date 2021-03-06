#  Copyright (c) 2021. Sergei Sazonov. All Rights Reserved
"""
Admin module providing simple interface to querying and manipulating data in database.
Use for development and debug purpose only
"""

from hardio import db, bcrypt
from hardio.models import Users, DBActivity
from hardio import Config
import sqlalchemy
from config import ConfigTest


def add_user(username: str, email: str, password: str, image_file: str = 'default.jpg', **kwargs) -> None:
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = Users(username=username, email=email, password=password, image_file=image_file, **kwargs)
    db.session.add(user)
    db.session.commit()


def get_user_id_by_name(username: str) -> list[int]:
    users = Users.query.filter_by(username=username).all()
    return [user.id for user in users]

def delete_user(user_id: int) -> None:
    user = Users.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()


def delete_users_strava_auth_info(user_id: int) -> None:
    user = Users.query.filter_by(id=user_id).first()
    user.strava_id = None
    user.strava_scope = None
    user.strava_access_token = None
    user.strava_token_expires_at = None
    user.strava_refresh_token = None
    user.strava_athlete_info = None
    db.session.commit()


def list_users() -> str:
    users = Users.query.all()
    string = "\n".join([u.__str__() for u in users])
    return string


def drop_test_db() -> None:
    import sqlalchemy
    from sqlalchemy.orm import close_all_sessions
    with sqlalchemy.create_engine(ConfigTest.TEST_DATABASE_SERVER,
                                  isolation_level="AUTOCOMMIT").connect() as connection:
        close_all_sessions()
        connection.execute(f'drop database {ConfigTest.TEST_DB_NAME} WITH (FORCE)')


def add_activity(db_activity: DBActivity) -> None:
    db.session.add(db_activity)
    db.session.commit()

def clen_user_config() -> None:
    with sqlalchemy.create_engine(Config.SQLALCHEMY_DATABASE_URI,
                                  isolation_level="AUTOCOMMIT").connect() as connection:
        connection.execute(f'TRUNCATE TABLE user_config')


def get_all_users() -> list[Users]:
    from hardio import create_app
    app = create_app()
    with app.app_context():
        users = Users.query.all()
    return users

def get_all_activities_of_user(user_id) -> list[DBActivity]:
    from hardio import create_app
    app = create_app()
    with app.app_context():
        activities = DBActivity.query.filter_by(user_id=user_id).all()
    return activities

def clean_db_activity() -> None:
    raise NotImplemented
    db.create_engine().execute("TRUNCATE TABLE DB_ACTIVITY")
