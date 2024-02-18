SELECT sb.lecturer_id, sb.subject_name, AVG(g.grade) AS average_grade
FROM Grades g
JOIN Subjects sb ON g.subject_id = sb.id
JOIN Lecturers l ON sb.lecturer_id = l.id
GROUP BY sb.lecturer_id