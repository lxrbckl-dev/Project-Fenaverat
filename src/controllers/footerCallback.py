# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.footer import footer
from ..models.footerManager import footerManager

# >


class footerCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.footer = footer()
      self.footerManager = footerManager()
      
      
   def getProperty(self): return self.footer.property
      
   
   def registerCallbacks(self):
      '''  '''
      
      self.callbackConnections()
            
   
   def callbackConnections(self):
      '''  '''
      
      @app.callback(
         
         inputs = [Input('footerDivId', 'children')],
         output = Output('footerConnectionsRowId', 'children')
         
      )
      def func(*args):
         '''  '''

         return [
            
            self.footer.buildConnection(
               
               link = link,
               icon = icon
               
            )
            
         for link, icon in self.footerManager.getConnections().items()]