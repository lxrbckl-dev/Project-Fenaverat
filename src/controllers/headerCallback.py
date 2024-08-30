# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.header import header
from ..models.headerManager import headerManager

# >


class headerCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.header = header()
      self.headerManager = headerManager()
      
      
   def getProperty(self): return self.header.property
      
      
   def registerCallbacks(self):
      '''  '''
      
      self.callbackRow()
               

   def callbackRow(self):
      '''  '''

      @app.callback(
         
         inputs = [Input('headerRowId', 'children')],
         output = [
            
            Output('headerTitleColId', 'children'),
            Output('headerAvatarsColId', 'children')
            
         ]
         
      )
      def func(*args):

         return [
            
            self.header.buildTitle(self.headerManager.getTitle()),
            self.header.buildAvatars(self.headerManager.getAvatars())
            
         ]