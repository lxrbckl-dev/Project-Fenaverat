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
      iconOS,
      iconHost,
      properties
      
   ):
      '''  '''
      
      return html.Div(
         
         className = 'myServersCard',
         children = [
            
            # (header, body, footer) <
            dbc.Row(
               
               justify = 'between',
               className = 'myServersRowHeader',
               children = [
                  
                  # (title, status) <
                  dbc.Col(
                     
                     width = 'auto',
                     children = self.buildCardTitle(name)
                                             
                  ),
                  dbc.Col(
                     
                     width = 'auto',
                     children = self.buildCardStatus(properties['status'])
                     
                  )
                  
                  # >
                  
               ]
               
            ),
            dbc.Row(
               
               className = 'myServersRowBody',
               children = self.buildBadges({'services' : properties['services']})
               
            ),
            dbc.Row(
               
               justify = 'between',
               className = 'myServersRowFooter',
               children = [
                  
                  # (os, host) <
                  dbc.Col(
                     
                     width = 'auto',
                     children = self.buildCardIconOS(iconOS)
                     
                  ),
                  dbc.Col(
                     
                     width = 'auto',
                     children = self.buildCardIconHost(iconHost)
                     
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
         
         spinnerClassName = {
            
            'down' : 'myServersCardStatusDown',
            'ready' : 'myServersCardStatusReady'
            
         }[status]
         
      )
      
      
   def buildCardIconOS(self, icon):
      '''  '''
      
      return html.Img(
         
         src = icon,
         className = 'myServersCardFooterIcon'
         
      )
   
   
   def buildCardIconHost(self, icon):
      '''  '''
      
      return html.Img(
         
         src = icon,
         className = 'myServersCardFooterIcon'
         
      )