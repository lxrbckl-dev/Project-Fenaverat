# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.components.myServers import myServers
from ..controllers.bodyCallback import bodyCallback
from ..models.myServersManager import myServersManager

# >


class myServersCallback(bodyCallback):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__()
      
      self.id = 'myServers'
      self.title = 'my servers'
      
      self.myProjects = myServers()
      self.myServersManager = myServersManager()
   
   
   def getProperty(self): return self.myProjects.property
   
   
   def registerCallbacks(self):
      '''  '''
      
      pass