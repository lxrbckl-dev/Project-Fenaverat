# import <
from random import randint
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
         
         id = 'headerRowId',
         justify = 'between',
         className = 'headerRow',
         children = [
            
            # title <
            # images <
            dbc.Col(
               
               width = 'auto',
               children = None,
               id = 'headerTitleColId',
               className = 'headerTitleCol'
               
            ),
            dbc.Col(
               
               width = 'auto',
               children = None,
               align = 'center',
               id = 'headerImagesColId',
               className = 'headerImagesCol'
               
            )
            
            # >
            
         ]
         
      )
      
      
   def buildTitle(self, title):
      '''  '''
      
      return html.Div(
         
         children = [
            
            # letter <
            html.H1(
               
               children = i,
               className = {
                  
                  True : 'letterH1Pixel',
                  False : 'letterH1Normal'
                  
               }[(randint(1, 3) == 1)]
                          
            )
            
            # >
            
         for i in title]
         
      )
      
      
   def buildImages(self, images):
      '''  '''
      
      return dbc.Stack(
         
         gap = 3,
         direction = 'horizontal',
         id = 'headerImagesStackId',
         children = [
            
            html.Img(
               
               src = image,
               className = 'headerImagesImg'
               
            )
            
         for image in images]
         
      )