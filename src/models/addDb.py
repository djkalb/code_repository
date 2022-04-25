
from . import models
import sys
from getopt import GetoptError, getopt
import pyperclip as pc


def add(argv):
    #instantiate model of type -- only allowing algorithm for now
    alg = models.Algorithm()
    code_body = ''
    try:
        opts, args = getopt(argv, ':td:hl:rv', ["language=", "descr="])
    except GetoptError:
        print("not a valid selection")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == "-h":
            print("""repos is a console app designed to add and search code algorithms and other helpful tools.
            accepted arguments are add, search, config, view, and -h for help which can be called for each method individually. 
            call repos search <search>, <language> etc. can only call one function at a time""")
            sys.exit()
        elif opt == "-t":
            code_body = pc.paste()
            alg.code_body = code_body
            print(code_body)
        elif opt in ('-l', '--language'):
            lang = arg
            alg.language = lang
        elif opt in ('-d', '--descr'):
            descr = arg
            alg.description = descr
        elif opt == "-r":

            print('-r will call the previous entry and use its info for any non specified arg')
        elif opt == "-v":
            print("will open a gui -- might just get rid of this option to keep lightweight")
    print(alg)
    try:
        with models.Session.begin() as sesh:
            sesh.add(alg)
            sesh.commit()
    except Exception as e:
        #print(e)
        
        print(dir(alg))



    
