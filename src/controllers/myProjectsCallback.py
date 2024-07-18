# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.components.myProjects import myProjects
from ..models.myProjectsManager import myProjectsManager

# >


class myProjectsCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.id = 'myProjects'
      self.title = 'my projects'
      
      self.myProjects = myProjects()
      self.myProjectsManager = myProjectsManager()
   
   
   def register(self):
      '''  '''
      
      return self.myProjects.property