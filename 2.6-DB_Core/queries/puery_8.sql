-- Найти средний балл, который ставит определенный преподаватель по своим предметам.
SELECT t.first_name, t.last_name, AVG(g.grade) AS average_grade
FROM teachers t
JOIN subjects s ON t.teacher_id = s.teacher_id
JOIN grades g ON s.subject_id = g.subject_id
WHERE t.teacher_id = 2
GROUP BY t.teacher_id, t.first_name, t.last_name;
