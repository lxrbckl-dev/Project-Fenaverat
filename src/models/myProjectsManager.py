# import <
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
      
      
   def getProjects(self): return self.files['myProjects']
   
   
   def getProjectBackground(self, project):
      '''  '''
      
      try: return self.files['myProjects']['projectCardBackgrounds'][project]
      except KeyError: return None