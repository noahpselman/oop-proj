from __future__ import annotations


class Registrar():
    def __init__(self) -> None:
        self.queue = RegistrationQueue.getInstance()

    def register_student_for_course(self, student: Student, course_section: CourseSection):
        reg = RegistrationObject(self, student, course_section)
        return self.add_to_queue(reg)

    def add_student_to_queue(self, student_id: str, course_id: str):
        self.queue.add(student_id, course_id)

    def drop_student_from_course(self, student: Student, course_section: CourseSection):
        return course_section.remove_student(student)
