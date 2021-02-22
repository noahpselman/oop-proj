from __future__ import annotations


class RegistrationObject():

    def __init__(self, registrar: Registrar, student: Student, course_section: CourseSection) -> None:
        self.registrar = registrar
        self.student = student
        self.course_section = course_section

    def execute(self):
        pass

    def validate(self, policies: List[RegistrationPolicy]):
        for policy in policies:
            is_valid = policy.validate(self.student, self.course_section)
            if not is_valid:
                policy.on_fail(self.student, self.course_section)
