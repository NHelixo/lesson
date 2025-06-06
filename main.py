import sqlite3

conn = sqlite3.connect("datab.db")
cursor = conn.cursor()

def add_student():
    name = input("Ім'я студента: ")
    age = int(input("Вік: "))
    major = input("Спеціальність: ")
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    conn.commit()
    print("Студент доданий!")

def add_course():
    name = input("Ім'я студента: ")
    instructor = input("Викладач: ")
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", (name, instructor))
    conn.commit()
    print("Курс доданий")

def register_student_to_course():
    student_id = int(input(" ID студента: "))
    course_id = int(input("ID курсу: "))
    cursor.execute("INSERT INTO student_course (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    conn.commit()
    print("Студент зареєстрований на курс!")

def list_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def list_courses():
    cursor.execute("SELECT * FROM courses")
    for row in cursor.fetchall():
        print(row)

def students_in_course():
    course_id = int(input("Введіть ID курсу: "))
    cursor.execute("""
        SELECT students.id, students.name, students.age, students.major 
        FROM students
        JOIN student_course ON students.id = student_course.student_id
        WHERE student_course.course_id = ?
    """, (course_id,))
    students = cursor.fetchall()

    cursor.execute("SELECT course_name FROM courses WHERE course_id = ?", (course_id,))
    course_name = cursor.fetchone()

    if course_name:
        print(f"\nСтуденти на курсі '{course_name[0]}':")
        for student in students:
            print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")
    else:
        print("Курс не знайдено.")

def main_menu():
    while True:
        print("1 - Меню")
        print("2 - Додати студента")
        print("3 - Додати курс")
        print("4 - Зареєструвати студента на курс")
        print("5 - Показати всіх студентів")
        print("6 - Показати всі курси")
        print("7 - Показати студентів для конкретного курсу")
        print("0 - Вихід")

        choice = input("Оберіть опцію (1-7): ")

        if choice == "1":
            pass

        elif choice == "2":
            add_student()

        elif choice == "3":
            add_course()

        elif choice == "4":
            register_student_to_course()

        elif choice == "5":
            list_students()

        elif choice == "6":
            list_courses()

        elif choice == "7":
            students_in_course()

        elif choice == "0":
            break

        else:
            print("Некоректний вибір!")

    conn.close()

if __name__ == "__main__":
    main_menu()