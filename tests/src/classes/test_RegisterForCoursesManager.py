# import pytest
# from unittest.mock import Mock
# from src.classes.TimeSlot import TimeSlot
# from src.classes.Instructor import Instructor
# from src.classes.CourseSection import CourseSection
# from src.classes.Student import Student
# from src.classes.RegisterForCourseManager import RegisterForCourseManager


# @pytest.fixture
# def make_register_for_class_manager():
#     s = Student()
#     cs = CourseSection()
#     rfc_manager = RegisterForCourseManager(s, cs)
#     return rfc_manager


# # most of the testing of these method will happen in the controller
# # responsible for the tests
# def test_are_registration_conditions_met_type(make_register_for_class_manager):

#     rfc_manager = make_register_for_class_manager
#     conditions_met = rfc_manager.are_registration_conditions_met()
#     assert type(conditions_met) == bool


# def test_are_registration_conditions_met_false():

#     s = Mock()
#     cs = Mock()
#     cs.prereqs.return_value = [CourseSection()]
#     rfc_manager = RegisterForCourseManager(s, cs)
#     conditions_met = rfc_manager.are_registration_conditions_met()
#     assert not conditions_met


# def test_are_registration_conditions_met_true(make_register_for_class_manager):

#     s = Mock()
#     s.course_history.return_value = [CourseSection()]
#     cs = Mock()
#     cs.prereqs.return_value = [CourseSection()]
#     rfc_manager = RegisterForCourseManager(s, cs)
#     conditions_met = rfc_manager.are_registration_conditions_met()
#     assert conditions_met


# def test_request_instructor_permission():

#     rfc_manager = RegisterForCourseManager(Mock(), Mock())
#     requestor = Mock()
#     request_sent = rfc_manager.request_instructor_permission(requestor)
#     assert request_sent
#     requestor.request_instructor_permission.assert_called()
#     # I can call also use .call_args_list to make sure
#     # method was called with correct args


# def test_request_overload_permission():

#     rfc_manager = RegisterForCourseManager(Mock(), Mock())
#     requestor = Mock()
#     request_sent = rfc_manager.request_overload(requestor)
#     assert request_sent
#     requestor.request_overload.assert_called()
#     # I can call also use .call_args_list to make sure
#     # method was called with correct args


# def test_are_there_time_conflicts():

#     rfc_manager = RegisterForCourseManager(Mock(), Mock())
#     time_conflict_detector = Mock()
#     mock_schedule = [TimeSlot(), TimeSlot(), TimeSlot()]
#     mock_other_slot = TimeSlot()
#     result = rfc_manager.are_there_time_conflicts(time_conflict_detector,
#                                                   mock_schedule, mock_other_slot)
#     assert type(result) == bool
#     assert time_conflict_detector.check_for_conflicts.assert_called()
#     # I can call also use .call_args_list to make sure
#     # method was called with correct args


# def test_register_for_lab():
#     rfc_manager = RegisterForCourseManager(Mock(), Mock())
#     rflab_manager = Mock()
#     rfc_manager.register_for_lab(rflab_manager, s, cs)
#     rflab_manager.do_registration_process.assert_called()


# # def test_are_registration_conditions_met_true():

#     # def test_check_student_has_restrictions_false():
#     #     r = RegisterForCourseManager()
#     #     s = Student()
#     #     assert not r.test_check_student_has_restrictions(s)

#     # def test_check_student_has_restrictions_true():
#     #     s = Student()
#     #     s.add_restriction('LIBRARY')
#     #     s.add_restriction('TUITION')
#     #     r = RegisterForCourseManager()
#     #     assert r.test_check_student_has_restrictions(s)

#     # def test_check_student_has_restrictions_false_after_drop():
#     #     s = Student()
#     #     s.add_restriction('LIBRARY')
#     #     s.add_restriction('TUITION')
#     #     r = RegisterForCourseManager()
#     #     s.drop_restriction('LIBRARY')
#     #     s.drop_restriction('TUITION')
#     #     assert not r.test_check_student_has_restrictions(s)

#     # def test_check_student_meets_course_prereqs():
#     #     cs = CourseSection()
#     #     cs.add_prereq(CourseSection())
#     #     r = RegisterForCourseManager()
#     #     assert type(r.check_course_prereqs(cs)) == bool
#     #     assert not r.check_course_prereqs(cs)
#     #     s.add_course_section_to_history(Mock())
#     #     assert r.check_course_prereqs()

#     # def test_check_course_prereqs_no_prereqs(make_register_for_class_manager):
#     #     r = make_register_for_class_manager
#     #     assert r.check_course_prereqs()

#     # def test_check_instructor_permission():
#     #     s = Student()
#     #     cs = CourseSection()
#     #     cs.instructor_permission_required = False
#     #     r = RegisterForCourseManager(s, cs)
#     #     assert not r.check_instructor_permission()
#     #     cs._instructor_permission_required = True
#     #     assert r.check_course_prereqs()

#     # def test_initiate_instructor_permission_request():
#     #     """
#     #     must test
#     #         1. was a dialogue sent to the user
#     #         2. if yes, was a request entered in db
#     #         and was an email manager notified to send
#     #         the email
#     #         3. if no, did that stuff not happen
#     #     """
#     #     s = Student()
#     #     i = Instructor()
#     #     cs = CourseSection()
#     #     cs.add_instructor(i)
#     #     cs.lead_instructor = i
#     #     r = RegisterForCourseManager(s, cs)
#     #     r
#     #     r.initiate_instructor_permission_request()

#     # def test_check_overload_required():
#     #     s = Student()
#     #     cs = CourseSection()
#     #     r = RegisterForCourseManager(s, cs)
#     #     assert not r.check_overload_required()
#     #     s.add_current_course(CourseSection())
#     #     s.add_current_course(CourseSection())
#     #     s.add_current_course(CourseSection())
#     #     assert r.check_overload_required()

#     # def test_initiate_overload_request():
#     #     """
#     #     initiate_overload_request creates
#     #     """
#     #     pass
