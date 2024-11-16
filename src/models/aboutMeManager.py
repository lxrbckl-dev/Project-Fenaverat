# import <
from .loadManager import loadManager

# >


class aboutMeManager(loadManager):
   

   def __init__(self):
      '''  '''

      self.key = 'aboutMe'
      super().__init__(
         
         resources = {
            
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/aboutMe.json'
            
         }
         
      )
      

   def getText(self): return self.files[self.key]['text']
      

   def getPhoto(self): return self.files[self.key]['photo']
   
   
   def getEcosystem(self): return self.files[self.key]['ecosystem']