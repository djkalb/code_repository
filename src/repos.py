#!/usr/bin/env python3
from models.addDb import add
import sys
from getopt import GetoptError, getopt


def main(argv):
    # if "add" in argv:
    #     print("???")
    # for item in argv:
    #     if item == "add":
    #         print(":)")
    #     print(item)

    # need to add check to make sure only one func is called at a time
    commands = {'add': add,
                'search': search,
                }
    if argv[0] in commands.keys():
        #calls matching command -> passes extra args to it
        commands[argv[0]](argv[1:])
    else:
        print("that command was not recognized")
    # for key in commands:
        
    #     if key in argv:
            
    #         print("here!")
    #         commands[key](argv[1:])
    #     else:
    #         print(":(")
    # print ('Number of arguments:', len(sys.argv), 'arguments.')
    # print ('Argument List:', str(sys.argv))   
    #

def search(lst):
    print("search works")
if __name__ == "__main__":
    main(sys.argv[1:])