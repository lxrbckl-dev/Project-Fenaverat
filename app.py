# < Project Fenaverat 4 by Alex Arbuckle > #


# import <
from src.views.layout import layout
from src.configs import (app, port, host)

# >


# expose Flask server #
server = app.server


# initialize layout #
# register callbacks #
layout = layout()
layout.registerCallbacks()


# build application <
app.layout = layout.property
app.run(
   
   host = host,
   port = port,
   debug = False
   
)

# >