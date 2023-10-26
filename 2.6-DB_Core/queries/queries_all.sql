-- Найти 5 студентов с наибольшим средним баллом по всем предметам.
SELECT s.student_id, s.first_name, s.last_name, AVG(g.grade) AS average_grade
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
GROUP BY s.student_id, s.first_name, s.last_name
ORDER BY average_grade DESC
LIMIT 5;

-- Найти студента с наивысшим средним баллом по определенному предмету.
SELECT s.student_id, s.first_name, s.last_name, AVG(g.grade) AS average_grade
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
WHERE g.subject_id = 1,
GROUP BY s.student_id, s.first_name, s.last_name
ORDER BY average_grade DESC
LIMIT 1;

-- Найти средний балл в группах по определенному предмету.
SELECT g.group_id, group_name, AVG(gr.grade) AS average_grade
FROM groups g
LEFT JOIN students s ON g.group_id = s.group_id
LEFT JOIN grades gr ON s.student_id = gr.student_id
WHERE gr.subject_id = 1,
GROUP BY g.group_id, group_name
ORDER BY average_grade DESC;

-- Найти средний балл на потоке (по всей таблице оценок).
SELECT AVG(grade) AS average_grade
FROM grades;

-- Найти какие курсы читает определенный преподаватель.
SELECT s.subject_name
FROM subjects s
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE t.teacher_id = 1;

-- Найти список студентов в определенной группе.
SELECT first_name, last_name
FROM students
WHERE group_id = 1;

-- Найти оценки студентов в отдельной группе по определенному предмету.
SELECT s.first_name, s.last_name, g.grade, g.grade_date
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE s.group_id = 1
AND g.subject_id = 2;

-- Найти средний балл, который ставит определенный преподаватель по своим предметам.
SELECT t.first_name, t.last_name, AVG(g.grade) AS average_grade
FROM teachers t
JOIN subjects s ON t.teacher_id = s.teacher_id
JOIN grades g ON s.subject_id = g.subject_id
WHERE t.teacher_id = 2
GROUP BY t.teacher_id, t.first_name, t.last_name;

-- Найти список курсов, которые посещает определенный студент.
SELECT DISTINCT s.subject_name, t.last_name AS teacher_last_name
FROM students st
JOIN grades g ON st.student_id = g.student_id
JOIN subjects s ON g.subject_id = s.subject_id
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE st.student_id = 1;

-- Список курсов, которые определенному студенту читает определенный преподаватель.
SELECT DISTINCT s.subject_name,
  t.last_name AS teacher_last_name,
  st.last_name AS student_last_name
FROM students st
JOIN grades g ON st.student_id = g.student_id
JOIN subjects s ON g.subject_id = s.subject_id
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE st.student_id = 1
  AND t.teacher_id = 1;

-- Средний балл, который определенный преподаватель ставит определенному студенту.
SELECT AVG(g.grade) AS average_grade,
  t.last_name AS teacher_last_name,
  st.last_name AS student_last_name
FROM students st
JOIN grades g ON st.student_id = g.student_id
JOIN subjects s ON g.subject_id = s.subject_id
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE st.student_id = 1
  AND t.teacher_id = 1;

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
