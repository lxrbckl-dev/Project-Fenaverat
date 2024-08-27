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
      
      self.myServers = myServers()
      self.myServersManager = myServersManager()
   
   
   def getProperty(self): return self.myServers.property
   
   
   def registerCallbacks(self):
      '''  '''
      
      self.callbackRow()
   
   
   def callbackRow(self):
      '''  '''
      
      @app.callback(
         
         output = Output('myServersRowId', 'children'),
         inputs = [Input('myServersDivId', 'children')]
         
      )
      def func(*args):

         return list(map(
            
            self.myServers.buildCard,
            self.myServersManager.getServers()
            
         ))