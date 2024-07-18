# import <
from .resourceManager import resourceManager

# >


class myServersManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'myServers',
         loadType = 'remote'
         
      )
      
      self.content = super().fetchContent()