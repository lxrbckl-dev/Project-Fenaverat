# import <
from .resourceManager import resourceManager

# >


class aboutMeManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'aboutMe',
         loadType = 'local'
         
      )
      
      self.content = super().fetchContent()
      
      
   def getText(self): return self.content['text']
      

   def getPhoto(self): return self.content['photo']
   
   
   def getEcosystem(self): return self.content['ecosystem']