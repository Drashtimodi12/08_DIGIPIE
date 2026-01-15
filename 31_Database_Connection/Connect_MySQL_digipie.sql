-- Step 1: Create Database and use database to make tables
create database if not exists digipie;
use digipie;

-- Step 2: Create Table
create table if not exists employee (ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(50), AGE INT, MARKS FLOAT);

-- Step 3: Insert new data into the employee table
INSERT INTO employee (NAME, AGE, MARKS) VALUES ('Drashti', 21, 7), ('Khushbu', 24, 10);

-- Step 4: To see all inserted data
select * from employee;

-- Step 5: Employees with marks > 7
select * from employee where marks > 7;

-- Step 6: Update marks
UPDATE employee SET MARKS = 9 WHERE ID = 8;

-- Step 7: Delete an Employee Record
DELETE FROM employee WHERE ID = 11;

-- Step 8: Count Total Employees 
select count(*) from employee;

-- Step 9: Find Average Marks 
select avg(MARKS) from employee;

-- Step 10: Sort Employees by Marks (Highest First)
select * from employee order by MARKS DESC;

-- Step 11: Add a New Column (e.g., City)
alter table employee add column CITY varchar(50);

-- Step 12: Update City Data
update employee SET CITY = 'Surat', STATE = 'Gujarat' where ID = 1;