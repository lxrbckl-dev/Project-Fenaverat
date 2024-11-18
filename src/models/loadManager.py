# import <
from os import getenv
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class loadManager:
   

   def __init__(self, key, resources):
      '''  '''

      self.key = key
      self._resourcePath = '/src/content'
      self._projName = getenv('PROJECT_NAME')
      self._githubEmail = getenv('GITHUB_EMAIL')
      self._githubToken = getenv('GITHUB_TOKEN')
      self._projVersion = getenv('PROJECT_VERSION')

      self.files = {
         
         r['id'] : {
            
            'local' : self.loadLocalResource,
            'remote' : self.loadRemoteResource
            
         }[r['load']](r['link'])
         
      for r in resources}
      
      
   def getIcon(self, icon): return self.files[self.key]['icons'][icon]
   
   
   def loadRemoteResource(self, resource): return requestsGet(
      
      pURL = resource, 
      pDisplayError = True,
      pHeaders = {
         
         'Authorization' : f'token {self._githubToken}',
         'User-Agent' : f'{self._projName}/{self._projVersion} ({self._githubEmail})'
         
      }
      
   )
      
   
   def loadLocalResource(self, resource): return fileGet(f'{self._resourcePath}/{self.key}.json')