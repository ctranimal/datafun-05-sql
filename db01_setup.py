
#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Import local modules
from utils_logger import logger
import utils_project03

#####################################
# Declare Global Variables
#####################################


#####################################
# Define Functions
#####################################


#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting db01_setup ...")
    utils_project03.set_globalvars_for_data_folders_empty() # call this function to SET global vars FETCHED_DATA_DIR, PROCESSED_DIR
    logger.info(f"Global vars FETCHED_DATA_DIR: {utils_project03.FETCHED_DATA_DIR}")
    logger.info(f"Global vars PROCESSED_DIR: {utils_project03.PROCESSED_DIR}") 
    #process_json_file()
    logger.info("db01_setup complete.")