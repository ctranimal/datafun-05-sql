
-- Update the email field for Students table with matching student's first/lastname
-- NOTE: You might need to refresh the database to see results in the Students table
UPDATE Students
SET email = "newemail_addr@blah.com"
    WHERE Students.last_name = "Doe" AND Students.first_name = "John 08";
    