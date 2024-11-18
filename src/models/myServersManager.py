# import <
from .loadManager import loadManager

# >


class myServersManager(loadManager):
   

   def __init__(self):
      '''  '''

      self.data = 'nodeArchive'
      super().__init__(
         
         key = 'myServers',
         resources = [
            
            {
               
               'load' : 'remote',
               'id' : 'nodeArchive',
               'link' : 'https://raw.githubusercontent.com/lxRbckl/Project-Acta-Mea/V6/resources/nodeArchive.json'
               
            },
            {
               
               'load' : 'local',
               'id' : 'myServers',
               'link' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/myServers.json'
               
            }
            
         ]
         
      )
      
      
   def getServers(self): return self.files[self.data]