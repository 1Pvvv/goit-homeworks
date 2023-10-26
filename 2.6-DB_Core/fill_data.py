import sqlite3
from datetime import datetime
from random import randint

from faker import Faker


NUMBER_GROUPS = 3
NUMBER_STUDENTS = randint(30, 50)
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_TEACHERS = randint(3, 5)


def generate_fake_data(number_groups, number_students, number_subjects, number_teachers) -> tuple():
    fake_groups = list()
    fake_students = list()
    fake_subjects = list()
    fake_teachers = list()
    fake_data = Faker()

    for _ in range(number_groups):
        fake_groups.append(f'{fake_data.random_letter()}-{fake_data.random_number(digits=2)}')

    for _ in range(number_students):
        fake_students.append((fake_data.first_name(), fake_data.last_name()))

    for _ in range(number_teachers):
        fake_teachers.append((fake_data.first_name(), fake_data.last_name()))

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.catch_phrase())

    return fake_groups, fake_students, fake_subjects, fake_teachers


def prepare_data(groups, students, subjects) -> tuple():
    for_groups = list()
    for group in groups:
        for_groups.append((group,))

    for_students = list()
    for student in students:
        for_students.append((*student, randint(1, NUMBER_GROUPS)))

    for_subjects = list()
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_grades = list()
    for student in range(1, NUMBER_STUDENTS + 1):
        for subject in range(1, NUMBER_SUBJECTS + 1):
            for grade in range(randint(1, 20)):
                try:
                    grade_date = datetime(2023, randint(1, 12), randint(1, 31)).date()
                except ValueError:
                    grade_date = datetime(2023, randint(1, 12), randint(1, 28)).date()
                for_grades.append((student, subject, randint(1, 100), grade_date))

    return for_groups, for_students, for_subjects, for_grades


def insert_data_to_db(groups, students, subjects, teachers, grades) -> None:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(first_name, last_name, group_id)
                               VALUES (?, ?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(first_name, last_name)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, grade_date)
                               VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        con.commit()


groups, students, subjects, teachers = generate_fake_data(
    NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_TEACHERS)

groups, students, subjects, grades = prepare_data(groups, students, subjects)

insert_data_to_db(groups, students, subjects, teachers, grades)
