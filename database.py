import sqlite3

conn = sqlite3.connect("datab.db")
cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name NAME,
    instructor TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_course (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id),
    PRIMARY KEY(student_id, course_id)
)
""")

conn.commit()
