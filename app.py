# < Project Fenaverat 4 by Alex Arbuckle > #


# import <
from src.views.layout import layout
from src.configs import (app, port, host)

# >


# initialize layout #
# register callbacks #
layout = layout()
layout.registerCallbacks()


# build application #
# expose Flask server #
app.layout = layout.property
server = app.server