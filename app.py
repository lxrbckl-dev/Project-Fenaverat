from json import loads

from src.view import View
from src.services import Services
from src.callbacks import Callbacks
from src.config import (app, fileLayout)


items = loads(fileLayout.read_text()).values()
app.layout = View(items = items).build
server = app.server

Callbacks(Services()).registerCallbacks()


if (__name__ == "__main__"): app.run(debug = True)