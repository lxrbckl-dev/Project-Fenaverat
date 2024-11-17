# import <
from github import Github
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class loadManager:
   

   def __init__(self, resources):
      '''  '''

      self.localResourceName = None
      self.resourcePath = '/src/content'
      self.files = {
         
         self.getResourceName(resource) : {
            
            'local' : self.loadLocalResource,
            'remote' : self.loadRemoteResource
            
         }[loadType](resource)
         
      for loadType, resource in resources.items()}
            
   
   def loadRemoteResource(self, resource): return requestsGet(resource, pShowError = True)
   
   
   def getIcon(self, icon): return self.files[self.localResourceName]['icons'][icon]
   
   
   def getResourceName(self, resource): 
      
      print(resource.split('/')[-1].replace('.json', '')) # remove

      return resource.split('/')[-1].replace('.json', '')
   
   
   def loadLocalResource(self, resource): 
      
      self.localResourceName = self.getResourceName(resource)
      
      return fileGet(f'{self.resourcePath}/{self.localResourceName}.json')