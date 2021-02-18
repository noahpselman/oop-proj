from typing import List
# from src.classes.CourseSection import CourseSection
from src.classes.Student import Student


class AddCoursesManager:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AddCoursesManager.__instance == None:
            AddCoursesManager()
        return AddCoursesManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if AddCoursesManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AddCoursesManager.__instance = self

    def add_student_to_course(self, student: Student, course_section: CourseSection, requirement_checkers: List[RequirementChecker]):
        """
        checks to make sure adding requirments are met
        """
        if self.check_eligibility(student, course_section, requirement_checkers):
            pass
            # add student

    def check_eligibility(self, student, course_section, requirement_checkers):
        for checker in requirement_checkers:
            if not checker.check_eligibility(student, course_section):
                checker.on_fail(student)
                return False
