-- Оценки студентов в определенной группе по определенному предмету на последнем занятии.
SELECT sbj.subject_name,
  s.first_name AS student_first_name,
  s.last_name AS student_last_name,
  g.grade, g.grade_date
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sbj ON g.subject_id = sbj.subject_id
WHERE g.grade_date = (SELECT MAX(grade_date) FROM grades WHERE student_id = s.student_id AND subject_id = sbj.subject_id)
  AND sbj.subject_id = 2
  AND s.group_id = 1;
