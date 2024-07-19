# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc

# >


class body:
   
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   @property
   def property(self):
      '''  '''

      return dbc.Col(
         
         id = 'bodyColId',
         className = 'bodyCol',
         children = dbc.Accordion(
            
            flush = True,
            children = None,
            active_item = None,
            id = 'bodyAccordionId'
            
         )
                  
      )
      
      
   def buildAccordion(self, accordionItems):
      '''  '''
      
      return [
         
         dbc.AccordionItem(
            
            item_id = i.id,
            title = i.title,
            children = i.getProperty()
            
         )
         
      for i in accordionItems]
      
      
   def buildCards(self):
      '''  '''
      
      pass
      
      
   def buildBadges(
      
      self, 
      textColor,
      ecosystem,
      backgroundColors
      
   ):
      '''  '''
      
      return html.Div(
         
         className = 'badgeDiv',
         children = [
            
            dbc.Badge(
               
               children = i,
               className = 'badge',
               color = backgroundColors[k],
               style = {'color' : textColor}
               
            )
                        
         for k, v in ecosystem.items() for i in v]
                  
      )