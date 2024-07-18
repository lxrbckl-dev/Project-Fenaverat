# import <
from ..body import body

from dash import (dcc, html)
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
            
            # (photo, ecosystem) <
            # (title, description) <
            dbc.Col(
               
               width = 4,
               className = 'leftCol',
               children = dbc.Stack(
                  
                  children = None,
                  id = 'leftStackId'
                  
               )
               
            ),
            dbc.Col(
               
               width = 8,
               className = 'rightCol',
               children = dbc.Stack(
                  
                  children = None,
                  id = 'rightStackId'
                  
               )
               
            )
            
            # >
            
         ]
         
      )
      
      
   def buildPhoto(self):
      '''  '''
      
      pass
   
   
   def buildEcosystem(self, ecosystem):
      '''  '''
      
      pass
   
   
   def buildTitle(self, title):
      '''  '''
      
      pass
   
   
   def buildDescription(self, description):
      '''  '''
      
      pass