# import <
from github import Github
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class loadManager:
   

   def __init__(self, resources):
      '''  '''

      self.resourcePath = '/src/content'
      self.files = {
         
         self.getName(resource) : {
            
            'local' : self.loadLocal,
            'remote' : self.loadRemote
            
         }[loadType](resource)
         
      for loadType, resource in resources.items()}
      
   
   def loadRemote(self, resource): return requestsGet(resource)
   
   
   def getName(self, resource): return resource.split('/')[-1].replace('.json', '')
   
   
   def loadLocal(self, resource): return fileGet(f'{self.resourcePath}/{self.getName(resource)}.json')