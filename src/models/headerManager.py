# import <
from .loadManager import loadManager

# >


class headerManager(loadManager):
   

   def __init__(self):
      '''  '''

      super().__init__(
         
         resources = {
            
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/header.json'
            
         }
         
      )
      
      
   def getTitle(self): return self.files['header']['title']
   
   
   def getImages(self): return self.files['header']['images']