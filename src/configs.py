# import <
from dash import Dash
from os import environ
from dash_bootstrap_components import themes

# >


# referencing outsourced Dockerfile <
# ref: 
port = environ.get('port')
host = environ.get('host')

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