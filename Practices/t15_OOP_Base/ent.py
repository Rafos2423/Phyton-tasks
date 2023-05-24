class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def rate_hw(self, student, course, grade):
        student.grades[course] = [grade]

    def __bool__(self, student):
        for course in student.courses_in_progress:
            if self.courses.__contains__(course):
                return True
        return False


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if student is Student and course in student.finished_courses and course in self.courses:
            if course in self.grades:
                self.grades[course].append(grade)

    def __str__(self):
        if len(self.grades) == 0:
            return 'нет оценок'
        avg_grade = sum(self.grades) / len(self.grades)
        return f'Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции {avg_grade:.1f}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def rate_hw(self, student, course, grade):
        if course in self.courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname}"


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []

    def add_course(self, course_name):
        self.courses_in_progress.append(course_name)

    def finish_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
            self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]

    def __float__(self):
        total_sum = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                total_sum += grade
                count += 1
        if len(count) == 0:
            return 'нет оценок'
        return total_sum / count

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(
            len(grades) for grades in self.grades.values())
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name} Фамилия: {self.surname}\nСредняя оценка за домашние задания {avg_grade:.1f} \n' \
               f'Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'
