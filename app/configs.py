# import <
from dash import Dash
from dash_bootstrap_components import themes

# >


app = Dash(
   
   name = 'lxRbckl',
   title = 'lxRbckl',
   assets_folder = './assets',
   suppress_callback_exceptions = True,
   external_stylesheets = [
      
      themes.GRID,
      themes.BOOTSTRAP
      
   ]
   
)

server = app.server