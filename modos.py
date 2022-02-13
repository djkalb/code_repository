from importlib.metadata import files
import os
from os.path import join
import subprocess

#
"""
logic function calls other funcs based on commands given to it
 choice = input('What would you like to do? ')
"""




root = "c:\A"
def fileFinder(path):
    

    for (_, dirs, files) in os.walk(path, topdown=True):

        list = dirs + files
        newKeys = range(len(list))
        
        test = { k:v for (k,v) in zip(newKeys, list)}
        print(test)
        choice = int(input('pick a folder or file: '))
        
        if choice in test:
            choice = test[choice]
            print(choice)
            
            
            
            path = join(path, choice)
            print( path)
            
            if '.' in choice:
                print("start "+ path)
                return subprocess.Popen("start "+ path, shell=True)
            
                
        
        fileFinder(path)
    

def brains():
    commands = {
            #'back': 'what'#fileFinder(root),
            #'file': fileFinder(path, fileFinder(path, 'file')),
            'open1': os.system("start "+"components.txt")
        }



fileFinder(root)


    





   
   
