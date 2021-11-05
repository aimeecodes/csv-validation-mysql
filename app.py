from constants import *
from database import *

if __name__ == "__main__":
    with mysql.connector.connect(**DB_CONFIG) as cnx:
        with cnx.cursor() as cursor:
            # initialize or use database
            use_database(cursor, DB_NAME)

            # create tables using dictionary
            create_tables(cursor, TABLES)

            # validate and insert csv files
            # to tables line by line
            lbl_insert(cursor, TABLES)
