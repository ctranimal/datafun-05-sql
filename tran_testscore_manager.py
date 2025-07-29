'''
This Python script requires an external dependency (pandas),
so we'll need a project virtual environment.

Note: pandas now requires pyarrow to be installed as well.

For Windows, my commands are:

py -m venv .venv
.venv\Scripts\Activate
py -m pip install pandas pyarrow
py book_manager.py
'''

#####################################
# Import Modules
#####################################
# Import from Python Standard Library first
import sqlite3
import pathlib

# Import from external packages
import pandas as pd

#import local utilities
import utils_project
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################
# Define paths using joinpath
#ROOT_DIR: str = ""
#SQL_SCRIPT_FOLDER: str = ""
#DATA_FOLDER: str = ""
#DATABASE_FOLDER: str = ""
#DB_PATH: str = ""
#db_file_path = utils_project.DB_PATH
#sql_file_path = pathlib.Path("sql_create").joinpath("02_create_tables.sql")
STUDENT_DATA_PATH = ""
TESTSCORE_DATA_PATH = ""
#STUDENT_DATA_PATH = utils_project.DATA_FOLDER.joinpath("students.csv")
#TESTSCORE_DATA_PATH = utils_project.DATA_FOLDER.joinpath("testscores.csv")


#####################################
# Define Functions
#####################################

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path, delete_prev_tables: bool):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_path) as conn:

            if(delete_prev_tables):
                execute_sql_file(conn, utils_project.SQL_SCRIPT_FOLDER.joinpath('01_drop_tables.sql'))
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, student_data_path, testscore_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        students_df = pd.read_csv(student_data_path)
        testscores_df = pd.read_csv(testscore_data_path)
        with sqlite3.connect(db_path) as conn:
            students_df.to_sql("Students", conn, if_exists="replace", index=False)
            testscores_df.to_sql("TestScores", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

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

def main():
    global STUDENT_DATA_PATH
    global TESTSCORE_DATA_PATH

    utils_project.set_globalvars_for_project_folders("sql_create") 
    logger.info(f"Global vars ROOT_DIR: {utils_project.ROOT_DIR}")
    logger.info(f"Global vars DB_PATH: {utils_project.DB_PATH}")   

    STUDENT_DATA_PATH = utils_project.DATA_FOLDER.joinpath("students.csv")
    TESTSCORE_DATA_PATH = utils_project.DATA_FOLDER.joinpath("testscores.csv")

    sql_file_path = utils_project.SQL_SCRIPT_FOLDER.joinpath("02_create_tables.sql")
    paths_to_verify = [sql_file_path, STUDENT_DATA_PATH, TESTSCORE_DATA_PATH]
    verify_and_create_folders(paths_to_verify)
    
    create_database(utils_project.DB_PATH)
    create_tables(utils_project.DB_PATH, sql_file_path, True)
    insert_data_from_csv(utils_project.DB_PATH, STUDENT_DATA_PATH, TESTSCORE_DATA_PATH)

if __name__ == "__main__":
    main()
