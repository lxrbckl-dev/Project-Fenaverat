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
      iconWiki,
      properties,
      iconRepository,
      backgroundImage
      
   ):
      '''  '''
            
      return self.buildCard(
         
         cardHeight = '275px',
         headerJustify = 'start',
         cardBackground = backgroundImage,
         headerChildren = dbc.Col(
            
            width = 'auto',
            children = [
               
               # (title, description) <
               self.buildCardTitle(name, '22px'),
               self.buildCardDescription(properties['description'])
               
               # >
               
            ]
            
         ),
         
         bodyChildren = self.buildBadges({
         
            'Languages' : properties['languages'],
            'Packages' : properties['topics']
            
         }),
         
         footerJustify = 'between',
         footerChildren = [
            
            # (wiki, repository) <
            dbc.Col(
               
               width = 'auto',
               children = self.buildCardLink(
                  
                  icon = iconWiki,
                  link = properties['url'] + '/wiki'
                  
               )
               
            ),
            dbc.Col(
               
               width = 'auto',
               children = self.buildCardLink(
                  
                  icon = iconRepository,
                  link = properties['url']
                  
               )
               
            )
            
            # >
            
         ]
         
      )
      
      
   def buildCardDescription(self, description):
      '''  '''
      
      return html.P(
         
         children = f'{description}.',
         className = 'myProjectsDescriptionP'
         
      )
      
      
   def buildCardLink(self, link, icon):
      '''  '''
      
      return html.A(
         
         href = link,
         target = '_blank',
         children = self.buildCardIcon(icon)
         
      )