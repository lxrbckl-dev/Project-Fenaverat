# < Project Fenaverat 4 by Alex Arbuckle > #


# import <
from src.configs import app
from src.views.layout import layout

# >


# initialize layout <
# register callbacks <
layout = layout()
layout.registerCallbacks()

# >


# build application <
app.layout = layout.property
app.run(debug = True)

# >