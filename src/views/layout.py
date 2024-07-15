# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc

from .components.header import header
from .components.footer import footer
from .components.aboutMe import aboutMe
from .components.myServers import myServers
from .components.myProjects import myProjects

# >


class layout:
   
   
   def __init__(self):
      '''  '''
      
      self.header = header()
      self.footer = footer()
      self.aboutMe = aboutMe()
      self.myServers = myServers()
      self.myProjects = myProjects()
   
   
   @property
   def property(self):
      '''  '''
      
      return dbc.Row(
         
         justify = 'center',
         className = 'layoutRow',
         children = dbc.Col(
            
            width = 7,
            # className = 'layoutCol',
            children = [
               
               # header <
               # body <
               # footer <
               self.header.property,
               
               self.aboutMe.property,
               self.myServers.property,
               self.myProjects.property,
               
               self.footer.property
               
               # >
               
            ]
            
         )
         
      )