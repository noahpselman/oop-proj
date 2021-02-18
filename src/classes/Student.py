from src.classes.UniversityAffiliatedPerson import UniversityAffiliatedPerson


class Student(UniversityAffiliatedPerson):

    def __init__(self, university_id: str, name: str) -> None:
        super().__init__(university_id, name)

        self._exp_grad_date: str = None
        self._student_type: str = None
        self._major: str = None
        self._maximum_enrollment = None
        self._course_history = []
        self._restrictions = []

        # course history could be stored as a list of
        # strings of course_ids or course participation
        # objects - will need to weigh the pros/cons

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
    def maximum_enrollment(self):
        return self._maximum_enrollment

    @maximum_enrollment.setter
    def maximum_enrollment(self, new_maximum_enrollment):
        self._maximum_enrollment = new_maximum_enrollment
    # def register_for_course(self, adder: AddCoursesManager, course_section: CourseSection):
    #     adder.add_student_to_course(self, course_section)

    @property
    def restrictions(self):
        return self._restrictions

    @restrictions.setter
    def restrictions(self, new_restrictions):
        self._restrictions = new_restrictions

    @property
    def course_history(self):
        return self._course_history

    @course_history.setter
    def course_history(self, new_course_history):
        self._course_history = new_course_history
