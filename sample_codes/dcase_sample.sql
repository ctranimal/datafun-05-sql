-- Add a new column to the books table to store the author's age at the time of publication 
ALTER TABLE Students ADD COLUMN year_born INT;

-- Update the author_age_at_publication column in the Students table
-- NOTE: You might need to refresh the database to see results in the Students table
UPDATE Students
SET year_born = 2010
    WHERE Students.last_name = "Doe"; -- Add all of Doe's year_born to 2010;