# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.components.footer import footer
from ..models.footerManager import footerManager

# >


class footerCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.footer = footer()
      self.footerManager = footerManager()
      
   
   def register(self):
      '''  '''
      
      self.callbackConnections()
      
      return self.footer.property
   
   
   def callbackConnections(self):
      '''  '''
      
      @app.callback(
         
         output = Output('footerRowId', 'children'),
         inputs = [Input('footerColId', 'children')]
         
      )
      def func(*args):

         connections = self.footerManager.getConnections()
         return self.footer.buildConnections(connections)