from src.config import app
from dash.dependencies import (Input, Output, State, ALL)


class Callbacks:


    def __init__(self, services):
        """  """

        self._services = services
    

    def registerCallbacks(self):
        """  """

        self._nIntervalsCallback()


    def _nIntervalsCallback(self):
        """  """

        @app.callback(

            inputs = Input("intervalId", "n_intervals"),
            state = State({"type": "video", "index": ALL}, "autoPlay"),
            output = Output({"type": "video", "index": ALL}, "autoPlay")

        )
        def func(*args): return self._services.nIntervalService(*args[1:])