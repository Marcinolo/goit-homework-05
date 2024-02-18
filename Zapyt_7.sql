SELECT s.first_name, s.last_name, gr.group_name, sb.subject_name, g.grade
FROM Students s
JOIN Grades g ON s.id = g.student_id
JOIN Groups gr ON s.group_id = gr.id
JOIN Subjects sb ON g.subject_id = sb.id
--WHERE gr.group_name = 'Grupa A'  -- Wybierz grupę
--AND sb.subject_name = 'Matematyka' -- Wybierz przedmiot
ORDER BY s.last_name, s.first_name;