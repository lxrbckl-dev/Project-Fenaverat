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
            children = i.register()
            
         )
         
      for i in accordionItems]
      
      
   def buildCards(self):
      '''  '''
      
      pass
      
      
   def buildBadges(self, ecosystem):
      '''  '''
      
      pass