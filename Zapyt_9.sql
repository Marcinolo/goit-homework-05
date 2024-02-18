SELECT s.first_name, s.last_name, sb.subject_name
FROM Students s
JOIN Grades g ON g.student_id = s.id
JOIN Subjects sb ON sb.id = g.subject_id
GROUP BY s.last_name