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
);

CREATE TABLE TestScores (
    testscore_id TEXT PRIMARY KEY,
    test_title TEXT NOT NULL
    student_id TEXT NOT NULL,
    test_category TEXT NOT NULL,
    score REAL,
    date_taken TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);


Explanation
Students Table:
     student_id: This column serves as the primary key and automatically increments, ensuring each student has a unique identifier.
    first_name: Stores the student's first name, required (NOT NULL).
    last_name: Stores the student's last name, also required.
    email: Stores the student's email address and is set to be unique (UNIQUE), preventing duplicate email entries.
Grades Table:
    grade_id: The primary key for the grades table, automatically incrementing.
    student_id: This column is a foreign key, establishing a relationship with the Students table. It links a grade to a specific student. The FOREIGN KEY (student_id) REFERENCES Students(student_id) clause ensures data integrity, meaning you can't enter a grade for a non-existent student.
    subject: Stores the name of the subject the grade is for.
    score: Stores the numerical grade, defined as a real number (REAL) to accommodate decimal grades.