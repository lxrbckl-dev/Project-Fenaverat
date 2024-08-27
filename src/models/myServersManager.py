# import <
from .resourceManager import resourceManager

# >


class myServersManager(resourceManager):
   
   
   def __init__(self):
      '''  '''
      
      super().__init__(
         
         file = 'myServers',
         loadType = 'remote'
         
      )
      
      self.content = super().fetchContent()
      
      
   def getServers(self):
      '''  '''
      
      server = []
      
      return server
      
      
   # def getServers(self):
   #    '''  '''
      
   #    servers = []
      
   #    # iterate (host, swarm) <
   #    for kind in (self.content).keys():
         
   #       # iterate (host, swarm)->node <
   #       for sid, svals in self.content[kind].items():
            
   #          servers.append({
               
   #             'kind' : kind,
   #             ''
   #             'services' : svals['service'],
   #             'name' : sid if (kind == 'host') else svals['hostname'],
   #             'status' : True if (kind == 'host') else svals['status']
               
   #          })
            
   #       # >
         
   #    # >
            
   #    return servers