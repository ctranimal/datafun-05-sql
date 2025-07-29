-- insert records into the Students table first
INSERT INTO Students VALUES
    ('STUDENT_001', 'John 01', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_002', 'John 02', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_003', 'John 03', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_004', 'John 04', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_005', 'John 05', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_006', 'John 06', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_007', 'John 07', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_008', 'John 08', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_009', 'John 09', 'Doe', 'firstname.lastname@blah.com'),
    ('STUDENT_010', 'John 10', 'Doe', 'firstname.lastname@blah.com');

-- Insert records into the TestScores table
-- And include foreign key references to the Students table
-- IMPORTANT: No tic marks inside a string, use two single quotes to escape a single quote
INSERT INTO TestScores VALUES
    ('TESTSCORE_001', 'SAT English', 'STUDENT_001', 'SAT', 80, '12/31/2024'),
    ('TESTSCORE_002', 'SAT Math', 'STUDENT_001', 'SAT', 80, '3/31/2024'),
    ('TESTSCORE_003', 'AP Physics', 'STUDENT_001', 'AP', 80, ''), 
    ('TESTSCORE_004', 'Keystone English', 'STUDENT_002', 'SAT', 80, '12/31/2025'), 
    ('TESTSCORE_005', 'SAT English', 'STUDENT_002', 'SAT', 75, '12/31/2024'), 
    ('TESTSCORE_006', 'SAT English', 'STUDENT_002', 'SAT', 65, '12/31/2024'), 
    ('TESTSCORE_007', 'SAT English', 'STUDENT_003', 'SAT', 80, '12/31/2024'), 
    ('TESTSCORE_008', 'SAT Math', 'STUDENT_004', 'SAT', 90, '12/31/2024'), 
    ('TESTSCORE_009', 'AP Chemistry', 'STUDENT_005', 'AP', 95, '12/31/2024'), 
    ('TESTSCORE_010', 'SAT History', 'STUDENT_006', 'AP', 45, '12/31/2024');
    