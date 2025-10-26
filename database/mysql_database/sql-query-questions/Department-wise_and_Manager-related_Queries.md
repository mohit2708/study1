### 🧠 **Common Department-wise & Manager-related Queries**
```sql
-- Create departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

-- Create employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department_id INT,
    manager_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- Insert data into departments
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Engineering'),
(3, 'HR'),
(4, 'Finance');

-- Insert data into employees
INSERT INTO employees (employee_id, name, department_id, manager_id, salary) VALUES
(101, 'Alice', 1, NULL, 90000),    -- Alice is manager of Sales
(102, 'Bob', 1, 101, 60000),
(103, 'Charlie', 1, 101, 65000),

(201, 'David', 2, NULL, 120000),   -- David is manager of Engineering
(202, 'Eve', 2, 201, 80000),
(203, 'Frank', 2, 201, 85000),
(204, 'Grace', 2, 201, 78000),

(301, 'Heidi', 3, NULL, 95000),    -- Heidi is manager of HR
(302, 'Ivan', 3, 301, 55000),

(401, 'Judy', 4, NULL, 105000);    -- Judy is manager of Finance
```


<div style="page-break-before: always;"></div>

#### 📌 **List all employees department-wise**
```sql
SELECT d.department_name, e.employee_id, e.name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.name;
```

#### 📌 **Count number of employees in each department**
```sql
SELECT d.department_name, COUNT(*) AS employee_count
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
```

#### 📌 **Find the manager of each employee (show employee and their manager name)**
```sql
SELECT e.name AS employee_name, m.name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;
```

#### 📌 **List all managers and their direct reports (employees reporting to them)**
```sql
-- if we using left join then show the all emp which have no mgr.
SELECT e.name AS employee_name, m.name AS manager_name
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
ORDER BY m.name;
```

#### 📌 **Count how many employees report to each manager**
```sql
SELECT m.name AS manager_name, COUNT(e.employee_id) AS emp_count
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
GROUP BY m.employee_id;
```

#### 📌 **Find the highest-paid employee in each department**
```sql
SELECT d.department_name, e.name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary = (
    SELECT MAX(salary) 
    FROM employees 
    WHERE department_id = d.department_id
);
```

#### 📌 **Show all departments along with their managers (assuming one manager per department)**
```sql
SELECT d.department_name, m.name AS manager_name
FROM departments d
JOIN employees m ON d.department_id = m.department_id
WHERE m.employee_id IN (
    SELECT DISTINCT manager_id FROM employees WHERE manager_id IS NOT NULL
);
```

#### 📌 **Find departments without any employees**
```sql
SELECT d.department_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
WHERE e.employee_id IS NULL;
```