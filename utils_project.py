"""

File: utils_project.py

This script provides some basic upkeeping utilities for project 03
Example: All files handling common to several tran_process_*.py are moved here.

"""

# Imports from Python Standard Library
import pathlib
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

# Moved these 2 variables to util_project03.py
ROOT_DIR: str = ""
SQL_SCRIPT_FOLDER: str = ""
DATA_FOLDER: str = ""
DATABASE_FOLDER: str = ""
DB_PATH: str = ""

#####################################
# Define Functions
#####################################

# return False if the strings are empty
# this is to ensure that the global variables are set only if they were empty
def are_globalvars_for_project_folders_empty() -> bool:
    #logger.info(" * are_globalvars_for_data_folders_empty() is called")
    if(ROOT_DIR == ""): return True
    if(DATABASE_FOLDER == ""): return True

    #if code reaching here, return default as False
    return False

#set these variables to set variables for project folders
# input parameter: call with either sql_create, sql_features or sql_queries
def set_globalvars_for_project_folders(sql_script_folder:str) -> None:
    # declare these as global, in order to SET global variables
    global ROOT_DIR
    global SQL_SCRIPT_FOLDER
    global DATA_FOLDER
    global DATABASE_FOLDER
    global DB_PATH

    logger.info(f" * set_globalvars_for_project_folders() is called, sql_script_folder={sql_script_folder}")

    if(are_globalvars_for_project_folders_empty()):
        ROOT_DIR = pathlib.Path(__file__).parent.resolve()
        DATA_FOLDER = ROOT_DIR.joinpath("data")
        DATABASE_FOLDER = ROOT_DIR.joinpath("database")
        DB_PATH = DATABASE_FOLDER.joinpath('tran_project05_database.db')          

    SQL_SCRIPT_FOLDER = ROOT_DIR.joinpath(sql_script_folder)

