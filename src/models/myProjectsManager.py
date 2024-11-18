# import <
from random import shuffle

from .loadManager import loadManager

# >


class myProjectsManager(loadManager):
   
   
   def __init__(self):
      '''  '''

      self.data = 'repositoryArchive'
      super().__init__(
         
         key = 'myProjects',
         resources = [
            
            {
               
               'load' : 'remote',
               'id' : 'repositoryArchive',
               'link' : 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/V2/data/repositoryArchive.json'
               
            },
            {
               
               'load' : 'local',
               'id' : 'myProjects',
               'link' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/myProjects.json'
               
            }
            
         ]
         
      )
      
      
   def getProjects(self): 
      
      projects = self.files[self.data]
      keys = list(projects.keys())
      shuffle(keys)
      
      return {k : projects[k] for k in keys}
   
   
   def getCardBackground(self, project):
      '''  '''
      
      try: return self.files[self.key]['projectCardBackgrounds'][project]
      except KeyError: return None