# import <
from .resourceManager import resourceManager

# >


class aboutMeManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'body',
         loadType = 'local'
         
      )