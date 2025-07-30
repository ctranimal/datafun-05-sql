-- Query to count the number of test-scores taken by each student
SELECT a.last_name AS student_lastname, COUNT(b.testscore_id) AS testscore_count
FROM Students a
LEFT JOIN Testscores b ON a.student_id = b.student_id
GROUP BY student_lastname
ORDER BY testscore_count DESC;