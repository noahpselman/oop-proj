# from src.classes.Student import Student
# from src.classes.Instructor import Instructor
# from src.classes.TimeSlot import TimeSlot
# from src.classes.Course import Course

# from typing import List


# class CourseSection(Course):

#     @classmethod
#     def load_course_section(cls):
#         """
#         This will eventually query the db and return a
#         CourseSection constructed with the queried data

#         Returns:
#             CourseSection
#         """
#         cs = CourseSection()
#         return cs

#     def __init__(self) -> None:
#         super().__init__()
#         # TODO: make getters/setters

#         self._section_id: str = "01"
#         self._time_slot: TimeSlot = None
#         self._quarter: str = "Winter 2021"
#         self._instructors: List[Instructor] = []
#         self._lead_instructor: Instructor = None
#         self._capacity: int = 50
#         self._instructor_permission_required: bool = False
#         self._has_lab: bool = False
#         self._lab_sections: List[CourseSection] = []
#         self._roster: List(Student) = []
