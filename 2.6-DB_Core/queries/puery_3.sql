-- Найти средний балл в группах по определенному предмету.
SELECT g.group_id, group_name, AVG(gr.grade) AS average_grade
FROM groups g
LEFT JOIN students s ON g.group_id = s.group_id
LEFT JOIN grades gr ON s.student_id = gr.student_id
WHERE gr.subject_id = 1,
GROUP BY g.group_id, group_name
ORDER BY average_grade DESC;
