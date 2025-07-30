-- Query to count the number of test-scores taken by each student
SELECT b.test_title AS test_title, COUNT(b.testscore_id) AS testscore_count
FROM Students a
LEFT JOIN Testscores b ON a.student_id = b.student_id
GROUP BY b.test_title;