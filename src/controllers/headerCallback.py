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
      
      
   def register(self):
      '''  '''
      
      self.callbackTitle()
      self.callbackPictures()
      
      return self.header.property
   
   
   def callbackTitle(self):
      '''  '''
   
      @app.callback(
         
         output = Output('headerTitleH1Id', 'children'),
         inputs = [Input('headerTitleColId', 'children')]
         
      )
      def func(*args): return self.headerManager.getTitle()
   
   
   def callbackPictures(self):
      '''  '''
   
      @app.callback(
         
         inputs = [Input('headerImagesColId', 'children')],
         output = Output('headerImagesStackId', 'children')
         
      )
      def func(*args): 
         
         images = self.headerManager.getImages()
         return self.header.buildPictures(images)