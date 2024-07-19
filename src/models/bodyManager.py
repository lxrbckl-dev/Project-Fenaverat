# import <
from .resourceManager import resourceManager

# >


class bodyManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'body',
         loadType = 'local'
         
      )
      
      self.content = super().fetchContent()
      
   
   def getBadgeBackgroundColors(self): return self.content['badgeBackgroundColors']
   
   
   def getBadgeTextColor(self): return self.content['badgeTextColor']