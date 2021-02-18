from src.classes.Student import Student
import pytest


def test_student_has_attr_from_superclass():
    student = Student()
    assert hasattr(student, "uid")
    assert hasattr(student, "full_name")
    assert hasattr(student, "email")


def test_student_has_expected_graduation():
    student = Student()
    assert hasattr(student, "exp_grad_date")
    assert type(student.exp_grad_date) == str


def test_student_has_student_type():
    student = Student()
    assert hasattr(student, "student_type")
    assert student.student_type in ("full-time", "part-time")


def test_load_restrictions_returns_list():
    student = Student()
    student.load_restrictions()
    assert type(student.restrictions) == list


def test_load_restrictions_returns_list_of_restrictions():
    """
    testing to make sure restrictions are of correct type
    for now using an enum but maybe it would be better
    to hold types of restrictions in the db and make sure
    that the student restrictions match that list
    """

    student = Student()
    student.load_restrictions()
    assert all([type(r) == Restriction for r in student.restrictions])


def test_load_course_history_returns_list():
    student = Student()
    student.load_course_history()
    assert type(student.course_history) == list


def test_load_course_history_returns_list_of_course_id():
    student = Student()
    student.load_course_history()
    assert all([type(ch) == str for ch in student.course_history])


def test_load_current_courses_returns_list():
    student = Student()
    student.test_load_current_courses_returns_list()
    assert type(student.current_courses == list)


def test_load_current_courses_returns_course_sectiion():
    student = Student()
    student.load_course_history()
    assert all([type(cc) == CourseSection for cc in student.current_courses])
