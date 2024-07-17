# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc

# from .components.header import header
# from .components.footer import footer
# from .components.aboutMe import aboutMe
# from .components.myServers import myServers
# from .components.myProjects import myProjects

from ..controllers.headerCallback import headerCallback
from ..controllers.footerCallback import footerCallback

# >


class layout:
   
   
   def __init__(self):
      '''  '''
      
      self.header = headerCallback()
      self.footer = footerCallback()
   
   
   @property
   def property(self):
      '''  '''
      
      return dbc.Row(
         
         justify = 'center',
         className = 'layoutRow',
         children = dbc.Col(
            
            width = 9,
            children = [
               
               # header <
               # body <
               # footer <
               self.header.register(),
               
               
               
               self.footer.register()
               
               # >
               
            ]
            
         )
         
      )