# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.components.myServers import myServers
from ..models.myServersManager import myServersManager

# >


class myServersCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.id = 'myServers'
      self.title = 'my servers'
      
      self.myProjects = myServers()
      self.myServersManager = myServersManager()
   
   
   def register(self):
      '''  '''
      
      return self.myProjects.property