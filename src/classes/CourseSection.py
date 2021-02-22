from __future__ import annotations
from typing import List
from src.classes.Exceptions import CourseSectionFullExcetion
# from src.classes.Student import Student
from src.classes.Instructor import Instructor
from src.classes.TimeSlot import TimeSlot
from src.classes.Course import Course
from src.classes.Quarter import Quarter


class CourseSection(Course):

    def __init__(self, course_id: str, dept: str, course_name: str, section_id: str, quarter: Quarter) -> None:
        super().__init__(course_id, dept, course_name)

        self._section_id: str = section_id
        self._quarter: Quarter = quarter
        self._course_designation = self.__create_course_designation()
        self._time_slot: TimeSlot = None
        self._instructors: List[Instructor] = []
        self._lead_instructor: Instructor = None
        self._capacity: int = 0
        self._roster: List[Student] = []
        self._is_full: bool = len(self.roster) >= self.capacity
        self._instructor_permission_required: bool = False
        self._lab_sections: List[CourseSection] = []
        self._auditors: List[Student] = []

    def __create_course_designation(self):
        return "".join([self.course_name, "/", self.section_id, " ", self.quarter.name])

    @property
    def course_designation(self):
        return self._course_designation

    @property
    def section_id(self):
        return self._section_id

    @property
    def time_slot(self):
        return self._time_slot

    @property
    def quarter(self):
        return self._quarter

    @property
    def instructors(self):
        return self._instructor

    @instructors.setter
    def instructors(self, new_instructors):
        self._instructors = new_instructors

    def add_instructor(self, instructor: Instructor):
        instructors = self.instructors
        instructor.append(instructor)
        self.instructors = instructors

    @property
    def lead_instructor(self):
        return self._lead_instructor

    @lead_instructor.setter
    def lead_instructor(self, new_lead_instructor):
        self._lead_instructor = new_lead_instructor

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        self._capacity = new_capacity
        self.check_is_full()

    @property
    def roster(self):
        return self._roster

    @roster.setter
    def roster(self, new_roster):
        self._roster = new_roster

    def add_student_to_roster(self, student: Student):
        if self.is_full:
            raise CourseSectionFullExcetion
        else:
            roster = self.roster
            roster.append(student)
            self.roster = roster
            self.check_is_full()

    def check_is_full(self):
        self._is_full = len(self.roster) >= self.capacity

    @property
    def auditors(self):
        return self._auditors

    def add_student_to_auditors(self, student: Student):
        auditors = self.auditors
        auditors.append(student)
        self.auditors = auditors

    @property
    def is_full(self):
        return self._is_full

    @property
    def instructor_permission_required(self):
        return self._instructor_permission_required

    @property
    def lab_sections(self):
        return self._lab_sections
