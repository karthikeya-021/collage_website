CREATE DATABASE college_db;Add commentMore actions
USE college_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    password VARCHAR(100),
    roll_number VARCHAR(20),
    department VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO students (name, password, roll_number, department, email)
VALUES ('ganapathi', '1234', 'CSE001', 'CSE', 'john@example.com');

CREATE TABLE marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(50),
    mark INT
);

INSERT INTO marks (student_id, subject, mark)
VALUES (1, 'Math', 85), (1, 'Physics', 90);

CREATE TABLE fees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    total INT,
    paid INT,
    balance INT
);

INSERT INTO fees (student_id, total, paid, balance)
VALUES (1, 50000, 30000, 20000);