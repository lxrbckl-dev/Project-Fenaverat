# import <
from dash.dependencies import (Input, Output)

from ..configs import app
from ..views.components.aboutMe import aboutMe
from ..models.aboutMeManager import aboutMeManager
from ..controllers.bodyCallback import bodyCallback

# >


class aboutMeCallback(bodyCallback):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__()
      
      self.id = 'aboutMe'
      self.title = 'about me'
      
      self.aboutMe = aboutMe()
      self.aboutMeManager = aboutMeManager()
      
      
   def getProperty(self): return self.aboutMe.property
   
   
   def registerCallbacks(self):
      '''  '''

      self.callbackRow()
         

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
               self.aboutMe.buildEcosystem(self.aboutMeManager.getEcosystem())
                  
            ],
            [
               
               self.aboutMe.buildText(self.aboutMeManager.getText())
                
            ]
            
            # >
            
         ]