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
   
   
   def fileGet(
      
      self, 
      link = None,
      file = None, 
      repo = None
      
   ):
      '''  '''
      
      if (self.loadType == 'local'):
      
         fileGet(pFile = '{}'.format())
         
      else: return requestsGet(link)
         
      