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
         children = [
            
            # (header, body, footer) <
            dbc.Row(
               
               justify = 'between',
               className = 'myServersRow',
               children = [
                  
                  # (title, status) <
                  dbc.Col(
                     
                     width = 11,
                     children = self.buildCardTitle(name)
                                             
                  ),
                  dbc.Col(
                     
                     width = 1,
                     children = self.buildCardStatus(properties['status'])
                     
                  )
                  
                  # >
                  
               ]
               
            )
            
            # >
            
         ]
         
      )
      
      
   def buildCardTitle(self, title):
      '''  '''
      
      return html.H4(
         
         children = title,
         className = 'myServersCardTitle'
         
      )
      
      
   def buildCardStatus(self, status):
      '''  '''
      
      return dbc.Spinner(
         
         type = 'grow',
         spinnerClassName = {
            
            'down' : 'myServersCardStatusOffline',
            'ready' : 'myServersCardStatusOnline',
            'online' : 'myServersCardStatusOnline',
            'offline' : 'myServersCardStatusOffline'
            
         }[status]
         
      )