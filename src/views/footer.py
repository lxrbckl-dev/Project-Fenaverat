# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc

# >


class footer:
   
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   @property
   def property(self):
      '''  '''
      
      return dbc.Col(
         
         id = 'footerColId',
         className = 'footerCol',
         children = [
            
            # connections <
            dbc.Row(
               
               children = None,
               justify = 'between',
               id = 'footerConnectionsRowId'
               
            )
            
            # >
            
         ]
         
      )
      
      
   def buildConnections(self, connections):
      '''  '''
      
      return [
         
         dbc.Col(
            
            width = 'auto',
            children = html.A(
               
               href = v['url'],
               target = '_blank',
               children = html.Img(
                  
                  alt = k,
                  src = v['icon'],
                  className = 'footerConnection'
                  
               )
               
            )
            
         )
         
      for k, v in connections.items()]