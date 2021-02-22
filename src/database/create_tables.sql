DROP TABLE IF EXISTS department CASCADE;
DROP TABLE IF EXISTS quarter CASCADE;
DROP TABLE IF EXISTS restriction CASCADE;
DROP TABLE IF EXISTS timeslot CASCADE;
DROP TABLE IF EXISTS course CASCADE;
DROP TABLE IF EXISTS course_section CASCADE;
DROP TABLE IF EXISTS university_affiliated_person CASCADE;
DROP TABLE IF EXISTS student CASCADE;
DROP TABLE IF EXISTS student_restrictions CASCADE;
DROP TABLE IF EXISTS instructor CASCADE;

CREATE TABLE department (
    department_name varchar(4),
    PRIMARY KEY (department_name)
);

CREATE TABLE quarter (
    quarter varchar(11),
    PRIMARY KEY (quarter)
);

CREATE TABLE restriction (
    restriction varchar(30),
    PRIMARY KEY (restriction)
);

CREATE TABLE timeslot (
    id serial,
    days varchar(3) NOT NULL,
    starttime time NOT NULL,
    endtime time NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE user (
    university_id serial,
    name varchar(100) NOT NULL,
    email varchar(100) NOT NULL,
    is_student boolean NOT NULL,
    is_faculty boolean NOT NULL,
    PRIMARY KEY (university_id)
);

CREATE TABLE student (
    university_id int,
    expected_graduation varchar(11) NOT NULL,
    major varchar(4) NOT NULL,
    fulltime boolean NOT NULL DEFAULT TRUE,
    maximum_enrollment int DEFAULT 3,
    PRIMARY KEY (university_id),
    FOREIGN KEY (university_id) REFERENCES university_affiliated_person,
    FOREIGN KEY (expected_graduation) REFERENCES quarter,
    FOREIGN KEY (major) REFERENCES department
);

CREATE TABLE student_restrictions (
    university_id int,
    restriction varchar(30),
    PRIMARY KEY (university_id, restriction),
    FOREIGN KEY (restriction) REFERENCES restriction
);

CREATE TABLE instructor (
    university_id int,
    department varchar(4),
    PRIMARY KEY (university_id),
    FOREIGN KEY (university_id) REFERENCES university_affiliated_person,
    FOREIGN KEY (department) REFERENCES department
);

CREATE TABLE course (
    course_id int,
    department varchar(4),
    name varchar(120),
    PRIMARY KEY (course_id, department),
    FOREIGN KEY (department) REFERENCES department
);

CREATE TABLE course_section (
    section_number int,
    course_id int,
    department varchar(4),
    quarter varchar(11),
    timeslot int,
    PRIMARY KEY (course_id, department),
    FOREIGN KEY (course_id, department) REFERENCES course (course_id, department),
    FOREIGN KEY (department) REFERENCES department,
    FOREIGN KEY (quarter) REFERENCES quarter,
    FOREIGN KEY (timeslot) REFERENCES timeslot
);

-- TODO: quarter, restrictions, student_course link