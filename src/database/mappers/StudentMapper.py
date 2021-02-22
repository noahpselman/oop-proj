from typing import List
from src.classes.Restriction import AcademicAdvisorRestriction, ImmunizationRestriction, LibraryRestriction, SuspensionRestriction, TuitionRestriction
from src.classes.User import User
from src.database.mappers.Mapper import Mapper
from src.classes.Student import FullTimeStudent, PartTimeStudent, Student
from src.database.DatabaseHelper import DatabaseHelper

"""
Kind of like a factory but only from db
Also can load in chunks - not sure if this
will be useful
"""


# this will eventually find somewhere else to live
RESTRICTION_MAPPER = {
    "LIBRARY": LibraryRestriction,
    "ACADEMIC ADVISOR": AcademicAdvisorRestriction,
    "TUITION": TuitionRestriction,
    "SUSPENSION": SuspensionRestriction,
    "IMMUNIZATION": ImmunizationRestriction
}


class StudentMapper(Mapper):

    def __init__(self, university_id: str) -> None:

        super().__init__()

        self.student = self.load(university_id)

    def load(self, university_id: str):
        # print(self.db_helper)
        user_data = self.db_helper.load_user_by_id(university_id)
        student_data = self.db_helper.load_student_by_id(university_id)
        user = User(user_data['university_id'],
                    user_data['name'], user_data['email'])

        if student_data['fulltime']:
            student = FullTimeStudent(user)
        else:
            student = PartTimeStudent(user)

        student.exp_grad_date = student_data['expected_graduation']
        student.major = student_data['major']

        restrictions = self.db_helper.load_student_restrictions(university_id)

        restrictions = [RESTRICTION_MAPPER[r] for r in restrictions]
        student.restrictions = restrictions

        return student

        # TODO
        # load course history
        # load restrictiosn
        # if

    def save(self):
        pass


# old implementation before I started using mappers
# class StudentMapper(Mapper):
#     """
#     Builds Student in chunks from DB
#     """

#     def __init__(self, student=None, university_id=None):

#         self.db_helper = DatabaseHelper.getInstance()
#         if student:
#             self.student = student

#         elif university_id:
#             self.student = self.load_student_by_id(university_id)

#         else:
#             # this isn't a feature of this build - i just have a catch all
#             print("Oh no - it wasn't in the database")
#             id = self.create_new_student_in_db()
#             self.student = Student(id)

#     def create_new_student_in_db(self) -> str:
#         """
#         not a feature of prototype
#         """
#         pass

#     def load_student_by_id(self, university_id: str) -> Student:
#         """
#         queries db for student by ID then creates student object
#         """
#         student_data = self.db_helper.load_student_by_id(university_id)
#         print("student_data", student_data)
#         s = Student(str(student_data["university_id"]), student_data["name"])
#         s.email = student_data['email']
#         s.exp_grad_date = student_data['expected_graduation']
#         s.student_type = "full-time" if student_data["fulltime"] else "part-time"
#         s.major = student_data["major"]
#         s.maximum_enrollment = student_data["maximum_enrollment"]
#         print("student from student builder", s)
#         return s

#     def load_student_restrictions(self) -> None:

#         self.student.restrictions = self.db_helper.load_student_restrictions(
#             self.student.uid)

#     def load_course_history(self) -> List[str]:
#         """
#         will return list of course ids, not full objects
#         that is all that is needed
#         """
#         self.db_helper.load_student_course_history(self.student.university_id)

#     def update(self):
#         """
#         StudentLoader will be a subscriber to the registrar
#         Registrar will notify student when it needs to be updated
#         """
#         self.load_course_history()
