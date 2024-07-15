# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc

from ...controllers.headerCallback import headerCallback

# >


class header:
   
   
   def __init__(self):
      '''  '''
      
      self.headerCallback = headerCallback()
      self.headerCallback.register()
   
   
   @property
   def property(self):
      '''  '''
      
      return dbc.Col(
         
         id = 'headerColId',
         className = 'headerCol',
         children = dbc.Row(
            
            justify = 'between',
            children = [
               
               # title <
               # pictures <
               dbc.Col(
                  
                  width = 'auto',
                  children = html.H1(
                     
                     children = None,
                     id = 'headerTitleId',
                     className = 'headerTitle'
                     
                  )
                  
               ),
               dbc.Col(
                  
                  width = 'auto',
                  className = 'headerPictures',
                  children = dbc.Stack(
                     
                     gap = 3,
                     children = None,
                     id = 'headerPicturesId',
                     direction = 'horizontal'
                     
                  )
                                    
               )
               
               # >
               
            ]
            
         )
         
      )