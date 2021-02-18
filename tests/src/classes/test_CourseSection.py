from src.classes.Instructor import Instructor
from src.classes.TimeSlot import TimeSlot
from src.classes.CourseSection import CourseSection
from src.classes.Student import Student
from typing import List
import pytest


def test_course_section_inherits_attr():
    cs = CourseSection()
    assert hasattr(cs, "course_id")
    assert hasattr(cs, "dept")
    assert hasattr(cs, "course_name")
    assert hasattr(cs, "prereqs")


def test_course_section_has_initialized_attributes():
    cs = CourseSection()
    assert hasattr(cs, "section_id")
    assert type(cs.section_id) == str
    assert hasattr(cs, "time_slot")
    assert type(cs.time_slot) == TimeSlot
    assert hasattr(cs, "quarter")
    assert type(cs.quarter) == List[Instructor]
    assert hasattr(cs, "instructors")
    assert type(cs.instructors) == str
    assert hasattr(cs, "lead_instructor")
    assert type(cs.lead_instructor) == Instructor
    assert hasattr(cs, "capacity")
    assert type(cs.capacity) == int
    assert hasattr(cs, "instr_permission_req")
    assert type(cs.instr_permission_req) == bool
    assert hasattr(cs, "has_lab")
    assert type(cs.has_lab) == bool
    assert hasattr(cs, "lab_sections")
    assert type(cs.lab_sections) == List[CourseSection]
    assert hasattr(cs, "roster")
    assert type(cs.roster) == List[Student]


def test_load_course_section():
    cs = CourseSection.load_course_section()
    assert type(cs) == CourseSection


def test_load_labs():
    cs = CourseSection()
    cs.load_labs()
    type(cs.lab_sections) == List[CourseSection]


def test_add_student():
    cs = CourseSection()
    s = Student()
    cs.add_student(s)
    assert s in cs.roster


def test_drop_student():
    cs = CourseSection()
    s = Student()
    t = Student()
    cs.add_student(s)
    cs.add_student(t)
    cs.drop_student(t)
    assert s in cs.roster
    assert t not in cs.roster


def test_add_student():
    cs = CourseSection()
    i = Instructor()
    cs.add_instructor(i)
    assert i in cs.instructors


def test_drop_instructor():
    cs = CourseSection()
    i = Student()
    j = Student()
    cs.add_instructor(i)
    cs.add_instructor(j)
    cs.drop_instructor(j)
    assert i in cs.instructors
    assert j not in cs.instructors
