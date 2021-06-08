from courses.mentor import Mentor
from courses.student import Student


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def is_course_valid(self, student, course):
        return course in self.courses_attached and student.is_course_available(course)

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            ValueError(f'student не является подтипом {type(Student())}')
        if self.is_course_valid(student, course):
            ValueError(f'ошибка {course} у студента не найден')

        student.add_grade(course, grade)

