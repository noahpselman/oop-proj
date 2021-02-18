from src.constants.Grades import GRADES


class StudentCourseParticipation():

    def __init__(self, student_id: str, course_id: str) -> None:
        self._student_id: str = student_id
        self._course_id: str = course_id
        self._grade: str = None

    @property
    def student_id(self) -> str:
        print("student_id getter called")
        return self._student_id

    @property
    def course_id(self) -> str:
        print("course_id getter called")
        return self._course_id

    @property
    def grade(self) -> str:
        print("grade getter called boiiiii")
        return self._grade

    @grade.setter
    def grade(self, new_grade: str) -> str:
        print("grade setter called boiiiii")
        if new_grade not in GRADES:
            raise ValueError("That is not a valid grade")
        self._grade = new_grade


# if __name__ == "__main__":
#     scp = StudentCourseParticipation("99999999", "MATH1234")
#     print(scp.student_id)
#     print(scp.course_id)
#     print(scp.grade)
#     # scp.grade = 5
#     scp.grade = "B"
#     print(scp.grade)
