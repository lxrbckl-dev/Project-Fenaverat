# import <
from .framework import framework

from dash import dcc, html
import dash_bootstrap_components as dbc

# >


class header(framework):
   
   def __init__(self): 
      
      super().__init__()
      self.file = 'header'
   
   
   def component(
      
      self,
      pStyle,
      pContent,
      
      pKey = 'component'
   
   ):
      '''  '''

      return dbc.Col(
         
         style = {
            
            'minWidth' : self.colWidth,
            'maxWidth' : self.colWidth,
            **pStyle[self.file][pKey]['col'],
            'background' : pStyle['framework']['colorWhite']
            
         },
         children = dbc.Row(
            
            justify = 'between',
            children = [
               
               # title <
               # profiles <
               dbc.Col(
                  
                  width = 'auto',
                  children = html.H1(
                     
                     children = pContent[self.file]['title'],
                     style = {
                        
                        **pStyle[self.file][pKey]['titleH1'],
                        'background' : pStyle['framework']['colorWhite']
                        
                     }
                     
                  )
                  
               ),
               dbc.Col(
                  
                  width = 'auto',
                  style = pStyle[self.file][pKey]['rightCol'],
                  children = dbc.Stack(
                     
                     gap = 3,
                     direction = 'horizontal',
                     children = [
                        
                        html.Img(
                           
                           src = i,
                           style = {
                              
                              **pStyle[self.file][pKey]['titleImg'],
                              'border' : pStyle['framework']['borderBlack']
                              
                           }
                           
                        )
                        
                     for i in pContent[self.file]['profiles']]
                     
                  )
                  
               )
               
               # >
               
            ]
            
         )
                     
      )