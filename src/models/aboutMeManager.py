# import <
from .resourceManager import resourceManager

# >


class aboutMeManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'aboutMe',
         loadType = 'remote'
         
      )
      
      self.content = super().fetchContent()
      
      
   def getTitle(self): return self.content['title']


   def getPhoto(self): return self.content['photo']
   
   
   def getEcosystem(self): return self.content['ecosystem']
   
   
   def getDescription(self): return self.content['description']