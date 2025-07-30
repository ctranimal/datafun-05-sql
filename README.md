# Ken McTran -- Exploratory SQL 

## Purposes
    The purpose of this repository  is to implement project 05 for SQL exploration

## Workflow:
    Repeatable workflows include the following:
    1. Follow best-practices for git-update-push to ensure workable code are regularly checked-in into cloud-based Github repository. After this step, do a 'git clone' to clone remote cloud-based GitHub repository into ~/Repos/datafun-05-sql directory
    2. On Mac, change to ~/Repos/datafun-05-sql directory created above. This step create a local .venv directory to install tool into --> 
    ```
    cd ~/Repos/datafun-05-sql      
    python3 -m venv .venv
    ```
    
    3. On Mac, next 2 lines install needed tools (documented in requirements.txt ) into .venv environment
    ```
    python3 -m pip install --upgrade pip setuptools wheel
    python3 -m pip install -r requirements.txt
    ```

    4. On Mac, this command would activate the environment
    ```
    source .venv/bin/activate 
    ```

    5. At terminal, use the command:
    ``` 
    code ~/Repos/datafun-05-sql
    ``` 
    to launch VS Code (previously installed on MAC) to open/edit/execute code related to this project.

## SQL Schemas
    For this project, I'll implement 2 tables to help manage students' grades

    CREATE TABLE Students (
    student_id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT
) CREATE TABLE TestScores (
    testscore_id TEXT PRIMARY KEY,
    test_title TEXT NOT NULL
    student_id TEXT NOT NULL,
    test_category TEXT NOT NULL,
    score REAL,
    date_taken TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
)
## Explanation
### Students Table:
    student_id: This column serves as the primary key, must be unique
    first_name: Stores the student's first name, required (NOT NULL).
    last_name: Stores the student's last name, also required.
    email: Stores the student's email address and is set to be unique (UNIQUE), preventing duplicate email entries.
### TestScores Table:
    testscore_id: The primary key for the TestScores table, must be unique.
    test_title: This column describe, via a title, which type of test it is, example: AP Biology etc ..., required (Not Null)
    student_id: This column is a foreign key, establishing a relationship with the Students table, required (Not Null)
    test_category: This coloumn describes which type of tests: SAT, AP etc ..., required (Not Null)
    score: Stores the numerical grade, defined as a real number (REAL) to accommodate decimal grades.
    year_taken: Noted the year the test was taken.

## Folders structure of the project:
### data folder: 
    1. Contain students.csv with 10 rows representing students
    2. testscores.csv with 40+ rows of test scores data
### database folder:
    contain the sqlite database for this project
### sample_codes folder:
    contain sample, starter-code provided by the instructor
### sql_create, sql_features and sql_queries:
    contain the sql calls that implement various requirements for this project.
### the main scripts db*.py script and tran_testscore_manager.py script
    1. provide for ways to invoke the SQL stored procedures in sql_create, sql_features and sql_queries folders.
    2. On a terminal windows on Mac, after following instructions (in above sections) for creating .venv and installing various required packages, here're the instructions to launch these scripts:
        a. python3 db01_setup.py
        b. python3 db02_features.py
        c. db03_queries.py
### Please read the document tran_demo.ipynb to see the results of running various scripts db01_setup.py, db02_features.py and db03_queries.py
