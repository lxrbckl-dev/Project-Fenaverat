# import <
from .loadManager import loadManager

# >


class myServersManager(loadManager):
   

   def __init__(self):
      '''  '''

      self.data = 'nodeArchive'
      super().__init__(
         
         resources = {
            
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/myServers.json',
            'remote' : 'https://raw.githubusercontent.com/lxRbckl/Project-Acta-Mea/V6/resources/nodeArchive.json'
            
         }
         
      )
      
      
      print('myservers', self.files.keys()) # remove
      print('nodeArchive', self.files['myServers']) # remove
      
      
   def getServers(self): return self.files[self.data]