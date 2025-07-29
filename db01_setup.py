
#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys
import sqlite3
import os

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

    current_directory = os.getcwd()
    subfolder_path_for_db= os.path.join(current_directory, "database")
    subfolder_path_for_sqlscripts= os.path.join(current_directory, "sql_create")
    file_path = os.path.join(subfolder_path_for_sqlscripts, "01_drop_tables.sql")
    #file_path = os.path.join(subfolder_path_for_sqlscripts, "02_create_tables.sql")
    #file_path = os.path.join(subfolder_path_for_sqlscripts, "03_insert_records.sql")
    logger.info(f"Subfolder Path: {subfolder_path_for_sqlscripts}")
    logger.info(f"File Path: {file_path}")

    db_file_path = os.path.join(subfolder_path_for_db, "tran_project05_database.db")
     
    conn = sqlite3.connect(db_file_path) # for SQLite
    cursor = conn.cursor()

    with open(file_path, 'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)
    conn.commit()
    cursor.close()
    conn.close()

    #process_json_file()
    logger.info("db01_setup complete.")