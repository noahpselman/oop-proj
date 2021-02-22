from src.database.mappers.Mapper import Mapper


class CourseSectionMapper(Mapper):

    def __init__(self, course_section_id: str) -> None:
        super().__init__()
        self.course_section = self.load(course_section_id)

    def load(self):
        # TODO
        course_section = None
        return course_section

    def save(self):
        # TODO
        pass
