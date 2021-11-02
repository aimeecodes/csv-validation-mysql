# CSV Validator and Database Uploader
**Why**: MySQL classifies "NA" values as 0 in numerical fields, which messed up my data. I wanted a tool that could validate my csv files line by line, let me know which ones had problems (missing fields or fields with mismatching types), and rewrite "NA" values to the expected MySQL NULL. 

**How**: In the `constants.py` script, 
