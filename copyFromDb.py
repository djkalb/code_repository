import sqlite3
# -- version 1.0 add will just read a txt file for func itself user input for everything else 
# -- uses current

# early version will hardcode dB info
# copy and add are almost the same so it will use the same function                           // except the actual add / copy part
def copyFromDb(table, pk):
    
    with sqlite3.connect('code_repository_.db') as conn:
        c = conn.cursor()
        get_body_tbl = """SELECT body FROM {} WHERE ID == {}""".format(table, pk)
        c.execute(get_body_tbl)
        body = c.fetchone()
        with open('copy.txt', 'a') as txt:
                       
            print(body[0], file=txt)
    c.close()
    print('copy was successful')
    
           
    
    
    
    


""" 
Algorithm Table Elements:
    language:
    description:
    code:
    title:


Error Table Elements:
    Descr:
    Title:
    Problem:
    Language:
    working solution:


Layouts Table Elements:
    Language:
    descr:
    code:

Cheatsheets:
    syntax definitions??
    descr:
    title:
    language:
"""