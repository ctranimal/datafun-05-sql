-- Query to count the number of books written by each author
SELECT Students.last_name AS author_name, COUNT(b.testscore_id) AS book_count
FROM Students a
LEFT JOIN Testscores b ON a.student_id = b.student_id
GROUP BY b.test_title
ORDER BY book_count DESC;