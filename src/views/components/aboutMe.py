# import <
from ..body import body

from dash import (dcc, html)
from dash_player import DashPlayer
import dash_bootstrap_components as dbc

# >


class aboutMe(body):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__()
   
   
   @property
   def property(self):
      '''  '''
      
      return dbc.Row(
         
         id = 'aboutMeRowId',
         className = 'aboutMeRow',
         children = [
            
            # left (photo, ecosystem) <
            # right (text) <
            dbc.Col(
               
               width = 4,
               className = 'aboutMeLeftCol',
               children = dbc.Stack(
                  
                  children = None,
                  id = 'aboutMeLeftStackId'
                  
               )
               
            ),
            dbc.Col(
               
               width = 8,
               className = 'aboutMeRightCol',
               children = dbc.Stack(
                  
                  children = None,
                  id = 'aboutMeRightStackId'
                  
               )
               
            )
            
            # >
            
         ]
         
      )
      
      
   def buildPhoto(self, url):
      '''  '''
      
      return DashPlayer(
         
         url = url,
         muted = True,
         width = '100%',
         height = '100%',
         playing = False,
         controls = False,
         id = 'aboutMePhotoDashPlayerId',
         className = 'aboutMePhotoDashPlayer'
         
      )
   
   
   def buildEcosystem(
      
      self, 
      ecosystem,
      styleMargins,
      backgroundColors
      
   ):
      '''  '''
      
      return html.Div(
         
         className = 'aboutMeEcosystemDiv',
         children = self.buildBadges(
         
            ecosystem = ecosystem,
            styleMargins = styleMargins,
            backgroundColors = backgroundColors
         
         )
         
      )
      
      
   def buildText(self, text):
      '''  '''
      
      return dcc.Markdown(
         
         children = '\n\n'.join(text),
         className = 'aboutMeTextMarkdown'
         
      )