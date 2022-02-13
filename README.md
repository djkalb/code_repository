# code_repository
program to store and search code snippets / cheatsheets / error logs

simplest version --- completed

-- run module from python in cmd choose from lst of text files open selected file 
-- uses inputs to interact (y/n)super simple 

version 1.0 -- almost completed 

-- query tables by descr. open selected results in a txt file  DONE
-- refine search using a nested dictionary use results to query more selectively DONE
-- run() saves a record of state permitting users to go back , and continue from last spot on rerun -- moved into version 2.0
-- add will read from txt file and place into dB  DONE

 version 2.0 will

-- allow users to copy or add into selected file in cwd at chosen line no -- the db does keep the formatting provided you print it
-- run saves state permitting users to go back
-- file explorer in cwd // configurable cwd
-- search allows refinements to search ie table / language / project / any column in dB
-- link the dB's together through clustered index -- so searches can refine 
-- search will return list of top 5 // if all results are 0 will ask to search again with different phrasing for new 
-- run will be able to nav through those choices with a next and back function
-- use dict as representative structure of tables // allow users to create modify their own datastructure
at every depth of structure option to create that layer ie at language layer add language
option to base it off other data structure??? or add own optional configs
only primary key every item entry will require descr table structure is optional descr configs
-- delete option ask confirmation then delete will also be performable at level of current depth|| cannot be undone
-- include basic tablelist already made // allow columns to be added / modified or creation of own 
