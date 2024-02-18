SELECT
    group_id_id,
    AVG(grade) AS average_grade_group,
    (SELECT AVG(grade) FROM Grades) AS average_grade_scale
FROM
    Grades
GROUP BY
    group_id_id;