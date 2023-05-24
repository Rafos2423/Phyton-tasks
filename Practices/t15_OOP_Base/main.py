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
student1.rate_lecture(lecturer1, course2, 4)
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

student1.finish_course(course1)
student2.finish_course(course2)

# Выводим информацию о всех созданных экземплярах
print(f"Добавлен проверяющий: {reviewer1}")
print(f"Добавлен проверяющий: {reviewer2}")

print(f"Добавлен лектор: {lecturer1}")
print(f"Добавлен лектор: {lecturer2}")

print(f"Добавлен студент: {student1}")
print(f"Добавлен студент: {student2}")

print(f"Лектор ведет пары у студента: {lecturer1.__bool__(student1)}")


# Функция для подсчета средней оценки в рамках курса
# params: list: Список студентов или лекторов
def avg_grade_hw(person_list, course_name):
    grade_sum = 0
    courses = 0
    for person in person_list:
        if course_name in person.courses_in_progress:
            grade_sum += sum(map(lambda sublist: sum(sublist), person.grades.values()))
            courses += 1
    return grade_sum / courses


print(f"Средняя оценки за курс {course2} ученика {student1}: {avg_grade_hw([student1], course2)}")
print(f"Cредняя оценка за курс {course1} учеников {student1} {student2}: {avg_grade_hw([student1, student2], course1)}")

