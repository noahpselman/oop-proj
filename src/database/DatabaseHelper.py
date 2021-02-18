
"""
handles all database requests
"""

from typing import List
from src.database.Database import Database


LOAD_STUDENT_COLUMNS = ("university_id", "expected_graduation",
                        "major", "fulltime", "maximum_enrollment", "name", "email")


class DatabaseHelper():

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if DatabaseHelper.__instance == None:
            DatabaseHelper()
        return DatabaseHelper.__instance

    def __init__(self):
        """ Virtually private constructor. """
        self._conn = None
        if DatabaseHelper.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseHelper.__instance = self
        self.db = Database.getInstance()
        if not self.db.conn:
            raise Exception("Database doesn't have connection")

    def load_student_by_id(self, university_id: str) -> dict:
        """
        queries db and formats result into dict with
        table colnames as keys and values as values
        """
        result_dict = {}
        result = self.db.load_student_by_id(university_id)
        for col in LOAD_STUDENT_COLUMNS:
            result_dict[col] = result[col]
        # print("result_dict from dbhelper", result_dict)
        return result_dict

    def load_student_restrictions(self, univeristy_id: str) -> List[str]:
        result_list = []
        result = self.db.load_student_restrictions(univeristy_id)
        print("result from db helper", result)
        for row in result:
            result_list.append(row[0])
        print("result list", result_list)
        return result_list
        # for col in LOAD_STUDENT_COLUMNS:
        #     result_dict[col] = result[col]
        # return result_dict

    def load_course_history(self, university_id: str) -> List[str]:
        """
        TODO after i put historical courses in the db
        """
        pass
