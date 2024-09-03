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
   
   
   def getCardIconOS(self, os): 
      
      try: return self.files['myServers']['iconsOS'][os]
      except KeyError: return None
   
   
   def getCardIconHost(self, host): 
      
      try: return self.files['myServers']['iconsHost'][host]
      except KeyError: return None
      
      
   def getCardIconHardware(self, hardware):
      '''  '''
      
      try: return self.files['myServers']['iconsHardware'][hardware]
      except KeyError: return None