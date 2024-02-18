SELECT s.id, s.first_name, s.last_name, AVG(g.grade) AS average_grade
FROM Students s
JOIN Grades g ON s.id = g.student_id
GROUP BY s.id, s.first_name, s.last_name
ORDER BY average_grade DESC
LIMIT 5;