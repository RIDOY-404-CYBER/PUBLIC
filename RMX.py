#!usr/bin/env python
# -*- coding:utf-8
#CODE BY RMX-XD
"""
CREATED By RMX, 27 January 2024
@AUTHOR: ADRIAN WAYNE RIDOY 
"""
##MAIN##
class RMX_XD:
   def __init__(self):
       self.update()
       self.models()
       self.main_()
 
   def update(self):
       import os
       os.system('git pull')
   
   def models(self):
      import os
      try:
        import pycurl,httpx
      except:
        os.system('pip install pycurl')
        os.system('pip install httpx')
         
   def main_(self):
       import os,platform
       self.rmx=platform.architecture()[0]
       if self.rmx=='64bit':
        print('\033[1;32m[•] Congrats! Your Device Support This Tools')
        #os.system('xdg-open https://facebook.com/groups/770617227293870/')
        import PUBLICX
       if self.rmx=='32bit':
        print('\033[1;32m[•] Congrats! Your Device Support This Tools')
        os.system('xdg-open https://facebook.com/groups/770617227293870/')
        import PUBLICX2
       else:print('\033[1;32m[•] Contract Admin For Help');exit()
  
RMX_XD()
##
