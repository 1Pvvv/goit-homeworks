from random import randint
from seeds import select_id_from_table
from connect_db import session
from models import Group, Student, Teacher, Subject, Grade
from sqlalchemy import func, desc


# Найти 5 студентов с наибольшим средним баллом по всем предметам.
def select_1():
    result = (
        session.query(
            Student.first_name,
            Student.last_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.student_id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


# Найти студента с наивысшим средним баллом по определенному предмету.
def select_2():
    subject_id = randint(*select_id_from_table(Subject.subject_id))
    result = (
        session.query(
            Student.student_id,
            Student.first_name,
            Student.last_name,
            func.round(func.avg(Grade.grade), 2).label("average_grade"),
        )
        .outerjoin(Grade, Student.student_id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.student_id, Student.first_name, Student.last_name)
        .order_by(func.avg(Grade.grade).desc())
        .limit(1)
    ).first()
    return result


# Найти средний балл в группах по определенному предмету.
def select_3():
    subject_id = randint(*select_id_from_table(Subject.subject_id))
    result = (
        session.query(
            Group.group_id,
            Group.group_name,
            func.round(func.avg(Grade.grade), 2).label("average_grade"),
        )
        .outerjoin(Student, Group.group_id == Student.group_id)
        .outerjoin(Grade, Student.student_id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.group_id, Group.group_name)
        .order_by(func.avg(Grade.grade).desc())
    ).all()
    return result


# Найти средний балл на потоке (по всей таблице оценок).
def select_4():
    return session.query(
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).first()


# Найти какие курсы читает определенный преподаватель.
def select_5():
    teacher_id = randint(*select_id_from_table(Teacher.teacher_id))
    result = (
        session.query(Subject.subject_name)
        .join(Teacher, Subject.teacher_id == Teacher.teacher_id)
        .filter(Teacher.teacher_id == teacher_id)
        .all()
    )
    return result


# Найти список студентов в определенной группе.
def select_6():
    group_id = randint(*select_id_from_table(Group.group_id))
    result = (
        session.query(Student.first_name, Student.last_name)
        .filter(Student.group_id == group_id)
        .all()
    )
    return result


# Найти оценки студентов в отдельной группе по определенному предмету.
def select_7():
    group_id = randint(*select_id_from_table(Group.group_id))
    subject_id = randint(*select_id_from_table(Subject.subject_id))
    result = (
        session.query(
            Student.first_name, Student.last_name, Grade.grade, Grade.grade_date
        )
        .join(Grade, Student.student_id == Grade.student_id)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    return result


# Найти средний балл, который ставит определенный преподаватель по своим предметам.
def select_8():
    teacher_id = randint(*select_id_from_table(Teacher.teacher_id))
    result = (
        session.query(
            Teacher.first_name,
            Teacher.last_name,
            func.round(func.avg(Grade.grade), 2).label("average_grade"),
        )
        .join(Subject, Teacher.teacher_id == Subject.teacher_id)
        .join(Grade, Subject.subject_id == Grade.subject_id)
        .filter(Teacher.teacher_id == teacher_id)
        .group_by(Teacher.teacher_id, Teacher.first_name, Teacher.last_name)
        .all()
    )
    return result


# Найти список курсов, которые посещает определенный студент.
def select_9():
    student_id = randint(*select_id_from_table(Student.student_id))
    result = (
        session.query(
            Subject.subject_name, Teacher.last_name.label("teacher_last_name")
        )
        .select_from(Subject)
        .join(Grade, Grade.subject_id == Subject.subject_id)
        .join(Student, Student.student_id == Grade.student_id)
        .join(Teacher, Teacher.teacher_id == Subject.teacher_id)
        .filter(Student.student_id == student_id)
        .distinct()
        .all()
    )
    return result


# Список курсов, которые определенному студенту читает определенный преподаватель.
def select_10():
    student_id = randint(*select_id_from_table(Student.student_id))
    teacher_id = randint(*select_id_from_table(Teacher.teacher_id))
    result = (
        session.query(
            Subject.subject_name,
            Teacher.last_name.label("teacher_last_name"),
            Student.last_name.label("student_last_name"),
        )
        .join(Grade, Student.student_id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.subject_id)
        .join(Teacher, Subject.teacher_id == Teacher.teacher_id)
        .filter(Student.student_id == student_id, Teacher.teacher_id == teacher_id)
        .distinct()
        .all()
    )
    return result


print("Найти 5 студентов с наибольшим средним баллом по всем предметам.")
print(select_1())
print("\nНайти студента с наивысшим средним баллом по определенному предмету.")
print(select_2())
print("\nНайти средний балл в группах по определенному предмету.")
print(select_3())
print("\nНайти средний балл на потоке (по всей таблице оценок).")
print(select_4())
print("\nНайти какие курсы читает определенный преподаватель.")
print(select_5())
print("\nНайти список студентов в определенной группе.")
print(select_6())
print("\nНайти оценки студентов в отдельной группе по определенному предмету.")
print(select_7())
print(
    "\nНайти средний балл, который ставит определенный преподаватель по своим предметам."
)
print(select_8())
print("\nНайти список курсов, которые посещает определенный студент.")
print(select_9())
print(
    "\nСписок курсов, которые определенному студенту читает определенный преподаватель."
)
print(select_10())
