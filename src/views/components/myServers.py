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
         className = 'myServerDiv',
         children = dbc.Row(
            
            children = None,
            id = 'myServersRowId'
            
         )
         
      )

      
   def buildCard(
      
      self, 
      node,
      styleMargins,
      backgroundColors
      
   ):
      '''  '''

      name, properties = node
      
      print(name)
      print(properties)
      print('==========')
      
      return dbc.Col(
         
         width = 3,
         className = 'myServersCol',
         children = [
            
            # (header, body, footer) <
            dbc.Row(
            
               children = html.H1(name)   
               
            ),
            dbc.Row(
               
               children = self.buildBadges(
                  
                  styleMargins = styleMargins,
                  backgroundColors = backgroundColors,
                  ecosystem = {'services' : properties['services']}
                  
               )
               
            ),
            dbc.Row()
            
            # >
            
         ]
         
      )