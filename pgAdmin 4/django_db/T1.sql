CREATE TABLE if not exists employee(
	id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

CREATE TABLE if not exists department(
	id SERIAL PRIMARY KEY,
	dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE employee_profile(
	id SERIAL PRIMARY KEY, 
	employee_id INT REFERENCES employee(id) ON DELETE CASCADE,
	address TEXT,
	phone VARCHAR(15)
);