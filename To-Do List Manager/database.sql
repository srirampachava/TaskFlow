CREATE DATABASE IF NOT EXISTS student_db;

USE student_db;

-- Tasks table for ToDo app
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending'
);