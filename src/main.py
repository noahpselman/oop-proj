import psycopg2 as pg
from psycopg2.extras import DictCursor
import os
from classes.StudentBuilder import StudentBuilder
from src.database.Database import Database
from src.database.db_conf import db_conf


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
    # print(db.conn)
    sb = StudentBuilder(university_id="58")
    sb.load_student_restrictions()
    print(sb.student.restrictions)

    # cur = db.conn.cursor()
    # cur.close()
    # db.conn.commit()
