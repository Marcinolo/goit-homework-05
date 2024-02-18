SELECT s.subject_name, s.lecturer_id, l.last_name from Subjects s
JOIN Lecturers l ON l.id = s.lecturer_id
GROUP BY s.subject_name