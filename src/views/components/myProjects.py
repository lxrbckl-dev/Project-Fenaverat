# import <
from ..body import body

from dash import (dcc, html)
import dash_bootstrap_components as dbc

# >


class myProjects(body):
   
   
   def __init__(self): super().__init__()
   
   
   @property
   def property(self):
      '''  '''

      return html.Div(
         
         id = 'myProjectsDivId',
         className = 'myProjectsDiv',
         children = dbc.Stack(
            
            children = None,
            id = 'myProjectsStackId',
            direction = 'horizontal',
            className = 'myProjectsStack'
            
         )
         
      )
      
   
   # def buildCard(
      
   #    self,
   #    name,
   #    properties,
   #    backgroundImage
      
   # ):
   #    '''  '''
      
   #    return html.Div(
         
   #       className = 'myServersCard',
   #       children = [
            
   #          # (header, body, footer) <
            
            
   #          # >
            
   #       ]
         
   #    )