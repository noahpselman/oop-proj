from __future__ import annotations
from typing import List
from src.classes.CourseSection import CourseSection
from src.classes.Restriction import Restriction
from src.classes.StudentState import *
from src.classes.User import User


class Student():

    # def __init__(self, university_id: str, name: str) -> None:
    #     super().__init__(university_id, name)

    def __init__(self, user_data: User):
        self._state = OpenStudentState(self)
        self.user_data: User = user_data
        self._exp_grad_date: str = None
        self._major: str = None
        self._course_history = []
        self._restrictions: List[Restriction] = []
        self._current_courses = []
        # self.transition_to(OpenStudentState(self))

    # course history could be stored as a list of
    # strings of course_ids or course participation
    # objects - will need to weigh the pros/cons

    def transition_to(self, state: StudentState):
        self._state = state(self)

    @property
    def exp_grad_date(self) -> str:
        print("getter called")
        return self._exp_grad_date

    @exp_grad_date.setter
    def exp_grad_date(self, new_exp_grad_date: str) -> None:
        print("setter called")
        self._exp_grad_date = new_exp_grad_date

    @property
    def student_type(self) -> str:
        return self._student_type

    @student_type.setter
    def student_type(self, new_student_type) -> None:
        assert new_student_type in ("full-time", "part-time")
        if new_student_type == "full-time":
            self.maximum_enrollment = 3
        elif new_student_type == "part-time":
            self.maximum_enrollment = 2
        self._student_type = new_student_type

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, new_major):
        """
        TODO check major is a department
        """
        self._major = new_major

    @property
    def restrictions(self):
        return self._restrictions

    @restrictions.setter
    def restrictions(self, new_restrictions):
        self._restrictions = new_restrictions
        if self.restrictions:
            self.transition_to(RestrictedStudentState)

    @property
    def course_history(self):
        return self._course_history

    @course_history.setter
    def course_history(self, new_course_history):
        self._course_history = new_course_history

    @property
    def current_courses(self):
        return self._current_courses

    @current_courses.setter
    def current_courses(self, new_current_courses):
        self._current_courses = new_current_courses
        if len(self.current_courses) >= self.maximum_enrollment:
            self.transition_to(FullCourseloadStudentState())

    def add_current_course(self, new_current_course):
        curr_courses = self.current_courses
        if len(curr_courses) >= self.maximum_enrollment:
            raise StudentFullCourseloadException
        curr_courses.append(new_current_course)
        self.current_courses = curr_courses

    def register_for_course(self, registrar: Registrar, course_section: CourseSection):
        return self._state.register_for_course(registrar, course_section)

    def make_request(self, request_policy: RequestPolicy, course_section: CourseSection):
        return self._state.make_request(request_policy, course_section)


class FullTimeStudent(Student):

    def __init__(self, user_data):
        super().__init__(user_data)

        self._maximum_enrollment = 3

    @property
    def maximum_enrollment(self):
        return self._maximum_enrollment

    @maximum_enrollment.setter
    def maximum_enrollment(self, new_maximum_enrollment):
        self._maximum_enrollment = new_maximum_enrollment


class PartTimeStudent(Student):
    def __init__(self, user_data):
        super().__init__(user_data)

        self._maximum_enrollment = 2

    @property
    def maximum_enrollment(self):
        return self._maximum_enrollment

    @maximum_enrollment.setter
    def maximum_enrollment(self, new_maximum_enrollment):
        self._maximum_enrollment = new_maximum_enrollment
