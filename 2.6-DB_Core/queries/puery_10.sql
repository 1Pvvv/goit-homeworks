-- Список курсов, которые определенному студенту читает определенный преподаватель.
SELECT DISTINCT s.subject_name,
  t.last_name AS teacher_last_name,
  st.last_name AS student_last_name
FROM students st
JOIN grades g ON st.student_id = g.student_id
JOIN subjects s ON g.subject_id = s.subject_id
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE st.student_id = 5
  AND t.teacher_id = 2;
