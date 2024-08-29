# import <
from .loadManager import loadManager

# >


class aboutMeManager(loadManager):
   

   def __init__(self):
      '''  '''

      super().__init__(
         
         resources = {
            
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/aboutMe.json'
            
         }
         
      )
      

   def getText(self): return self.files['aboutMe']['text']
      

   def getPhoto(self): return self.files['aboutMe']['photo']
   
   
   def getEcosystem(self): return self.files['aboutMe']['ecosystem']