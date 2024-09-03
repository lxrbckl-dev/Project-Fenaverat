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
      
      
   def buildBadges(self, iterDict):
      '''  '''
      
      return html.Div(
         
         className = 'buildBadgesDiv',
         children = [
            
            dbc.Badge(
               
               children = i,
               className = f'badge{k.title()}'
               
            )
                        
         for k, v in iterDict.items() for i in v]
                  
      )
      
      
   def buildCard(
      
      self,
      bodyHeight,
      bodyChildren,
      headerChildren, 
      footerChildren,
      footerJustify = 'end',
      headerJustify = 'between'
      
   ):
      '''  '''
      
      return html.Div(
         
         className = 'buildCardDiv',
         children = [
            
            # (header, body, footer) <
            dbc.Row(
               
               justify = headerJustify,
               children = headerChildren,
               className = 'buildCardHeaderRow'
               
            ),
            dbc.Row(
               
               children = bodyChildren,
               className = 'buildCardBodyRow',
               style = {
                  
                  'minHeight' : bodyHeight,
                  'maxHeight' : bodyHeight
                  
               }
               
            ),
            dbc.Row(
               
               justify = footerJustify,
               children = footerChildren,
               className = 'buildCardFooterRow'
               
            )
            
            # >
            
         ]
         
      )
      
      
   def buildCardIcon(self, icon):
      '''  '''
      
      return html.Img(
         
         src = icon,
         className = 'buildCardIconImg'
         
      )
      
      
   def buildCardTitle(self, title):
      '''  '''
      
      return html.H4(
         
         className = 'buildCardTitleH4',
         children = title.replace('-', ' ')
         
      )