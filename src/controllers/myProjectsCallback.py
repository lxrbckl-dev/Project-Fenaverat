# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..controllers.bodyCallback import bodyCallback
from ..views.components.myProjects import myProjects
from ..models.myProjectsManager import myProjectsManager

# >


class myProjectsCallback(bodyCallback):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__()
      
      self.id = 'myProjects'
      self.title = 'my projects'
      
      self.myProjects = myProjects()
      self.myProjectsManager = myProjectsManager()
   
   
   def getProperty(self): return self.myProjects.property
   
   
   def registerCallbacks(self):
      '''  '''
      
      self.callbackRow()
   
   
   def callbackRow(self):
      '''  '''
      
      @app.callback(
         
         output = Output('myProjectsRowId', 'children'),
         inputs = [Input('myProjectsColId', 'children')]
         
      )
      def func(*args):
         
         pass