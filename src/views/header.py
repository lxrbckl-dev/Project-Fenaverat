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
               className = 'headerTitleCol',
               children = html.H1(
                  
                  children = None,
                  id = 'headerTitleH1Id',
                  className = 'headerTitleH1'
                  
               )
               
            ),
            dbc.Col(
               
               width = 'auto',
               align = 'center',
               id = 'headerImagesColId',
               className = 'headerImagesCol',
               children = dbc.Stack(
                  
                  gap = 3,
                  children = None,
                  direction = 'horizontal',
                  id = 'headerImagesStackId'
                  
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