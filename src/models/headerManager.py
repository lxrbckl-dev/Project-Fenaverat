# import <
from .loadManager import loadManager

# >


class headerManager(loadManager):
   

   def __init__(self):
      '''  '''

      self.key = 'header'
      super().__init__(
         
         resources = {
            
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/header.json'
            
         }
         
      )
      
      
   def getTitle(self): return self.files[self.key]['title']
   
   
   def getAvatars(self): return self.files[self.key]['avatars']