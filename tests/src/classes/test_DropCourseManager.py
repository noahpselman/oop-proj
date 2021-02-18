import pytest
from unittest.mock import Mock
from src.classes.CourseSection import CourseSection


def test_drop_student_from_course_success():
    student_id = '12345678'
    course_id = 'MATH12345'
    drop_student_manager = Mock()
    cs = CourseSection()
    cs.course_id = Mock(return_value=course_id)
    cs.roster = Mock(return_value=[student_id])
    is_successful = drop_student_manager.drop_student_from_course(
        student_id, course_id)
    assert is_successful and student_id not in cs.roster


def test_drop_student_from_course_fail():
    student_id = '12345678'
    course_id = 'MATH12345'
    drop_student_manager = Mock()
    cs = CourseSection()
    cs.course_id = Mock(return_value=course_id)
    cs.roster = Mock(return_value=[student_id])
    # do something to make it so the drop doesn't work
    is_successful = drop_student_manager.drop_student_from_course(
        student_id, course_id)
    assert not is_successful and student_id in cs.roster
