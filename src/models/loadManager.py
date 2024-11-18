# import <
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class loadManager:
   

   def __init__(self, key, resources):
      '''  '''

      self.key = key
      self.resourcePath = '/src/content'
      self.files = {
         
         r['id'] : {
            
            'local' : self.loadLocalResource,
            'remote' : self.loadRemoteResource
            
         }[r['load']](r['link'])
         
      for r in resources}
      
      
   def getIcon(self, icon): return self.files[self.key]['icons'][icon]
   
   
   def loadRemoteResource(self, resource): return requestsGet(resource, pDisplayError = True)
      
   
   def loadLocalResource(self, resource): return fileGet(f'{self.resourcePath}/{self.key}.json')