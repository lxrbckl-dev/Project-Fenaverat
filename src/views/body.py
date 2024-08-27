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
      
      
   def buildCard(
      
      self,
      header,
      body,
      footer
      
   ):
      '''  '''
      
      return dbc.Col(
         
         className = 'cardCol',
         children = dbc.Card(
            
            children = [
               
               # header <
               # body <
               # footer <
               dbc.CardHeader(
                  
                  children = header,
                  className = 'cardHeader'
                  
               ),
               dbc.CardBody(
                  
                  children = body,
                  className = 'cardBody'
                  
               ),
               dbc.CardFooter(
                  
                  children = footer,
                  className = 'cardFooter'
                  
               )
               
               # >
               
            ]
            
         )
         
      )
      
      
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