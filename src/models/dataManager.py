# import <
from github import Github
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class dataManager:
   
   
   def __init__(self):
      '''  '''
      
      self.loadType = 'local'
      self.contentPath = '/src/content'
   
   
   def fetch(self, url = None, file = None):
      '''  '''
         
      return {
         
         'remote' : lambda : requestsGet(url),
         'local' : lambda : fileGet('{}{}'.format(
            
            self.contentPath,
            file
            
         ))
         
      }[self.loadType]()