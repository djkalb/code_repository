from importlib.metadata import files
import os
from os.path import join
from ssl import Options
import subprocess

#
"""
uses recursion to navigate through a dictionary of items presenting user with 
the child nodes at every level

dict will be attached to table eventually

back command will be seperate, and so will search 
seearch will query the dB, with an additional argument of what file they want to open from the list
along with a basic description of the function they want to find
if arg is given from directory search will move through entire table list searching for blank

the root directory will be configured on first run by RUN() --not configged for testing purposes 
the dictionary will also be passed in by run -- not for test though
"""


tableDict = {
    'bad': {
        'test': {
            'nests': {
                'info': "this is not the info you were looking for"
            },
            '2nest': {
                'ninfo': 'i am what you want'
            }
        },
        'see_me?': "i got what you need"
    },
    'good': {
        'names': {
            'are': {
                'very': {
                    'hard': 'found me'
                }
            }
        },
        'confused?':{
            'ans': 'this is kindof alot to deal with'
        }
    }

}

#catch attempt to open unnested table???
#0def search(test, state):
    #for item in state:

        #print(item)



    
def fileFinder(Tdict, state):
    
    lst = [ key for key in Tdict]
    #print(lst)
    
    newKeys = range(len(lst))
    options = { k:v for (k,v) in zip(newKeys, lst)}
    print(options)
    choice = int(input('pick a folder or file: '))
    print(state)
    #print(choice)
    if choice in options and isinstance(Tdict[options[choice]], dict):
        #print(Tdict[options[choice]])
        state.append(options[choice])
        fileFinder(Tdict[options[choice]], state)
            #print(choice)
    else:
        words = input('would you like to search this file?(y/n)'  )
        if words == 'y':
            
            print(fileFinder.__annotations__)
            search(Tdict[options[choice]], state)
    
        
        
        
            
lst = []   
fileFinder(tableDict, lst)   









   
   

    





   
   
