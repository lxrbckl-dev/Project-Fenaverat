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

      self.callbackRow()
      
      return self.aboutMe.property
   

   def callbackRow(self):
      '''  '''

      @app.callback(
         
         inputs = [Input('aboutMeRowId', 'children')],
         output = [
            
            Output('aboutMeLeftStackId', 'children'),
            Output('aboutMeRightStackId', 'children')
            
         ]
         
      )
      def func(*args):
      
         return [
            
            # left <
            # right <
            [
               
               self.aboutMe.buildPhoto(self.aboutMeManager.getPhoto()),
               *self.aboutMe.buildEcosystem(self.aboutMeManager.getEcosystem())
                  
            ],
            [
               
               self.aboutMe.buildTitle(self.aboutMeManager.getTitle()),
               self.aboutMe.buildDescription(self.aboutMeManager.getDescription())
               
            ]
            
            # >
            
         ]