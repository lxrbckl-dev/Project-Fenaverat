# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.components.aboutMe import aboutMe
from ..models.aboutMeManager import aboutMeManager

# >


class aboutMeCallback:
   
   
   def __init__(self):
      '''  '''
      
      self.id = 'aboutMe'
      self.title = 'about me'
      
      self.aboutMe = aboutMe()
      self.aboutMeManager = aboutMeManager()
   
   
   def register(self):
      '''  '''
      
      return self.aboutMe.property
   
   
   def callbackLeftStack(self):
      '''  '''
      
      @app.callback(
         
         output = Output('leftStackId', 'children'),
         inputs = [Input('leftStackId', 'children')]
         
      )
      def func(*args):
         
         return [
            
            self.aboutMe.buildPhoto,
            self.aboutMe.buildEcosystem
            
         ]
      
      
   def callbackRightStack(self):
      '''  '''
      
      @app.callback(
         
         inputs = [Input('rightCol', 'children')],
         output = Output('rightStackId', 'children')
         
      )
      def func(*args):
         
         return [
            
            self.aboutMe.buildTitle,
            self.aboutMe.buildDescription
            
         ]