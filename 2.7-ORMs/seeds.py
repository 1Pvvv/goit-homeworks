from datetime import datetime
from random import randint

from faker import Faker

from connect_db import session
from models import Group, Student, Teacher, Subject, Grade
from sqlalchemy import delete, func

NUMBER_GROUPS = 3
NUMBER_STUDENTS = randint(30, 50)
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_TEACHERS = randint(3, 5)

fake_data = Faker()


def select_id_from_table(table):
    min_id = session.query(func.min(table)).scalar()
    max_id = session.query(func.max(table)).scalar()
    return min_id, max_id


def fake_groups():
    for _ in range(NUMBER_GROUPS):
        group = Group(
            group_name=f"{fake_data.random_letter()}-{fake_data.random_number(digits=2)}"
        )
        session.add(group)
        session.commit()


def fake_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(
            first_name=fake_data.first_name(), last_name=fake_data.last_name()
        )
        session.add(teacher)
        session.commit()


def fake_students():
    for _ in range(NUMBER_STUDENTS):
        student = Student(
            first_name=fake_data.first_name(),
            last_name=fake_data.last_name(),
            group_id=(randint(*select_id_from_table(Group.group_id)))
            # group_id=randint(1, NUMBER_GROUPS + 1),
        )
        session.add(student)
        session.commit()


def fake_subjects():
    for _ in range(NUMBER_SUBJECTS):
        subject = Subject(
            subject_name=fake_data.catch_phrase(),
            teacher_id=(randint(*select_id_from_table(Teacher.teacher_id)))
            # teacher_id=randint(1, NUMBER_TEACHERS + 1),
        )
        session.add(subject)
        session.commit()


def fake_grades():
    for student in range(*select_id_from_table(Student.student_id)):
        for subject in range(*select_id_from_table(Subject.subject_id)):
            for _ in range(randint(1, 20)):
                try:
                    grade_date = datetime(2023, randint(1, 12), randint(1, 31)).date()
                except ValueError:
                    grade_date = datetime(2023, randint(1, 12), randint(1, 28)).date()

                grade = Grade(
                    grade=randint(1, 100),
                    grade_date=grade_date,
                    student_id=student,
                    subject_id=subject,
                )
                session.add(grade)
                session.commit()


def db_clear():
    session.execute(delete(Group))
    session.commit()
    session.execute(delete(Teacher))
    session.commit()
    session.execute(delete(Student))
    session.commit()
    session.execute(delete(Subject))
    session.commit()
    session.execute(delete(Grade))
    session.commit()


if __name__ == "__main__":
    db_clear()

    fake_groups()
    fake_teachers()
    fake_students()
    fake_subjects()
    fake_grades()
