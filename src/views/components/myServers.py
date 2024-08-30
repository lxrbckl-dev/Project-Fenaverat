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
      
      
   def buildMyServerCard(
      
      self,
      name,
      iconOS,
      iconHost,
      properties
      
   ):
      '''  '''

      return self.buildCard(
         
         justifyHeader = 'between',
         header = [
            
            # (title, status) <
            dbc.Col(
               
               width = 'auto',
               children = self.buildMyServersTitle(name)
                                       
            ),
            dbc.Col(
               
               width = 'auto',
               children = self.buildMyServersStatus(properties['status'])
               
            )
            
            # >
            
         ],
                  
         body = self.buildBadges({'services' : properties['services']}),
         
         justifyFooter = 'between',
         footer = [
            
            # (os, host) <
            dbc.Col(
               
               width = 'auto',
               children = self.buildMyServersIcon(iconOS)
               
            ),
            dbc.Col(
               
               width = 'auto',
               children = self.buildMyServersIcon(iconHost)
               
            )
            
            # >
            
         ]
         
      )

      
   def buildMyServersTitle(self, title):
      '''  '''
      
      return html.H4(
         
         children = title,
         className = 'myServersTitleH4'
         
      )
      
      
   def buildMyServersStatus(self, status):
      '''  '''
      
      return dbc.Spinner(
         
         spinnerClassName = {
            
            'down' : 'myServersStatusDown',
            'ready' : 'myServersStatusReady'
            
         }[status]
         
      )
      
      
   def buildMyServersIcon(self, icon):
      '''  '''
      
      return html.Img(
         
         src = icon,
         className = 'myServersIconImg'
         
      )