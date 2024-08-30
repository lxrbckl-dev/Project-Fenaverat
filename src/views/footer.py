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
      
      return html.Div(
         
         id = 'footerDivId',
         className = 'footerDiv',
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
      

   def buildConnection(self, link, icon):
      '''  '''

      return dbc.Col(
         
         width = 'auto',
         children = html.A(
            
            href = link,
            target = '_blank',
            children = html.Img(
               
               src = icon,
               className = 'footerConnectionImg'
               
            )
            
         )
         
      )