# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc

# >


class header:
   
   
   def __init__(self):
      '''  '''
      
      pass
   

   @property
   def property(self):
      '''  '''

      return dbc.Row(
         
         justify = 'between',
         className = 'headerRow',
         children = [
            
            # title <
            # images <
            dbc.Col(
               
               width = 'auto',
               id = 'headerTitleColId',
               children = html.H1(
                  
                  children = None,
                  id = 'headerTitleId',
                  className = 'headerTitle'
                  
               )
               
            ),
            dbc.Col(
               
               width = 'auto',
               align = 'center',
               id = 'headerImagesColId',
               children = dbc.Stack(
                  
                  gap = 3,
                  children = None,
                  id = 'headerImagesId',
                  direction = 'horizontal'
                  
               )
                                 
            )
            
            # >
            
         ]
         
      )
      
      
   def buildPictures(self, urls):
      '''  '''
      
      return [
         
         html.Img(
            
            src = url,
            className = 'headerImage'
            
         )
         
      for url in urls]