"""
Use Python to execute feature queries from the sql_features folder.
"""

#####################################
# Import Modules
#####################################

# Imports from Python Standard Library
import sqlite3
import os
import pathlib
import argparse   ## to parse argument for command-line 

# Import local modules
from utils_logger import logger
import utils_project

#####################################
# Declare Global Variables
#####################################


#####################################
# Define Functions
#####################################
def execute_sql_file(connection, file_path) -> None:
    """
    Executes a SQL file using the provided SQLite connection.

    Args:
        connection (sqlite3.Connection): SQLite connection object.
        file_path (str): Path to the SQL file to be executed.
    """
    try:
        with open(file_path, 'r') as file:
            sql_script: str = file.read()
        with connection:
            connection.executescript(sql_script)
            logger.info(f"Executed: {file_path}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path}: {e}")
        raise


#####################################
# Main Execution
#####################################
def main() -> None:

    # Log start of feature execution
    logger.info("Starting feature queries execution...")

    # call this function to SET global vars ROOT_DIR, DB_PATH
    utils_project.set_globalvars_for_project_folders("sql_queries") 
    logger.info(f"Global vars ROOT_DIR: {utils_project.ROOT_DIR}")
    logger.info(f"Global vars DB_PATH: {utils_project.DB_PATH}")  

    parser = argparse.ArgumentParser(description="A simple script with arguments.")
    parser.add_argument("--setup", type=str, help="enter a number")
    parser.add_argument("--query", type=str, help="enter a number")

    args = parser.parse_args()

    if args.setup:
        logger.info(f"Program is called with argument -setup {args.setup}.")
    if args.query:
        logger.info(f"Program is called with argument -query {args.query}.")

    # Ensure the database file exists before attempting to connect
    if not utils_project.DB_PATH.exists():
        logger.error(f"Database file not found at {utils_project.DB_PATH}. Ensure the database is created first.")
        return

    # Connect to SQLite database
    try:
        connection = sqlite3.connect(utils_project.DB_PATH)
        logger.info(f"Connected to database: {utils_project.DB_PATH}")

        # Execute all SQL files in the sql_features folder
        #for sql_file in sorted(utils_project.SQL_SCRIPT_FOLDER.glob("*.sql")):
        #    execute_sql_file(connection, sql_file)

        if(args.setup): 
            if(int(args.setup) == 1): 
                utils_project.set_globalvars_for_project_folders("sql_create") 
                execute_sql_file(connection, utils_project.SQL_SCRIPT_FOLDER.joinpath('01_drop_tables.sql'))
                execute_sql_file(connection, utils_project.SQL_SCRIPT_FOLDER.joinpath('02_create_tables.sql'))
            else:
                logger.error(f"Unknown option -setup ={args.setup}")        

        if(args.query):
            utils_project.set_globalvars_for_project_folders("sql_queries") 
            if(int(args.query) == 1): 
                execute_sql_file(connection, utils_project.SQL_SCRIPT_FOLDER.joinpath('01_query_aggregation.sql'))
            elif(int(args.query) == 2):
                execute_sql_file(connection, utils_project.SQL_SCRIPT_FOLDER.joinpath('02_query_filter.sql'))
            elif(int(args.query) == 3):
                execute_sql_file(connection, utils_project.SQL_SCRIPT_FOLDER.joinpath('03_query_group_by.sql')) 
            elif(int(args.query) == 4):
                execute_sql_file(connection, utils_project.SQL_SCRIPT_FOLDER.joinpath('04_query_join.sql'))
            elif(int(args.query) == 5):
                execute_sql_file(connection, utils_project.SQL_SCRIPT_FOLDER.joinpath('05_query_sorting.sql'))  
            else:
                logger.error(f"Unknown option -query ={args.query}")



        logger.info("Feature queries execution completed successfully.")
    except Exception as e:
        logger.error(f"Error during feature queries execution: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")


if __name__ == '__main__':
    main()
