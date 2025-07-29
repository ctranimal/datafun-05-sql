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
    ('TESTSCORE_001', 'SAT English', 'STUDENT__001', 'SAT', 80, '12/31/2024'),
    ('TESTSCORE_001', 'SAT Math', 'STUDENT__001', 'SAT', 80, '3/31/2024'),
    ('TESTSCORE_001', 'AP Physics', 'STUDENT__001', 'AP', 80, ''), 
    ('TESTSCORE_002', 'Keystone English', 'STUDENT__002', 'SAT', 80, '12/31/2025'), 
    ('TESTSCORE_002', 'SAT English', 'STUDENT__002', 'SAT', 75, '12/31/2024'), 
    ('TESTSCORE_002', 'SAT English', 'STUDENT__002', 'SAT', 65, '12/31/2024'), 
    ('TESTSCORE_003', 'SAT English', 'STUDENT__003', 'SAT', 80, '12/31/2024'), 
    ('TESTSCORE_004', 'SAT Math', 'STUDENT__004', 'SAT', 90, '12/31/2024'), 
    ('TESTSCORE_005', 'AP Chemistry', 'STUDENT__005', 'AP', 95, '12/31/2024'), 
    ('TESTSCORE_006', 'SAT History', 'STUDENT__006', 'AP', 45, '12/31/2024');
    