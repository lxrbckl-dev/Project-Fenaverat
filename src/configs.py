# import <
from dash import Dash
from dash_bootstrap_components import themes

# >


app = Dash(
   
   name = 'lxRbckl',
   title = 'lxRbckl',
   assets_folder = 'src/assets',
   suppress_callback_exceptions = True,
   external_stylesheets = [
      
      themes.GRID,
      themes.BOOTSTRAP,
      './assets/layout.css'
      
   ]
   
)

server = app.server