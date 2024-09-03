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
      properties,
      iconHardware
      
   ):
      '''  '''

      return self.buildCard(
         
         headerJustify = 'between',
         headerChildren = [
            
            # title <
            # (os, hardware) <
            dbc.Col(
               
               width = 'auto',
               children = self.buildMyServersTitle(name)
               
            ),
            dbc.Col(
               
               width = 'auto',
               children = dbc.Stack(
                  
                  direction = 'horizontal',
                  children = [
                     
                     dbc.Col(
                        
                        width = 'auto',
                        children = self.buildMyServersIcon(iconOS)
                        
                     ),
                     dbc.Col(
                        
                        width = 'auto',
                        children = self.buildMyServersIcon(iconHardware)
                        
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
               children = self.buildMyServersStatus(properties['status'])
               
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