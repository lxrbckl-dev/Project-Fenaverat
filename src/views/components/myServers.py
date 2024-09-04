# import <
from ..body import body

from dash import (dcc, html)
import dash_bootstrap_components as dbc

# >


class myServers(body):
   
   
   def __init__(self): super().__init__()
   
   
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
      
      
   def buildMyServersCard(
      
      self,
      name,
      iconOS,
      iconHost,
      properties,
      iconHardware
      
   ):
      '''  '''

      return self.buildCard(
         
         cardHeight = '200px',
         headerJustify = 'between',
         headerChildren = [
            
            # title <
            # (os, hardware) <
            dbc.Col(
               
               width = 'auto',
               children = self.buildCardTitle(name, '19px')
               
            ),
            dbc.Col(
               
               width = 'auto',
               children = dbc.Stack(
                  
                  gap = 3,
                  direction = 'horizontal',
                  children = [
                     
                     dbc.Col(
                        
                        width = 'auto',
                        children = self.buildCardIcon(iconOS)
                        
                     ),
                     dbc.Col(
                        
                        width = 'auto',
                        children = self.buildCardIcon(iconHardware)
                        
                     )
                     
                  ]
                  
               )
               
            )
            
         ],
         
         bodyChildren = self.buildBadges({'services' : properties['services']}),
         
         footerJustify = 'between',
         footerChildren = [
            
            # (status, host) <
            dbc.Col(
               
               width = 'auto',
               children = self.buildCardStatus(properties['status'])
               
            ),
            dbc.Col(
               
               width = 'auto',
               children = self.buildCardIcon(iconHost)
               
            )
            
            # >
            
         ]
         
      )
      
      
   def buildCardStatus(self, status):
      '''  '''
      
      return dbc.Spinner(
         
         spinnerClassName = {
            
            'down' : 'myServersStatusDown',
            'ready' : 'myServersStatusReady'
            
         }[status]
         
      )