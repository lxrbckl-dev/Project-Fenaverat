# import <
from .loadManager import loadManager

# >


class headerManager(loadManager):
   

   def __init__(self):
      '''  '''

      super().__init__(
         
         key = 'header',
         resources = [
            
            {
               
               'id' : 'header',
               'load' : 'local',
               'link' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/header.json'
               
            }
            
         ]
         
      )
      
      
   def getTitle(self): return self.files[self.key]['title']
   
   
   def getAvatars(self): return self.files[self.key]['avatars']