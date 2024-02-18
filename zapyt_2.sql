SELECT s.id, s.first_name, s.last_name, sub.subject_name, AVG(g.grade) AS average_grade
FROM Students s
JOIN Grades g ON s.id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.id
WHERE g.subject_id = '1'
GROUP BY s.id, s.first_name, s.last_name, sub.subject_name
ORDER BY average_grade DESC