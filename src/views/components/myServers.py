# import <
from ..body import body

from dash import (dcc, html)
import dash_bootstrap_components as dbc

# >


class myServers(body):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__()
   
   
   @property
   def property(self):
      '''  '''

      return html.Div(
         
         id = 'myServersDivId',
         className = 'myServersDiv',
         children = dbc.Stack(
            
            children = None,
            id = 'myServersStackId',
            direction = 'horizontal',
            className = 'myServersStack'
            
         )
         
      )

      
   def buildCard(
      
      self, 
      name,
      properties
      
   ):
      '''  '''
      
      return html.Div(
         
         className = 'myServersCard',
         children = html.H1('okokook')
         
      )
      
      
   def buildCardStatus(self, status):
      '''  '''
      
      return None