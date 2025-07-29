
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
    # We know reading from a file can raise exceptions, so we wrap it in a try block
    # For example, the file might not exist, or the file might not be readable
    try:
        with open(file_path, 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
        with connection:
            # Use the connection as a context manager to execute the SQL script
            connection.executescript(sql_script)
            logger.info(f"Executed: {file_path}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path}: {e}")
        raise

#####################################
# Main Execution
#####################################

def main() -> None:

    # Log start of database setup
    logger.info("Starting database setup...")
    
    # Define path variables
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_CREATE_FOLDER = ROOT_DIR.joinpath("sql_create")
    DATA_FOLDER = ROOT_DIR.joinpath("data")
    DATABASE_FOLDER = ROOT_DIR.joinpath("database")
    DB_PATH = DATABASE_FOLDER.joinpath('tran_project05_database.db')

    # Ensure the data folder where we will put the db exists
    DATABASE_FOLDER.mkdir(exist_ok=True)

    # Connect to SQLite database (it will be created if it doesn't exist)
    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")

        # Execute SQL files to set up the database
        # Pass in the connection and the path to the SQL file to be executed
        execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('01_drop_tables.sql'))
        execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('02_create_tables.sql'))
        execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('03_insert_records.sql'))

        logger.info("Database setup completed successfully.")
    except Exception as e:
        logger.error(f"Error during database setup: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")


if __name__ == '__main__':
    main()