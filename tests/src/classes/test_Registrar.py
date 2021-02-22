import pytest
from unittest.mock import Mock

from classes.Registrar import Registrar


def test_register_student_for_course():
    registrar = Registrar()
    student = Mock()
    course_section = Mock()
    result = Registrar.add_student_to_course(student, course_section)
    assert type(result) == bool
