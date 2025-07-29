PRAGMA foreign_keys = ON;

-- Create the Students table
CREATE TABLE Students (
    student_id TEXT PRIMARY KEY,    -- Prefixed sequential ID as the primary key (e.g., STUDENT_001
    first_name TEXT NOT NULL,       -- firstname (required)
    last_name TEXT NOT NULL,        -- lastname (required)
    email TEXT                      -- email address of the student (optional)
);

-- Create the TestScores table
CREATE TABLE TestScores (          
    testscore_id TEXT PRIMARY KEY,  -- Prefixed sequential ID as the primary key (e.g., TESTSCORE_001
    test_title TEXT NOT NULL,       -- To identify what type of tests: English, Math etc ... 
    student_id TEXT NOT NULL,       -- To identify which student does this relate to (i.e: who took this test)
    test_category TEXT NOT NULL,    -- Test categories: AP, PA Keystone, SAT etc ...
    score REAL,            -- What are the scores, by default, it's zero (optional, default to zero)
    date_taken TEXT,                -- the date the test was taken (optional)
    FOREIGN KEY (student_id) REFERENCES Students(student_id) -- relationship with Students table
);
