import csv
import mysql.connector
from mysql.connector import errorcode
from validation import *
from constants import *


def create_tables(cursor, tables):
    """
    Accepts a cursor and table dictionary that holds SQL create commands

    keyword arguments:
    cursor -- created in app.py, connection to database
    tables -- defined in constants.py, SQL create commands to be executed
    """
    for tab in tables:
        tab_desc = tables[tab]["createcommand"]
        try:
            print("Creating table {}: ".format(tab), end="")
            cursor.execute(tab_desc)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("{} already exists.".format(tab))
            else:
                print(err.msg)

        else:
            print("OK")


def create_database(cursor, DB_NAME):
    """
    Accepts a cursor and database name to be created

    keyword arguments:
    cursor  -- created in app.py, connection to database
    DB_NAME -- defined in constants.py, database name
    """
    try:
        cursor.execute(
            "create database {} default character set 'utf8'".format(DB_NAME)
        )
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def use_database(cursor, DB_NAME):
    """
    Accepts a cursor and database name to either be used, or then created

    keyword arguments:
    cursor  -- created in app.py, connection to database
    DB_NAME -- defined in constants.py, database name
    """
    try:
        cursor.execute("use {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exist.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)


def lbl_insert(cursor, tables):
    """
    Accepts a cursor, and dictionary of tables;
    reads the csv file at csvfilepath line by line (lbl),
    checks each line to make sure it conforms to defined table schema,
    creates a list of insert commands

    keyword arguments:
    cursor       -- created in app.py, connection to database
    tables       -- defined in constants.py, called from app.py,
                    contains dictionary of tables, where each
                    value is a dictionary with keys: "filepath",
                    "createcommand", "columns", "columntypes"
    """
    # loop over tables to insert
    for tab in tables:
        cols = tables[tab]["columns"]
        coltypes = tables[tab]["columntypes"]
        path = tables[tab]["filepath"]

        valid_records = []
        invalid_records = []

        with open(path) as csvfile:
            # skip first line headers
            next(csvfile)

            csvreader = csv.reader(csvfile)
            for record in csvreader:
                if validate_record(record, coltypes):
                    # reformat any NA fields
                    record = reformat_NA(record)

                    # reformat boolean fields
                    record = reformat_bool(record, coltypes)

                    # create SQL insertion statement
                    sql_statement = make_insert(tab, tables[tab]["columns"], record)
                    # execute the insert statement
                    cursor.execute(sql_statement, record)
                else:
                    invalid_records.append(record)

        if len(invalid_records) > 0:
            print(
                "{} rows failed to insert into table {}".format(
                    len(invalid_records), tab
                )
            )
        else:
            print("All rows inserted into {} successfully.".format(tab))


def make_insert(tablename, columns, record):
    """
    Accepts a table name, schema, and record;
    creates a SQL INSERT

    keyword arguments:
    tablename -- name of the table to be inserted into
    schema    -- list of columns in the schema of table
    record    -- list of values to be inserted to table
    """
    query_placeholders = ", ".join(["%s"] * len(columns))
    query_columns = ", ".join(columns)
    insert_sql = """INSERT INTO %s (%s) VALUES (%s)""" % (
        tablename,
        query_columns,
        query_placeholders,
    )
    return insert_sql
