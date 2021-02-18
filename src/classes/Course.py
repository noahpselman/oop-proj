from typing import List


class Course():
    """
    Abstract Class
    """

    def __init__(self) -> None:
        self._course_id: str = "12345"
        self._dept: str = "MATH"
        # print(self.__form_course_name())
        self._course_name: str = self.__form_course_name()
        self._prereqs: List[str] = []
        self._lab: Course = None

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, new_course_id):
        self._course_id = new_course_id
        self._course_name: str = self.__form_course_name()

    @property
    def dept(self):
        return self._dept

    @dept.setter
    def dept(self, new_dept):
        self._dept = new_dept
        self._course_name: str = self.__form_course_name()

    @property
    def prereqs(self) -> List[str]:
        return self._prereqs

    def add_prereq(self, new_prereq: str) -> None:
        self.prereqs.append(new_prereq)

    def remove_prereq(self, to_remove: str) -> None:
        self.prereqs.remove(to_remove)

    @property
    def course_name(self):
        return self._course_name

    def __form_course_name(self) -> str:
        # print(self.dept + self.course_id)
        return self.dept + self.course_id
