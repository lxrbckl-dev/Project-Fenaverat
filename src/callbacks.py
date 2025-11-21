from src.config import app
from src.services import Services

from dash.dependencies import (Input, Output, State, ALL)


class Callbacks:


    def __init__(self, services):
        """  """

        self.services = services
    

    def registerCallbacks(self):
        """  """

        self.nIntervalsCallback()


    def nIntervalsCallback(self):
        """  """

        @app.callback(

            inputs = Input("intervalId", "n_intervals"),
            state = State({"type": "video", "index": ALL}, "autoPlay"),
            output = Output({"type": "video", "index": ALL}, "autoPlay")

        )
        def func(*args): return self.services.nIntervalService(*args[1:])