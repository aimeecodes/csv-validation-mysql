# list of constants to imported into appropriate function calls
# in databasesetup.py, validatecsv.py

DB_CONFIG = {"user": "aimee", "password": "temptemp", "host": "localhost", "port": 3336}

DB_NAME = "Berkeley"

# create dictionary where each value is a dictionary of values for the table
# key   -- table name in SQL database
# value -- dictionary with table's "filepath", "createcommand",
#          "columns", and "columntypes"
TABLES = {}
TABLES["stateStops"] = {}
TABLES["stateStops"]["filepath"] = "state.csv"
TABLES["stateStops"]["createcommand"] = (
    "create table `stateStops` ("
    "  `state`        varchar(20)  not null,"
    "  `city`         varchar(255) not null,"
    "  `geography`    varchar(255) not null,"
    "  `subgeography` varchar(255) not null,"
    "  `subject_race` varchar(20)  not null,"
    "  `search_rate`  double,"
    "  `stop_rate`    double,"
    "  `hit_rate`     double,"
    "  `inferred_threshold` double,"
    "  `stops_per_year` double,"
    "  `stop_rate_n`  double"
    ") ENGINE=InnoDB"
)
TABLES["stateStops"]["columns"] = [
    "state",
    "city",
    "geography",
    "subgeography",
    "subject_race",
    "search_rate",
    "stop_rate",
    "hit_rate",
    "inferred_threshold",
    "stops_per_year",
    "stop_rate_n",
]
TABLES["stateStops"]["columntypes"] = [
    str,
    str,
    str,
    str,
    str,
    float,
    float,
    float,
    float,
    float,
    float,
]
################################################################################
TABLES["cityStops"] = {}
TABLES["cityStops"]["filepath"] = "opp-stops_city.csv"
TABLES["cityStops"]["createcommand"] = (
    "create table `cityStops` ("
    "  `city`         varchar(20)  not null,"
    "  `state`        varchar(255) not null,"
    "  `geography`    varchar(255) not null,"
    "  `subgeography` varchar(255) not null,"
    "  `subject_race` varchar(20)  not null,"
    "  `search_rate`  double,"
    "  `stop_rate`    double,"
    "  `hit_rate`     double,"
    "  `inferred_threshold` double,"
    "  `stops_per_year` double,"
    "  `stop_rate_n`  double"
    ") ENGINE=InnoDB"
)
TABLES["cityStops"]["columns"] = [
    "city",
    "state",
    "geography",
    "subgeography",
    "subject_race",
    "search_rate",
    "stop_rate",
    "hit_rate",
    "inferred_threshold",
    "stops_per_year",
    "stop_rate_n",
]
TABLES["cityStops"]["columntypes"] = [
    str,
    str,
    str,
    str,
    str,
    float,
    float,
    float,
    float,
    float,
    float,
]
################################################################################
TABLES["mjSearches"] = {}
TABLES["mjSearches"]["filepath"] = "opp-search-marijuana_state.csv"
TABLES["mjSearches"]["createcommand"] = (
    "create table `mjSearches` ("
    "  `state`       varchar(20) not null,"
    "  `driver_race` varchar(20) not null,"
    "  `pre_legalization` boolean not null,"
    "  `quarter` double,"
    "  `search_rate` double"
    ") ENGINE=InnoDB"
)
TABLES["mjSearches"]["columns"] = [
    "state",
    "driver_race",
    "pre_legalization",
    "quarter",
    "search_rate",
]
TABLES["mjSearches"]["columntypes"] = [str, str, bool, "date", float]

# define a list of NA values as strings that may be encountered
# when parsing a csv file
NA_LIST = ["na", "n a", "n/a", "nan"]

# create dictionary of table columns and types where
# key      -- table name
#
# # create FILEPATHS dictionary where
# # key   -- table name in SQL database
# # value -- string of filepath location
# FILEPATHS = {}
# FILEPATHS["stateStops"] = "state.csv"
# FILEPATHS["cityStops"]  = "opp-stops_city.csv"
# FILEPATHS["mjSearches"] = "opp-search-marijuana_state.csv"
