import sqlite3
# -- version 1.0 add will just read a txt file for func itself user input for everything else 
# -- uses current

# early version will hardcode dB info
# copy and add are almost the same so it will use the same function                           // except the actual add / copy part
def addToDb (table):
    

    language = input('Which language is it written in? ')
    descr = input('give a brief description: ')
    body = ""
    
    with open('add.txt', 'w+') as file:
        
        for line in file:
            body += line
        file.write("\n")
    
    data = (descr, body, language)
    with sqlite3.connect('code_repository_.db') as conn:
        c = conn.cursor()
        sqlite_insert_with_param = """INSERT INTO {}
                          (descr, body, language) 
                          VALUES (?, ?, ?);""".format(table)
        c.execute(sqlite_insert_with_param, data)
        
        conn.commit()
    c.close()

 
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