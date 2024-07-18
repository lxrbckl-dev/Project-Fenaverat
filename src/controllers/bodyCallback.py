# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.body import body
from ..models.bodyManager import bodyManager

from .aboutMeCallback import aboutMeCallback
from .myServersCallback import myServersCallback
from .myProjectsCallback import myProjectsCallback


# >


class bodyCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.body = body()
      self.bodyManager = bodyManager()
      
      self.items = [
         
         aboutMeCallback(),
         myServersCallback(),
         myProjectsCallback()
         
      ]
   
   
   def register(self):
      '''  '''
      
      self.callbackAccordion()
      
      return self.body.property
   
   
   def callbackAccordion(self):
      '''  '''

      @app.callback(
         
         inputs = [Input('bodyColId', 'children')],
         output = Output('bodyAccordionId', 'children')
         
      )
      def func(*args): return self.body.buildAccordion(self.items)