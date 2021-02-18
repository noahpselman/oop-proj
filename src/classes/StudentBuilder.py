from typing import List
from src.classes.Student import Student
from src.database.DatabaseHelper import DatabaseHelper

"""
StudentBuilder seems to need to know a lot about the
interface of db but I don't know a cleaner way to do it
"""


class StudentBuilder():
    """
    Builds Student in chunks from DB
    """

    def __init__(self, student=None, university_id=None):

        self.db_helper = DatabaseHelper.getInstance()
        if student:
            self.student = student

        elif university_id:
            self.student = self.load_student_by_id(university_id)

        else:
            # this isn't a feature of this build - i just have a catch all
            print("Oh no - it wasn't in the database")
            id = self.create_new_student_in_db()
            self.student = Student(id)

    def create_new_student_in_db(self) -> str:
        """
        not a feature of prototype
        """
        pass

    def load_student_by_id(self, university_id: str) -> Student:
        """
        queries db for student by ID then creates student object
        """
        student_data = self.db_helper.load_student_by_id(university_id)
        print("student_data", student_data)
        s = Student(str(student_data["university_id"]), student_data["name"])
        s.email = student_data['email']
        s.exp_grad_date = student_data['expected_graduation']
        s.student_type = "full-time" if student_data["fulltime"] else "part-time"
        s.major = student_data["major"]
        s.maximum_enrollment = student_data["maximum_enrollment"]
        print("student from student builder", s)
        return s

    def load_student_restrictions(self) -> None:

        self.student.restrictions = self.db_helper.load_student_restrictions(
            self.student.uid)

    def load_course_history(self) -> List[str]:
        """
        will return list of course ids, not full objects
        that is all that is needed
        """
        self.db_helper.load_student_course_history(self.student.university_id)
