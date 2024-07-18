# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc

from ..controllers.bodyCallback import bodyCallback
from ..controllers.headerCallback import headerCallback
from ..controllers.footerCallback import footerCallback

# >


class layout:
   
   
   def __init__(self):
      '''  '''
      
      self.body = bodyCallback()
      self.header = headerCallback()
      self.footer = footerCallback()
   
   
   @property
   def property(self):
      '''  '''
      
      return dbc.Row(
         
         justify = 'center',
         className = 'layoutRow',
         children = dbc.Col(
            
            width = 10,
            children = [
               
               # header <
               # body <
               # footer <
               self.header.register(),
               self.body.register(),
               self.footer.register()
               
               # >
               
            ]
            
         )
         
      )