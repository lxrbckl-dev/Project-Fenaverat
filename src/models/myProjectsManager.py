# import <
from .resourceManager import resourceManager

# >


class myProjectsManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'body',
         loadType = 'remote'
         
      )