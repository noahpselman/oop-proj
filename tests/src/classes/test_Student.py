from src.classes.CourseSection import CourseSection
from src.classes.Exceptions import StudentFullCourseloadException, StudentHasRestrictionsException
from tests.conftest import load_student_full_courseload
from typing import List
from src.classes.StudentState import FullCourseloadStudentState, OpenStudentState, RestrictedStudentState
from src.classes.Restriction import *
from src.classes.User import User
from src.classes.Student import FullTimeStudent, PartTimeStudent, Student
from src.database.mappers.StudentMapper import StudentMapper
from unittest.mock import Mock
import pytest


def test_map_student_from_db(setup_db, load_student_restrictions):

    student = load_student_restrictions
    assert issubclass(type(student), Student)


def test_parttime_student_has_attr():
    user_data = User("69", "Noah", "noah@email.com")
    student = PartTimeStudent(user_data)
    assert hasattr(student, "user_data")
    assert hasattr(student.user_data, "uid")
    assert hasattr(student.user_data, "full_name")
    assert hasattr(student.user_data, "email")
    assert hasattr(student, "major")
    assert hasattr(student, "exp_grad_date")
    assert student.maximum_enrollment == 2


def test_fulltime_student_has_attr():
    user_data = User("69", "Noah", "noah@email.com")
    student = FullTimeStudent(user_data)
    assert hasattr(student, "user_data")
    assert hasattr(student.user_data, "uid")
    assert hasattr(student.user_data, "full_name")
    assert hasattr(student.user_data, "email")
    assert hasattr(student, "major")
    assert hasattr(student, "exp_grad_date")
    assert student.maximum_enrollment == 3


def test_restrictions_is_list_of_restrictions(setup_db, load_student_restrictions):
    student = load_student_restrictions
    assert type(student.restrictions) == list
    assert all([issubclass(r, Restriction) for r in student.restrictions])


def test_initial_student_state_open(setup_db, load_student_no_restrictions):
    student = load_student_no_restrictions
    assert isinstance(type(student._state), OpenStudentState)
    # TODO
    registrar = Mock()
    course_section = Mock()
    student.register_for_course(registrar, course_section)
    assert course_section in student.current_courses
    # TODO
    # Make request test


def test_student_state_restricted(setup_db, load_student_restrictions):
    student = load_student_restrictions
    assert isinstance(student._state, RestrictedStudentState)
    registrar = Mock()
    course_section = Mock()
    try:
        student.register_for_course(registrar, course_section)
    except StudentHasRestrictionsException:
        # testing correct exception
        assert True
    else:
        assert False

    policy = Mock()
    try:
        student.make_request(policy, course_section)
    except StudentHasRestrictionsException:
        assert True
    else:
        assert False


def test_student_state_full(setup_db, load_student_restrictions):
    student = load_student_full_courseload
    assert isinstance(student._state, FullCourseloadStudentState)
    registrar = Mock()
    course_section = Mock()
    try:
        student.register_for_course(registrar, course_section)
    except StudentFullCourseloadException:
        # testing correct exception
        assert True
    else:
        assert False


def test_course_history_type(setup_db, load_student_restrictions):
    # TODO after course history exists in db
    student = load_student_restrictions
    assert type(student.course_history) == list
    assert all([isinstance(c, CourseSection) for c in student.course_history])


def test_current_course_type(setup_db, load_student_restrictions):
    # TODO after course history exists in db
    student = load_student_restrictions
    assert type(student.course_current) == list
    assert all([isinstance(c, CourseSection) for c in student.course_history])


def test_current_course_changes():
    student = FullTimeStudent(Mock())
    student.current_courses = [Mock(), Mock()]
    student.add_current_course[Mock()]
    assert len(student.current_courses) == 3
    assert isinstance(student._state, FullCourseloadStudentState)
    try:
        student.add_current_course(Mock())
    except StudentFullCourseloadException:
        assert True
    else:
        assert False
