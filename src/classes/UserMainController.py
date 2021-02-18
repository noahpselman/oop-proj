from typing import List
from src.classes.AddCoursesManager import AddCoursesManager
from src.classes.UniversityAffiliatedPerson import UniversityAffiliatedPerson
from src.database.Database import Database
from src.classes.CourseSection import CourseSection


class UserMainController():
    """
    Abstract
    Initiates actions on behalf to the user
    """

    def __init__(self, user: UniversityAffiliatedPerson, db: Database) -> None:
        self._user = user
        self._db = db

    @property
    def user(self):
        return self._user

    @property
    def db(self):
        return self._db


class StudentMainController(UserMainController):

    def __init__(self, user: UniversityAffiliatedPerson, db: Database) -> None:
        super().__init__(user, db)

    def register_for_course(self, course_section: CourseSection) -> bool:
        adder = AddCoursesManager()
        success = adder.add_student_to_course(self.user, course_section)
        if success:
            try:
                self.db.add_student_to_course(self.student, course_section)
            except:
                # TODO figure out how to print error
                print("coudln't add student to databse")
                print()
            finally:
                return False
        else:
            return False

    def drop_course(self, course_section: CourseSection) -> bool:
        pass

    def change_lab(self, course_section: CourseSection) -> bool:
        pass

    def view_course_history(self) -> List[CourseSection]:
        pass

    def search_for_courses(self, args: dict) -> List[CourseSection]:
        pass
