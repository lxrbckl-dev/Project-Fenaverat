# import <
from ..configs import app
from ..models.headerManager import headerManager

from dash.dependencies import (
   
   Input,
   State,
   Output
   
)

# >


class headerCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.headerManager = headerManager()
   
   
   def register(self):
      '''  '''
      
      @app.callback(
         
         output = [
            
            Output('headerTitleId', 'children'),
            Output('headerPicturesId', 'children')
            
         ],
         inputs = [Input('headerColId', 'children')]
         
      )
      def func(*args):
         '''  '''         
         
         return [
            
            'ok', 
            'here'
            
         ]