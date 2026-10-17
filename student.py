
# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    student = {
        "ID": student_id,
        "Name": name
    }
    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        for student in students:
            print("ID:", student["ID"], "| Name:", student["Name"])

print("Student Management System - Develop Version")
add_student()
view_students()

def count_students():
    print("Total students:", len(students))