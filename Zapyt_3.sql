SELECT g.group_id_id, gr.group_name, AVG(g.grade) AS average_grade
FROM Grades g
JOIN Groups gr ON g.group_id_id = gr.id
WHERE g.subject_id = '1'
GROUP BY g.group_id_id, gr.group_name;