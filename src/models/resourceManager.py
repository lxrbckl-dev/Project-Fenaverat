# import <
from github import Github
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class resourceManager:
   
   
   def __init__(
      
      self,
      file,
      loadType
      
   ):
      '''  '''
      
      self.file = file
      self.loadType = loadType
      self.contentPath = '/src/content/'
      self.urls = {
         
         'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/header.json',
         
         'aboutMe' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/aboutMe.json',
         'myServers' : 'https://raw.githubusercontent.com/lxRbckl/Project-Acta-Mea/V6/resources/nodeArchive.json',
         'myProjects' : 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/V2/data/repositoryArchive.json',
         
         'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/footer.json'
         
      }

   
   def fetchContent(self):
      '''  '''
         
      return {
         
         'remote' : lambda : requestsGet(self.urls[self.file]),
         'local' : lambda : fileGet('{}{}.json'.format(self.contentPath, self.file))
         
      }[self.loadType]()
      
      
   def fetchExternalContent(self):
      '''  '''
      
      pass