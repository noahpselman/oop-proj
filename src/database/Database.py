import psycopg2


class Database:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):
        """ Virtually private constructor. """
        self._conn = None
        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, new_conn):
        self._conn = new_conn

    def load_user_by_id(self, university_id):
        query = """
        SELECT university_id, name, email
        FROM university_affiliated_person
        WHERE university_id = %s
        """
        return self.fetch_one(query, (university_id,))

    def load_student_by_id(self, university_id):
        query = """
        SELECT  *
        FROM student
        WHERE university_id = %s

        """
        return self.fetch_one(query, (university_id,))
        # cur = self.conn.cursor()
        # cur.execute(query, (university_id,))
        # return cur.fetchone()

    def fetch_one(self, query, args):
        cur = self.conn.cursor()
        cur.execute(query, args)
        return cur.fetchone()

    def load_student_restrictions(self, university_id):
        query = """
        SELECT restriction FROM student_restrictions
        WHERE university_id = %s
        """
        cur = self.conn.cursor()
        cur.execute(query, (university_id,))
        return cur.fetchall()


STUDENT_TABLE_NAMES = {
    "STUDENT_TABLE_NAME": "student",
    "STUDENT_PK": "university_id",
    "STUDENT_COLUMN_EXPECTED_GRADUATION": "expected_graduation",
    "STUDENT_COLUMN_MAJOR": "major",
    "STUDENT_COLUMN_FULLTIME": "maximum_enrollment"
}
