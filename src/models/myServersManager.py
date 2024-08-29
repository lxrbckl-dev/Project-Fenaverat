# import <
from .loadManager import loadManager

# >


class myServersManager(loadManager):
   

   def __init__(self):
      '''  '''

      super().__init__(
         
         resources = {
            
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/myServers.json',
            'remote' : 'https://raw.githubusercontent.com/lxRbckl/Project-Acta-Mea/V6/resources/nodeArchive.json'
            
         }
         
      )
      
      
   def getServers(self): return self.files['nodeArchive']
   
   
   def getBadgeOS(self, os): return self.files['myServers']['badgesOS'][os]
   
   
   def getBadgeHost(self, host): return self.files['myServers']['badgesHost'][host]