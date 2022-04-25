
import sqlite3

"""
query descriptions from all tables in dB for now -- later will add search refinements
clean list of descriptions and search 
compare list of descriptions to search
open result in new text file
later will need to add a basic thesaurus expansion for some of the search terms
     // ie algorithm - method - function would all work
ask user if result matches // else print next most accurate response


"""
def searcher(table):
    search = input('please describe what you are looking for: ')
    lstDescriptions = []
    with sqlite3.connect("code_repository_.db") as conn:
        c = conn.cursor()
        for row in c.execute('SELECT descr, ID FROM {}'.format(table)):
            lstDescriptions.append(row)
    c.close()

    #searchList = [string for string in lstDescriptions]
    #need to create a list of the queries to input into comparison Func 
    #then use returned list to grab the associated ID for the highest value
    #fewest iterations possible, but as many as necessary to get it working at first // refactor after it fucking works

    # -- func creates two lists of equal size one descr one is keys // searches keys / uses comparison 

    searchString, primaryKeys =  map(list,zip(*lstDescriptions))
    searchString.insert(0, search)


    comparisonResults = cos_sim_results(searchString)
    bestResult = comparisonResults.index(max(comparisonResults))
    resultKey = primaryKeys[bestResult]
    return resultKey
def testing():
    print("testing is going well")


























"""
with open("components.txt", 'r') as f:
    
    contents = [line for line in f]
    copy = contents[:]


with open("txt.txt", "w") as f:
    for line in copy:

        contents.insert(0, "copy")
print(contents)
contents = "".join(contents)
f.write(contents)

lines = ['searchable list of language folders\n', '\n', '- list of txt files containing different code or cheatsheets\n', '- search txt files for description of code\n', '- identify search matches present to user\n', '- copy into file automatically at specified line number?\n', '- select txt from current file and append it into local repository\n', '\n', '\n', 'simplest version\n', '\n', '-- run module from python in cmd choose from lst of text files open selected file \n', '-- uses inputs to interact (y/n)super simple ']

formatted = filter(lambda line: line != '\n', lines)
for i in formatted:
    print(i, file=open("searchAlgorithm.py", "a"), end="")

"""
    
    
    



    

