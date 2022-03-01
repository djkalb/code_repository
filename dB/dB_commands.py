import sqlite3



# current project search refinement
""" 
Algorithm Table Elements:
    language:
    description:
    code:
    title:
    project:


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
    image

Cheatsheets:
    syntax definitions??
    descr:
    title:
    language:\
"""
with sqlite3.connect("code_repository_.db") as conn:
    c = conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS Algorithm_tbl(ID INTEGER PRIMARY KEY AUTOINCREMENT, descr TEXT, body TEXT, language TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Error_tbl(ID INTEGER PRIMARY KEY AUTOINCREMENT, descr TEXT, body TEXT, title TEXT, language TEXT,  attempts TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Layout_tbl(ID INTEGER PRIMARY KEY AUTOINCREMENT, descr TEXT, body TEXT, title TEXT, language TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Cheatsheet_tbl(ID INTEGER PRIMARY KEY AUTOINCREMENT, descr TEXT, body TEXT, title TEXT, language TEXT)""")
c.close()

''' 
# sample data -- small list will need to enlarge soonish
with sqlite3.connect("code_repository_.db") as conn:
    c = conn.cursor()
    c.execute("""INSERT INTO Algorithm_tbl (descr) VALUES 
        ('Divide and conquer algorithms  divide the problem into smaller subproblems of the same type; solve those smaller problems, and combine those solutions to solve the original problem.'),
        ('Randomized algorithms  use a random number at least once during the computation to find a solution to the problem.'),
        ('Recursive algorithms  solve the lowest and simplest version of a problem to then solve increasingly larger versions of the problem until the solution to the original problem is found.'),
        ('Dynamic programming algorithms  break a complex problem into a collection of simpler subproblems, then solve each of those subproblems only once, storing their solution for future use instead of re-computing their solutions.'),
        ('Backtracking algorithms  divide the problem into subproblems, each which can be attempted to be solved; however, if the desired solution is not reached, move backwards in the problem until a path is found that moves it forward.'),
        ('Greedy algorithms  find an optimal solution at the local level with the intent of finding an optimal solution for the whole problem.');
        """)
    
    conn.commit()
c.close()
'''
with sqlite3.connect("code_repository_.db") as conn:
    c = conn.cursor()
    for row in c.execute('SELECT * FROM Algorithm_tbl'):
        print(row)
c.close()