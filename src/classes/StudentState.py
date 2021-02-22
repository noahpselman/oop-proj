from __future__ import annotations
from abc import ABC, abstractmethod
from src.classes.Exceptions import StudentFullCourseloadException, StudentHasRestrictionsException
from src.classes.CourseSection import CourseSection
# from src.classes.Student import Student


class StudentState(ABC):

    def __init__(self, student: Student) -> None:
        self.student = student

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, new_student):
        self._student = new_student

    @abstractmethod
    def register_for_course(self, registrar: Registrar, course_section: CourseSection) -> bool:
        pass

    @abstractmethod
    def make_request(self, request_policy: RequestPolicy, course_section: CourseSection) -> bool:
        """
        request refers to an overload request
        request_policy: singleton object

        """
        pass


class OpenStudentState(StudentState):

    def __init__(self, student: Student) -> None:
        super().__init__(student)

    def register_for_course(self, registrar: Registrar, course_section: course_section):
        print("register for course called from Open State")
        return registrar.register_for_course(self.student, course_section)

    def make_request(self, request_policy: RequestPolicy, course_section: CourseSection) -> bool:
        return request_policy.execute(self.student, course_section)


class RestrictedStudentState(StudentState):

    def __init__(self, student: Student) -> None:
        super().__init__(student)

    def register_for_course(self, registrar: Registrar, course_section: CourseSection):
        print("register for course called from restricted State")
        raise StudentHasRestrictionsException

    def make_request(self, request_policy: RequestPolicy, course_section: CourseSection) -> bool:
        raise StudentHasRestrictionsException


class FullCourseloadStudentState(StudentState):

    def __init__(self, student: Student) -> None:
        super().__init__(student)

    def register_for_course(self, registrar: Registrar, course_section: CourseSection):
        print("register for course called from full State")
        raise StudentFullCourseloadException

    def make_request(self, request_policy: RequestPolicy, course_section: CourseSection) -> bool:
        return request_policy.execute(self.student, course_section)
