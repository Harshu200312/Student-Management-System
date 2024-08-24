CREATE DATABASE Student_management1;
use Student_management1;
show tables;
CREATE TABLE Student_register (
    f_name VARCHAR(20) NOT NULL,
    l_name VARCHAR(20) NOT NULL,
    course VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    birth_date DATE NOT NULL,
    contact BIGINT NOT NULL,
    email VARCHAR(255) NOT NULL,
    prn BIGINT NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    PRIMARY KEY (contact)
);

-- adding the constraint to check email is proper formate our not
-- adding the constraint where year should not be greater than 2025
-- adding the constraint where prn no. length  shuld not be greater than 12 & mobile no. should not be greater than 10
ALTER TABLE Student_register
ADD CONSTRAINT year_check_constraint CHECK (year <= 2024),
ADD CONSTRAINT prn_chk CHECK (LENGTH(prn) = 12),
ADD CONSTRAINT contact_number CHECK (LENGTH(contact) = 10),
ADD CONSTRAINT gen_chk CHECK (gender IN ('male','female','Male','Female','other','Other')),
ADD CONSTRAINT chk_email CHECK (email LIKE '%_@__%.__%');

select * from Student_register;

INSERT INTO Student_register(f_name, l_name, course, year, birth_date, contact, email, prn, age, gender)
VALUES 
('Ruby', 'Roy', 'bscit', 2023, '2002-01-21', 1234567890, 'ruby@gmail.com', 202312345678, 22, 'Female'),
('Harshada', 'Panmand', 'bscit', 2023, '2003-01-12', 1234567899, 'harshada@gmail.com', 202312345608, 21, 'Female'),
('Bro', 'Code', 'programming', 2021, '2000-01-21', 1234567800, 'bro@gmail.com', 202312345670, 24, 'Male');


