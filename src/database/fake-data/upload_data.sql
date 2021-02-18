-- DEPARTMENTS
\COPY department(department_name) FROM 'departments.csv' DELIMITER ',';

-- QUARTER
\COPY quarter(quarter) FROM 'quarter.csv' DELIMITER ',';

-- TIMESLOT
\COPY timeslot(days, starttime, endtime) FROM 'timeslot.csv' DELIMITER ',';

-- RESTRICTIONS
\COPY restriction(restriction) FROM 'restrictions.csv' DELIMITER ',';

-- UNIVERSITY AFFILIATED PERSON
\COPY university_affiliated_person(name, email, is_faculty, is_student) FROM 'UAP.csv' DELIMITER ',';

-- STUDENT
\COPY student(university_id, expected_graduation, major, fulltime, maximum_enrollment) FROM 'students.csv' DELIMITER ',';

-- STUDENT RESTRICTIONS
\COPY student_restrictions(university_id, restriction) FROM 'student_restriction.csv' DELIMITER ',';

-- INTRUCTORS
\COPY instructor(university_id, department) FROM 'instructor.csv' DELIMITER ',';

-- COURSE
\COPY course(name, course_id, department) FROM 'courses.csv' DELIMITER ',';