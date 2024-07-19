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
            Output('headerImagesColId', 'children')
            
         ]
         
      )
      def func(*args):
         
         title = self.headerManager.getTitle()
         images = self.headerManager.getImages()

         return [
            
            self.header.buildTitle(title),
            self.header.buildImages(images)
            
         ]