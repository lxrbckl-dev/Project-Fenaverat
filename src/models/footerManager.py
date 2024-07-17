# import <
from .resourceManager import resourceManager

# >


class footerManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'footer',
         loadType = 'local'
         
      )
      
      self.content = super().fetchContent()
      
      
   def getConnections(self): return self.content['connections']