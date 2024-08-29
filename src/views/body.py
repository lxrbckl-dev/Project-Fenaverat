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

      return html.Div(
         
         id = 'bodyDivId',
         className = 'bodyDiv',
         children = dbc.Accordion(
            
            flush = True,
            active_item = None,
            id = 'bodyAccordionId',
            children = [
               
               
               
            ]
            
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
      
      
   def buildBadges(self, iterDict):
      '''  '''
      
      return html.Div(
         
         className = 'bodyBadgeDiv',
         children = [
            
            dbc.Badge(
               
               children = i,
               className = f'{k}Badge'
               
            )
                        
         for k, v in iterDict.items() for i in v]
                  
      )