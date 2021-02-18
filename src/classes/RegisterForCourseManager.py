from src.classes.Course import Course
from src.classes.CourseSection import CourseSection
from src.classes.Student import Student
from src.classes.TimeSlot import TimeSlot
from typing import List


class RegisterForCourseManager():
    """
    The purpose of this class is to manage the
    process for registering a student for a course
    """

    def __init__(self, student, course_section) -> None:

        self._student: Student = student
        self._course_section: CourseSection = course_section

    # def check_student_has_restrictions(self, course: Course) -> bool:
    #     return None

    # def check_student_meets_course_prereqs(self, student: Student, course: Course) -> bool:
    #     return None

    # def check_instructor_permission(self, course: Course) -> bool:
    #     return None

    # def initiate_instructor_permission_request(self, course_section: CourseSection) -> bool:
    #     return None

    def check_overload_required(self, student: Student) -> bool:
        return None

    def initiate_overload_request(self, student_id: str, course_section_id: str, instructor_email: str) -> bool:
        return None

    def check_for_time_conflicts(self, student_current_course_times: List[TimeSlot], course_time_slot: TimeSlot) -> bool:
        return None

    def find_alternative_time_slots(self, student_current_course_times: List[TimeSlot], course_id: str, quarter: str) -> List[CourseSection]:
        return None

    def add_student_to_course(self, student: Student, course_section: CourseSection) -> bool:
        return None

    def register_student_for_corresponding_lab(self, student: Student, course_section: CourseSection) -> bool:
        return None
