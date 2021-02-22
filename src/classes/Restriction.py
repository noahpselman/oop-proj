from abc import ABC


class Restriction():
    pass
    # @classmethod
    # def __repr__(self):
    #     return self.__name__


class LibraryRestriction(Restriction):
    pass


class TuitionRestriction(Restriction):
    pass


class AcademicAdvisorRestriction(Restriction):
    pass


class SuspensionRestriction(Restriction):
    pass


class ImmunizationRestriction(Restriction):
    pass
