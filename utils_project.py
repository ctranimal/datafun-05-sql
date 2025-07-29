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
FETCHED_DATA_DIR: str = ""
PROCESSED_DIR: str = ""

#####################################
# Define Functions
#####################################

# return False if the strings are empty
# this is to ensure that the global variables are set only if they were empty
def are_globalvars_for_data_folders_empty() -> bool:
    #logger.info(" * are_globalvars_for_data_folders_empty() is called")
    if(FETCHED_DATA_DIR == ""): return True
    if(PROCESSED_DIR == ""): return True

    #if code reaching here, return default as False
    return False

#set these variables just once
def set_globalvars_for_data_folders_empty() -> None:
    # declare these as global, in order to SET global variables
    global FETCHED_DATA_DIR
    global PROCESSED_DIR

    logger.info(" * set_globalvars_for_data_folders_empty() is called")
    if(are_globalvars_for_data_folders_empty()):
        FETCHED_DATA_DIR = "example_data"
        PROCESSED_DIR = "tran_processed"
        #logger.info(f"after setting: Global vars FETCHED_DATA_DIR: {FETCHED_DATA_DIR}")
        #logger.info(f"after setting: Global vars PROCESSED_DIR: {PROCESSED_DIR}")          

