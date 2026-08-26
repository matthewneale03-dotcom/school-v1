class Student:
    def __init__(self, first_name, surname, dob, gender):
        self.student_first_name = first_name
        self.student_surname = surname
        self.student_dob = dob
        self.student_gender = gender

class Classroom:
    def __init__(self, title):
        self.class_title = title
        self.students = []

    def add_student(self, first_name, surname, dob, gender):
        self.students.append(Student(first_name, surname, dob, gender))

    def find_student(self, dob):
        for student in self.students:
            if student.student_dob == dob:
                return student
        return None