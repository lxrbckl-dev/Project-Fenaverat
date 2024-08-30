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
            
            # (title, avatars) <
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
               id = 'headerAvatarsColId',
               className = 'headerAvatarsCol'
               
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
                  
                  True : 'headerLetterH1Pixel',
                  False : 'headerLetterH1Normal'
                  
               }[(randint(1, 4) == 1)]
                          
            )
            
            # >
            
         for i in title]
         
      )
      
      
   def buildAvatars(self, avatars):
      '''  '''
      
      return dbc.Stack(
         
         gap = 3,
         id = 'headerStackId',
         direction = 'horizontal',
         children = [
            
            # avatar <
            html.Img(
               
               src = avatar,
               className = 'headerAvatarImg'
               
            )
            
            # >
            
         for avatar in avatars]
         
      )