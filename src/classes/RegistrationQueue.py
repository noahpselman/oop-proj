from __future__ import annotations


class RegistrationQueue():
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if RegistrationQueue.__instance == None:
            RegistrationQueue()
        return RegistrationQueue.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if RegistrationQueue.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            RegistrationQueue.__instance = self
        self._queue = {}
        self.subscribers = []

    def add(self, reg: RegistrationObject):
        course_section = reg.course_section
        self._queue[course_section] += self._queue.get(
            course_section, []) + [reg]

    def get(self, course_section: CourseSection):
        course_queue = self._queue.get(course_id, None)
        if course_queue:
            self._queue[course_section] = course_queue[1:]
            return course_queue[0]

    def go(self):
        while True:
            for course_section in self._queue:
                if not course_section.is_full:
                    reg = self.get(course_section)
                    reg.execute()
