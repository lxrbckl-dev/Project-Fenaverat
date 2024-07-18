# import <
from time import sleep
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
      self.sleepTime = 1
      self.activeItem = 'aboutMe'
      self.bodyManager = bodyManager()
      self.aboutMeCallback = aboutMeCallback()
      self.myServersCallback = myServersCallback()
      self.myProjectsCallback = myProjectsCallback()
      
      self.items = [
         
         self.aboutMeCallback,
         self.myServersCallback,
         self.myProjectsCallback
         
      ]
   
   
   def register(self):
      '''  '''
      
      self.callbackAccordion()
      self.callbackActiveItem()
      self.aboutMeCallback.register()
      self.myServersCallback.register()
      self.myProjectsCallback.register()
      
      return self.body.property
   
   
   def callbackAccordion(self):
      '''  '''

      @app.callback(
         
         inputs = [Input('bodyColId', 'children')],
         output = Output('bodyAccordionId', 'children')
         
      )
      def func(*args): return self.body.buildAccordion(self.items)
      
      
   def callbackActiveItem(self):
      '''  '''
      
      @app.callback(
         
         output = Output('bodyAccordionId', 'active_item'),
         inputs = [Input((self.activeItem + 'RowId'), 'children')]
         
      )
      def func(*args): 
         
         sleep(self.sleepTime)
         return self.activeItem