# import <
# from ..body import body
from ..components.myServers import myServers

from dash import (dcc, html)
import dash_bootstrap_components as dbc

# >


class myProjects(myServers):
   
   
   def __init__(self): super().__init__()
   
   
   @property
   def property(self):
      '''  '''

      return html.Div(
         
         id = 'myProjectsDivId',
         className = 'myProjectsDiv',
         children = dbc.Stack(
            
            children = None,
            id = 'myProjectsStackId',
            direction = 'horizontal',
            className = 'myServersStack'
            
         )
         
      )
      
      
   def buildMyProjectsCard(
      
      self,
      name,
      properties,
      backgroundImage
      
   ):
      '''  '''
      
      # print(properties)
      # print('---')
            
      return self.buildCard(
         
         headerJustify = 'start',
         headerChildren = dbc.Col(
            
            width = 'auto',
            children = [
               
               # (title, description) <
               self.buildCardTitle(name),
               self.buildCardDescription(properties['description'])
               
               # >
               
            ]
            
         ),
         
         bodyChildren = None,
         
         footerJustify = 'start',
         footerChildren = [
            
            # (repository, wiki) <
            
            
            # >
            
         ]
         
      )
      
      
   def buildCardDescription(self, description):
      '''  '''
      
      return html.P(
         
         children = f'{description}.',
         className = 'myProjectsDescriptionP'
         
      )