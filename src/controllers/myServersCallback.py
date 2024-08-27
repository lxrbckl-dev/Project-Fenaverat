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
         inputs = [Input('myServersColId', 'children')]
         
      )
      def func(*args):
         
         return [
            
            self.body.buildCard(
               
               header = self.myServers.buildHeader(
                  
                  name = server['name'],
                  status = server['status']
               
               ),
               body = self.myServers.buildBody(
                  
                  services = server['services']
                  
               ),
               footer = self.myServers.buildFooter()
               
            )
            
         for server in self.myServersManager.getServers()]