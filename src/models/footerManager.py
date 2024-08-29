# import <
from .loadManager import loadManager

# >


class footerManager(loadManager):


   def __init__(self):
      '''  '''

      super().__init__(
         
         resources = {
            
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/footer.json'
            
         }
         
      )

      
   def getConnections(self): return self.files['footer']['connections']