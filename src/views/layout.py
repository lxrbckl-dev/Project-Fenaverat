# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc

from ..controllers.bodyCallback import bodyCallback
from ..controllers.headerCallback import headerCallback
from ..controllers.footerCallback import footerCallback
from ..controllers.aboutMeCallback import aboutMeCallback
from ..controllers.myServersCallback import myServersCallback
from ..controllers.myProjectsCallback import myProjectsCallback

# >


class layout:
   
   
   def __init__(self):
      '''  '''
      
      self.header = headerCallback()
      
      self.body = bodyCallback(
         
         components = [
            
            aboutMeCallback(),
            myServersCallback(),
            myProjectsCallback()
            
         ]
         
      )
      
      self.footer = footerCallback()
      
   
   def registerCallbacks(self):
      '''  '''
   
      self.header.registerCallbacks()
      self.body.registerCallbacks()
      self.footer.registerCallbacks()
   
   
   @property
   def property(self):
      '''  '''
      
      return dbc.Row(
         
         justify = 'center',
         className = 'layoutRow',
         children = [
            
            dcc.Location(id = 'layoutLocation'),
            
            dbc.Col(
               
               className = 'layoutCol',
               children = [
                  
                  # header <
                  # body <
                  # footer <
                  self.header.getProperty(),
                  self.body.getProperty(),
                  self.footer.getProperty()
                  
                  # >
                  
               ]
               
            )
            
         ]

         # children = dbc.Col(
            
         #    className = 'layoutCol',
         #    children = [
               
               
               
         #       # header <
         #       # body <
         #       # footer <
         #       self.header.getProperty(),
         #       self.body.getProperty(),
         #       self.footer.getProperty()
               
         #       # >
               
         #    ]
            
         # )
         
      )