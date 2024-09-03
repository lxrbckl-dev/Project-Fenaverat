# import <
from random import shuffle

from .loadManager import loadManager

# >


class myProjectsManager(loadManager):
   
   
   def __init__(self):
      '''  '''

      super().__init__(
         
         resources = {
            
            'remote' : 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/V2/data/repositoryArchive.json',
            'local' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/V4/src/content/myProjects.json'
            
         }
         
      )
      
      
   def getProjects(self): 
      
      projects = self.files['repositoryArchive']
      keys = list(projects.keys())
      shuffle(keys)
      
      return {k : projects[k] for k in keys}
   
   
   def getCardBackground(self, project):
      '''  '''
      
      try: return self.files['myProjects']['projectCardBackgrounds'][project]
      except KeyError: return None
   
   
   def getCardIcon(self, icon): return self.files['myProjects']['icons'][icon]