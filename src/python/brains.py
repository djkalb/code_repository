from addToDb import addToDb
from copyFromDb import copyFromDb
from searchDb import searcher

"""
uses a dictionary of functions calls corresponding function based on UI
keeps track of state // version 1.0 just uses search | add | copy | 
run needs to configure CWD 
"""
#-- run() saves a record of state permitting users to go back , and continue from last spot on rerun
def run():
    commands = {
        1: 'Add to dB',
        2: 'Copy from dB',
        3: 'Search dB'
    }
    print(commands)
    
    choice = int(input('What would you like to do? '))
    tables = {1: 'Algorithm_tbl', 2: 'Error_tbl', 3: 'Layout_tbl', 4: 'Cheatsheet_tbl'}
    print(tables)
    selection = int(input('which table would you like to use? ')) 
    table = tables[selection]
    result = 13
    
    funcs = {
        1: addToDb,
        2: copyFromDb,
        3: searcher
    }
    if choice == 3:
        result = funcs[choice](table)
        print(result)
        copyFromDb(table, result)
    if choice == 2:
        searcher(table)
        print(searcher.__annotations__)
    if choice == 1:
        addToDb(table)
    
run()