import psycopg2 as pg
from psycopg2.extras import DictCursor
from src.classes.StudentState import RestrictedStudentState
from database.DatabaseHelper import DatabaseHelper
from database.mappers.Mapper import Mapper
from src.database.mappers.StudentMapper import StudentMapper
from src.database.Database import Database
from src.database.db_conf import db_conf
from src.classes.Restriction import LibraryRestriction, Restriction


if __name__ == "__main__":
    # try:
    # Connect to databasepip
    db_config = db_conf()
    # print(db_config)

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
    db_helper = DatabaseHelper.getInstance()
    # print(db_helper.load_user_by_id("58"))
    sm = StudentMapper("58")
    student = sm.student
    student.register_for_course()
    # print(RestrictedStudentState)
    # # print(isinstance(student._state, RestrictedStudentState))
    # print(student._state == RestrictedStudentState)

    # cur = db.conn.cursor()
    # cur.close()
    # db.conn.commit()
