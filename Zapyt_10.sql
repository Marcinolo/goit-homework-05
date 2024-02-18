SELECT  l.last_name, sb.subject_name, s.last_name
FROM Subjects sb
JOIN Lecturers l ON sb.lecturer_id = l.id
JOIN Grades g ON sb.id = g.subject_id
JOIN Students s ON g.student_id = s.id
WHERE l.id = '2'
GROUP BY s.last_name