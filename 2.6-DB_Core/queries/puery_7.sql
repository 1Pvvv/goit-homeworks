-- Найти оценки студентов в отдельной группе по определенному предмету.
SELECT s.first_name, s.last_name, g.grade, g.grade_date
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE s.group_id = 1
AND g.subject_id = 2;
