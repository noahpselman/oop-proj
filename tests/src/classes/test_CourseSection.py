from unittest.mock import Mock
from src.classes.Exceptions import CourseSectionFullExcetion
from src.classes.Quarter import Quarter
from tests.conftest import fake_course_section
from src.classes.Instructor import Instructor
from src.classes.TimeSlot import TimeSlot
from src.classes.CourseSection import CourseSection
from src.classes.Student import FullTimeStudent, Student
from typing import List
import pytest


def test_course_section_inherits_attr(fake_course_section):
    cs = fake_course_section
    assert hasattr(cs, "course_id")
    assert hasattr(cs, "dept")
    assert hasattr(cs, "course_name")
    assert hasattr(cs, "prereqs")


def test_course_section_has_initialized_attributes(fake_course_section):
    # TODO do a better mock so these things can be properly tested
    cs = fake_course_section
    assert hasattr(cs, "section_id")
    assert type(cs.section_id) == str
    assert hasattr(cs, "time_slot")
    assert type(cs.time_slot) == TimeSlot
    assert hasattr(cs, "quarter")
    assert type(cs.quarter) == Quarter
    assert hasattr(cs, "instructors")
    assert type(cs.instructors) == list
    assert all([type(i) == Instructor for i in cs.instructors])
    assert hasattr(cs, "lead_instructor")
    assert type(cs.lead_instructor) == Instructor
    assert hasattr(cs, "capacity")
    assert type(cs.capacity) == int
    assert hasattr(cs, "instr_permission_req")
    assert type(cs.instr_permission_req) == bool
    assert type(cs.has_lab) == bool
    assert hasattr(cs, "lab_sections")
    assert type(cs.lab_sections) == list
    assert all([type(l) == CourseSection for l in cs.lab_sections])
    assert hasattr(cs, "roster")
    assert type(cs.roster) == list
    assert all([issubclass(type(s), Student) for s in cs.roster])
    assert hasattr(cs, "auditors")
    assert type(cs.auditors) == list
    assert all([issubclass(type(s), Student) for s in cs.auditors])


def test_course_designation(fake_course_section):
    cs = fake_course_section
    assert cs.course_designation == "MATH12345/01 Winter 2021"


def test_add_instructor(fake_course_section):
    cs = fake_course_section
    instructor = Mock()
    cs.add_instructor(instructor)
    assert len(cs.instructors) == 1


def test_add_student_to_roster(fake_course_section):
    course_section = fake_course_section
    course_section.capacity = 2
    s = FullTimeStudent(Mock())
    course_section.add_student_to_roster(s)
    assert s in course_section.roster


def test_enrollment_capacity_error(fake_course_section):
    course_section = fake_course_section
    course_section.capacity = 2
    s = FullTimeStudent(Mock())
    t = FullTimeStudent(Mock())
    u = FullTimeStudent(Mock())
    course_section.add_student_to_roster(s)
    course_section.add_student_to_roster(t)
    try:
        course_section.add_student_to_roster(u)
    except CourseSectionFullExcetion:
        assert True
    else:
        assert False


def test_add_auditors(fake_course_section):
    course_section = fake_course_section
    s = FullTimeStudent(Mock())
    course_section.add_student_to_auditors(s)
    assert s in course_section.auditors

# TODO


def test_load_course_section():
    cs = CourseSection.load_course_section()
    assert type(cs) == CourseSection


# def test_load_labs():
#     cs = CourseSection()
#     cs.load_labs()
#     type(cs.lab_sections) == List[CourseSection]


# def test_add_student():
#     cs = CourseSection()
#     s = Student()
#     cs.add_student(s)
#     assert s in cs.roster


# def test_drop_student():
#     cs = CourseSection()
#     s = Student()
#     t = Student()
#     cs.add_student(s)
#     cs.add_student(t)
#     cs.drop_student(t)
#     assert s in cs.roster
#     assert t not in cs.roster


# def test_add_student():
#     cs = CourseSection()
#     i = Instructor()
#     cs.add_instructor(i)
#     assert i in cs.instructors


# def test_drop_instructor():
#     cs = CourseSection()
#     i = Student()
#     j = Student()
#     cs.add_instructor(i)
#     cs.add_instructor(j)
#     cs.drop_instructor(j)
#     assert i in cs.instructors
#     assert j not in cs.instructors
