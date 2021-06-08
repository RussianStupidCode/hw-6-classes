from courses.person import Person
from courses.lecturer import Lecturer


class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course):
        self.courses_in_progress.append(course)

    def finish_course(self, course):
        if course in self.courses_in_progress:
            self.courses_in_progress.remove(course)
        self.finished_courses.append(course)

    def get_average_grade(self, course=None):
        if len(self.grades.keys()) == 0:
            return 0

        if course is None:
            grades_count = sum(len(grade) for grade in self.grades.values())
            grades_sum = sum(sum(grade) for grade in self.grades.values())
            return grades_sum/grades_count
        return sum(self.grades[course]) / len(self.grades[course])

    def is_course_available(self, course):
        return course in self.courses_in_progress

    def add_grade(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]

    def rate_lecture(self, lecturer, course, lecture, grade):
        if not isinstance(lecturer, Lecturer):
            ValueError(f'lecturer не является подтипом {type(Lecturer())}')

        if not lecturer.is_lecture_exist(lecture, course) or not self.is_course_available(course):
            ValueError(f'у студента или лектора нет курса({course}) или лекции({lecture})')

        lecturer.add_grade(course, lecture, grade)

    def __str__(self):
        result = super().__str__()
        result += f'Средняя оценка за домашние задания: {self.get_average_grade()}\n'
        result += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        result += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return result

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.get_average_grade() == other.get_average_grade()
