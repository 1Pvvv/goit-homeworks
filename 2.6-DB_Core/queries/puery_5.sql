-- Найти какие курсы читает определенный преподаватель.
SELECT s.subject_name
FROM subjects s
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE t.teacher_id = 3;
