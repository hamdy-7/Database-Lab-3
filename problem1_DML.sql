USE company;

INSERT INTO DEPARTMENT (Dnumber, Dname, mgr_ssn, mgr_start_date) VALUES 
(1, 'Software', NULL, '2023-01-01'),
(2, 'HR', NULL, '2023-02-01'),
(3, 'Finance', NULL, '2023-03-01');

INSERT INTO EMPLOYEE (ssn, fname, lname, bdate, address, gender, salary, Dno) VALUES 
(101, 'Hamdy', 'Mabrouk', '2005-11-01', 'Alexandria', 'M', 15000.00, 1),
(102, 'Kareem', 'Emara', '2004-11-07', 'Cairo', 'M', 12000.00, 2),
(103, 'Mazen', 'Ibrahim', '2005-03-14', 'Alexandria', 'M', 13500.00, 3);

UPDATE DEPARTMENT SET mgr_ssn = 101 WHERE Dnumber = 1;
UPDATE DEPARTMENT SET mgr_ssn = 102 WHERE Dnumber = 2;
UPDATE DEPARTMENT SET mgr_ssn = 103 WHERE Dnumber = 3;

INSERT INTO PROJECT (Pnumber, Pname, Plocation, Dno) VALUES 
(10, 'AI Assistant', 'Alexandria', 1),
(20, 'Recruitment App', 'Cairo', 2),
(30, 'Payroll System', 'Alexandria', 3);