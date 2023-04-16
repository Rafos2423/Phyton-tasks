from Practices.t15_OOP_Base.ent import Lecturer, Reviewer, Student

course1 = 'Git'
course2 = 'Python'


reviewer1 = Reviewer('John', 'Smith')
reviewer2 = Reviewer('Jane', 'Doe')

lecturer1 = Lecturer('Alice', 'Wonderland')
lecturer2 = Lecturer('Bob', 'Builder')

student1 = Student('Ruoy', 'Eman')
student2 = Student('Anna', 'Karenina')

student1.add_course(course1)
student2.add_course(course2)
lecturer1.add_course(course1)
lecturer2.add_course(course2)


# Добавляем оценки лекторам от студентов
student1.rate_lecture(lecturer1, course1, 5)
student1.rate_lecture(lecturer2, course2, 4)
student2.rate_lecture(lecturer1, course2, 3)
student2.rate_lecture(lecturer2, course1, 5)

# Добавляем студентам курсы и оценки за домашние задания
student1.add_course(course2)
student1.add_course(course1)
student2.add_course(course2)
student2.add_course(course1)
student1.grades = {course2: [5, 4], course1: [4]}
student2.grades = {course2: [4, 3], course1: [5]}

# Выводим информацию о всех созданных экземплярах
print(reviewer1)
print(reviewer2)

print(lecturer1)
print(lecturer2)

print(student1)
print(student2)


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def avg_grade_hw(students_list, course_name):
    grades = []
    for student in students_list:
        if course_name in student.grades:
            grades.extend(student.grades[course_name])
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0


print(avg_grade_hw([student1, student2], course2))
print(avg_grade_hw([student1, student2], course1))


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def avg_grade_lecturers(lecturers_list, course_name):
    grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.courses:
            grades.extend(lecturer.grades)
    if len(grades) != 0:
        return sum(grades) / len(grades)
    else:
        return 0