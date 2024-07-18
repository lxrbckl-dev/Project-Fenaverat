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