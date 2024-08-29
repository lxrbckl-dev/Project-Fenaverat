# import <
from .loadManager import loadManager

# >


class bodyManager(loadManager):


   def __init__(self):
      '''  '''
   
      super().__init__(
         
         resources = {
            
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/body.json'
            
         }
         
      )
