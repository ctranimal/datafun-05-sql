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
    utils_project.set_globalvars_for_project_folders("sql_features") 
    logger.info(f"Global vars ROOT_DIR: {utils_project.ROOT_DIR}")
    logger.info(f"Global vars DB_PATH: {utils_project.DB_PATH}")  

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

        execute_sql_file(connection, utils_project.SQL_SCRIPT_FOLDER.joinpath('add_to_students_yearborn.sql'))

        logger.info("Feature queries execution completed successfully.")
    except Exception as e:
        logger.error(f"Error during feature queries execution: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")


if __name__ == '__main__':
    main()
