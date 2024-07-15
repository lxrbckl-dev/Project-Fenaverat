# import <
from github import Github
from lxrbckl.remote import (githubGet, requestsGet)

# >


class dataManager:
   
   
   def __init__(self):
      '''  '''
      
      self.useGithub = True
      self.token = ''
      
      self.github = Github(self.token)
   
   
   def fileGet(
      
      self, 
      link = None,
      file = None, 
      repo = None
      
   ):
      '''  '''
      
      if (self.useGithub):
      
         return githubGet(
            
            pFilename = file,
            pRepository = repo,
            pGithub = self.github
            
         )
         
      else: return requestsGet(link)
         
      