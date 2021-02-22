from _pytest.fixtures import fixture
import psycopg2 as pg
from psycopg2.extras import DictCursor
import pytest
from unittest.mock import Mock
from src.classes.CourseSection import CourseSection
from src.classes.Student import Student
from src.database.mappers.StudentMapper import StudentMapper
from src.database.Database import Database
from src.database.db_conf import db_conf


@pytest.fixture
def setup_db():
    db_config = db_conf()

    try:
        connection = pg.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port'],
            cursor_factory=DictCursor
        )
    except KeyError as e:

        print("Unable to connect to the databse with db_config")
        raise

    db = Database.getInstance()
    db.conn = connection

    return db


@pytest.fixture
def load_student_restrictions():

    mapper = StudentMapper("58")
    student = mapper.student
    return student


@pytest.fixture
def load_student_no_restrictions():

    mapper = StudentMapper("100")
    student = mapper.student
    return student


@pytest.fixture
def load_student_full_courseload():
    """
    TODO
    implement after course sections
    input into the db
    """
    return None


@pytest.fixture
def fake_course_section():
    quarter = Mock()
    quarter.name = "Winter 2021"
    cs = CourseSection("12345", "MATH", "Calculus", "01", quarter)
    return cs
