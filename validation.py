import datetime
from constants import *


def validate_record(record, columntypes):
    """
    Accepts a list of expected fields and types,
    and a list containing a record (instance, row, line, etc.),
    then runs a length check and type check

    keyword arguments:
    columntypes -- list of column types
    record      -- list of line from csv file, split on delimiter
    """
    # set returned boolean to True by default
    valid_record = True

    # compare length of expected fields with length of record
    if len(record) != len(columntypes):
        valid_record = False
        return valid_record

    # compare the types of each attribute in the record to the
    # types of each expected_field
    valid_record = check_types(record, columntypes)

    # return final boolean
    return valid_record


def check_types(values, columntypes):
    """
    Checks the values against column types using safe_cast
    Returns True if all values pass type check
    Returns False if one value does not pass type check

    keyword arguments:
    columntypes -- list of column types
    values      -- list of an instance's values
    """
    for value, ctype in zip(values, columntypes):
        if value.lower() in NA_LIST:
            # skip type checking this value
            # ADD NA OVERWRITE FUNCTION HERE
            # to change the NA to proper mysql syntax
            continue

        # check if columntype is date, if yes, pass to
        # date handler
        if ctype == "date":
            result = parse_date(value)
            if result:
                continue
            else:
                return False

        # see if value can be cast to ctype
        if safe_cast(value, ctype) == None:
            print("{} cannot be typed as {}".format(value, ctype))
            return False

    # only get here if all values pass type check
    return True


def parse_date(value):
    """
    Accepts a possible date object, returns True if the value
    is considered a datetime object.
    """
    try:
        year, month, day = value.split("-")
    except:
        print("{} is not a valid date.")
        return False

    try:
        datetime.datetime(int(year), int(month), int(day))
    except:
        print("{} is not a valid date.")
        return False

    return True


def safe_cast(value, casttype, default=None):
    """
    Attemps to cast value as casttype, otherwise returns None

    keyword arguments:
    value    -- value to be cast
    casttype -- desired type of value
    default  -- returned value if unable to cast value to casttype
    """
    try:
        return casttype(value)
    except (ValueError, TypeError):
        return default

def reformat_NA(record):
    """
    Accepts a record in list form, where each item is a field;
    Passes over the list, and reformats any NA values to "\\N"
    """
    for i, field in enumerate(record):
        if field.lower() in NA_LIST:
            record[i] = None
    return record

def reformat_bool(record, columntypes):
    """
    Accepts a record in list form, where each item is a field;
    Passes over the list, and reformats string "True" and "False"
    to their Bool equivalent
    """
    for i, field  in enumerate(record):
        if columntypes[i] == bool:
            record[i] = safe_cast(field, bool)
    return record
