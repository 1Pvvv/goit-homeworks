from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(255), nullable=False)


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.group_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    group = relationship('Group', backref='students')


class Teacher(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(255), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id',
                                            ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    teacher = relationship('Teacher', backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'

    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer, nullable=False)
    grade_date = Column(DateTime, nullable=False)
    student_id = Column(Integer, ForeignKey('students.student_id',
                                            ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.subject_id',
                                            ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
