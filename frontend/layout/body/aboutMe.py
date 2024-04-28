# import <
from dash import dcc, html
from dash_player import DashPlayer
import dash_bootstrap_components as dbc

# >


class aboutMe:
   
   def __init__(self):
      '''  '''
      
      self.id = 'b1'  
      self.waitVideo = 2
      self.maxHeight = 512
      self.file = 'aboutMe'
      self.title = 'about me'
   
   
   def badge(
      
      self,
      pStyle,
      pIterable,
      
      pKey = 'badge',
      pFile = 'aboutMe',
      isService = False
      
   ):
      '''  '''

      return [
                     
         dbc.Badge(
            
            color = None,
            text_color = None,
            children = i.replace('-', ' ') if (i) else None,
            style = {
               
               **pStyle[pFile][pKey]['badge'],
               'color' : pStyle['framework']['colorBlack'],
               'background' : pStyle['framework']['badgeColors'][k],
               **pStyle[pFile][pKey]['type'][{
                  
                  False : 'other',
                  True : 'service'
                  
               }[isService]]
               
            }
            
         )
         
      for k, v in pIterable.items() for i in v]
         
   
   def board(
      
      self,
      pData,
      pStyle,
      pContent,
      
      pKey = 'board'
   
   ):
      '''  '''

      return html.Div(
         
         style = {
            
            **pStyle[self.file][pKey]['div'],
            'backgroundImage' : pContent[self.file]['background']

            
         },
         children = [
            
            # (profile, bio) <
            # ecosystem <
            dbc.Row(
               
               style = {
                  
                  'borderTop' : pStyle['framework']['borderBlack'],
                  'borderLeft' : pStyle['framework']['borderBlack'],
                  'borderRight' : pStyle['framework']['borderBlack']
                  
               },
               children = [
                  
                  dbc.Col(
                     
                     width = 4,
                     style = pStyle[self.file][pKey]['profileCol'],
                     children = DashPlayer(
                        
                        muted = True,
                        width = '100%',
                        height = '100%',
                        playing = False,
                        controls = False,
                        id = 'profileVideoId',
                        url = pContent[self.file]['profileVideo'],
                        
                        style = {'padding' : '0 0 0 0', 'margin' : '0px 0 -6px 0'}
                        
                     )
                     
                  ),
                  dbc.Col(
                     
                     width = 8,
                     style = {

                        **pStyle[self.file][pKey]['titleBioCol'],
                        'borderLeft' : pStyle['framework']['borderBlack'],
                        'backdropFilter' : pStyle['framework']['backdropFilter']
                        
                     },
                     children = [
                        
                        html.H1(
                           
                           children = pContent[self.file]['title'],
                           style = {

                              **pStyle[self.file][pKey]['titleH1'],
                              'color' : pStyle['framework']['colorBlack']
                              
                           }
                           
                        ),
                        html.Div(
                           
                           style = pStyle[self.file][pKey]['bioDiv'],
                           children = [
                              
                              dcc.Markdown(
                                 
                                 children = i,
                                 style = {
                                    
                                    'color' : pStyle['framework']['colorBlack'],
                                    **pStyle[self.file][pKey]['contentMarkdown']
                                    
                                 }
                                 
                              )
                              
                           for i in pContent[self.file]['content']]
                           
                        )
                        
                     ]
                     
                  )
                                    
               ]
               
            ),
            dbc.Row(
               
               style = {
                  
                  **pStyle[self.file][pKey]['ecosystemRow'],       
                  'border' : pStyle['framework']['borderBlack']
                                    
               },
               children = self.badge(
                  
                  pStyle = pStyle,
                  pIterable = pContent[self.file]['ecosystem']
                  
               )
               
            )
            
            # >
                        
         ]
         
      )