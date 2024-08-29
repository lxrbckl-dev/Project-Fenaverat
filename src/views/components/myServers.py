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

      return dbc.Row(
         
         id = 'myServersRowId',
         className = 'myServersRow',
         children = dbc.Stack(
            
            children = None,
            id = 'myServersStackId',
            direction = 'horizontal'
            
         )
         
      )

      
   def buildCard(
      
      self, 
      name,
      properties
      
   ):
      '''  '''

      return html.Div(
         
         className = 'myServersCardDiv',
         children = [
            
            # (header, body, footer) <
            dbc.Row(
               
               children = [
                  
                  
                  
               ]
               
            )

            # html.H1(name),
            # self.buildBadges({'services' : properties['services']}
               
            # )
            
            # >
            
         ]
         
      )
      
      
   def buildCardStatus(self, status):
      '''  '''
      
      return 