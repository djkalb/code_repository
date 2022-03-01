import os
import sqlite3

"""
takes in a file line if copying from file needs end line number
if copy from dB reads lines inserts txt from source
returns success or failure?
if add copies lines from file returns copied lines

"""
def lineFinder(targetFile, command, startLine, endLine=0):
    with open(targetFile, 'w+'):
        endOfFile = len(targetFile)
        txt = ""
        for line in targetFile:
            if startLine < line < endLine or endOfFile:
                txt += line
            else: 
                pass
        
    
def accessDb(command):
    with sqlite3.connect('code_repository_.db') as conn:
        c = conn.cursor()
        sqlite_insert_with_param = """INSERT INTO {}
                          (descr, body, language) 
                          VALUES (?, ?, ?);""".format(table)
        c.execute(sqlite_insert_with_param, data)
        
        conn.commit()
    c.close()

print()