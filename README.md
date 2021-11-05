# CSV Validator and Database Uploader
**Why**: MySQL classifies "NA" values as 0 in numerical fields, which messed up my data. [With a few hours experience, I can now confirm this is because the fields I was using were classified as `Float`, which cannot have a `NULL` value in MySQL. Fun!]

MySQL formatting aside, I wanted to make a tool that could validate my csv files line by line, let me know which ones had problems (missing fields or fields with mismatching types), and reformat "NA"s to None for ease of insertion into a default `NULL` column.

**How**: All values are precoded into the `constants.py` script, including:
+ DB_CONFIG: dictionary that holds login information to access the MySQL server, including user, password, host, and port
+ DB_NAME: name of the database you will be accessing at the host
+ TABLES: a dictionary where the key is the table name in the SQL database, and the value is a dictionary with the following keys:
  + `filepath`
  + `createcommand` (SQL syntax)
  + `columns` (SQL schema)
  + `columntypes`
+ NA_LIST : a list of possible null or unavailable values that may be encountered while parsing a csv file


Running `app.py` will call functions in `database.py` to open a connection to `DB_NAME` or create the database if it is not already initialized, and will create tables in `DB_NAME`, unless they are already initialized. `app.py` then calls functions inside `validation.py` which will parse the csv files line by line, checking for number of entries and types of entries against the expected schema specified in `constants.py`.
