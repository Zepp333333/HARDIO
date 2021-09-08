#  Copyright (c) 2021. Sergei Sazonov. All Rights Reserved

import dash
from dash.dependencies import Input, Output, State
from flask_login import current_user

from hardio.dashapp.utils import ScatterDrawer
from iobrocker import IO


def register_interval_callbacks(dashapp):
    @dashapp.callback(
        Output(component_id='my-fig', component_property='figure'),
        [Input(component_id='create_interval', component_property='n_clicks'),
         Input(component_id='find_intervals', component_property='n_clicks'),
         Input(component_id='delete_intervals', component_property='n_clicks'),
         Input(component_id='interval_duration', component_property='value'),
         Input(component_id='how_many_to_find', component_property='value'),
         Input(component_id='interval_power', component_property='value'),
         Input(component_id='interval_tolerance', component_property='value'),
         Input(component_id='current_activity', component_property='data')],
        [State(component_id='my-fig', component_property='relayoutData')],
        prevent_initial_call=True
    )
    def manage_intervals(_: int,
                         __: int,
                         ___: int,
                         interval_duration: int,
                         how_many_to_find: int,
                         interval_power: int,
                         interval_tolerance: int,
                         data: int, relayout_data: dict):
        """
        Creates an interval in current activity based on relayoutData and button click"
        :param n_clicks: number of create_interval button clicks
        :param interval_duration - length of interval in seconds
        :param how_many_to_find - how many intervals to find
        :param interval_power: power to look for
        :param interval_tolerance - tolerance in % to power intervals to look for
        :param data: dcc.store containing integer id of current activity
        :param relayout_data: dict containing ends of a range slider (or user selection on a graph)
        :return: go.Figure
        """
        ctx = dash.callback_context
        if ctx.triggered[0]['prop_id'] == 'create_interval.n_clicks':
            interval_range = _relayout_data_to_range(relayout_data)
            if interval_range:
                io = IO(current_user.id)
                activity = io.get_hardio_activity_by_id(int(data))
                activity.new_interval(*interval_range)
                io.save_activity(activity)
                return _make_new_fig(activity)

        elif ctx.triggered[0]['prop_id'] == 'delete_intervals.n_clicks':
            io = IO(current_user.id)
            activity = io.get_hardio_activity_by_id(int(data))
            activity.delete_intervals()
            io.save_activity(activity)
            return _make_new_fig(activity)

        elif ctx.triggered[0]['prop_id'] == 'find_intervals.n_clicks':

            io = IO(current_user.id)
            activity = io.get_hardio_activity_by_id(int(data))
            found_intervals = activity.find_intervals(duration=interval_duration,
                                                      count=how_many_to_find,
                                                      power=interval_power,
                                                      tolerance=interval_tolerance)
            activity.add_intervals(found_intervals)
            io.save_activity(activity)

            return _make_new_fig(activity)
        return dash.no_update

    def _make_new_fig(activity):
        from .utils.scatter_drawer import ScatterDrawer
        new_fig = ScatterDrawer(
            activity=activity,
            index_col='time',
            series_to_plot=['watts', 'heartrate', 'cadence'],
        )
        return new_fig.get_fig()

    def _relayout_data_to_range(relayout_data: dict) -> tuple[int, int]:
        """Helper fuction converting relaout_daya dict to tuple"""
        try:
            if len(relayout_data) == 1:
                return int(relayout_data['xaxis.range'][0]), int(relayout_data['xaxis.range'][1])
            else:
                result = [int(v) for v in relayout_data.values()]
                return result[0], result[1]
        except KeyError:
            return tuple()