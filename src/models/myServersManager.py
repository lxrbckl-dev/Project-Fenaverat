# import <
from sys import stderr # check
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
      
      
   def getServers(self): 
      
      stderr.write('HERE')
      return self.files[self.data]