from courses.student import Student
from courses.lecturer import Lecturer
from courses.reviewer import Reviewer


def get_student_average_grade(students, course):
    grade_sum = sum(student.get_grade_sum(course) for student in students)
    grade_count = sum(student.get_grade_count(course) for student in students)
    return grade_sum / grade_count


def get_lecture_average_grade(lecturers, course):
    grade_sum = sum(lecturer.get_grade_sum(course) for lecturer in lecturers)
    grade_count = sum(lecturer.get_grade_count(course) for lecturer in lecturers)
    return grade_sum / grade_count


def student_test():
    course = 'Python'
    student_1 = Student('Ruoy', 'Eman', 'your_gender')
    student_1.add_course(course)
    student_2 = Student('Harry', 'Potter', 'your_gender')
    student_2.add_course(course)

    cool_mentor = Reviewer('Олег', 'Булыгин')
    cool_mentor.add_course(course)

    cool_mentor.rate_hw(student_1, course, 10)
    cool_mentor.rate_hw(student_1, course, 5)
    cool_mentor.rate_hw(student_1, course, 10)

    cool_mentor.rate_hw(student_2, course, 10)

    print(get_student_average_grade([student_2, student_1], course))
    print(student_1)
    print(student_1 == student_2)


def lecturers_test():
    course = 'JavaScript'
    lecture = 'Basic'
    lecturer_1 = Lecturer('Jotaro', 'Kujo')
    lecturer_1.add_lecture(course, lecture)
    lecturer_2 = Lecturer('Joseph', 'Joestar')
    lecturer_2.add_lecture(course, lecture)

    student_1 = Student('giorno', 'giovanna', 'Jojo')
    student_1.add_course(course)
    student_1.rate_lecture(lecturer_1, course, lecture, 1)
    student_1.rate_lecture(lecturer_1, course, lecture, 1)
    student_1.rate_lecture(lecturer_1, course, lecture, 1)
    student_1.rate_lecture(lecturer_2, course, lecture, 2)

    print(lecturer_1)
    print(lecturer_1.grades)
    print(lecturer_2.get_average_grade(course))
    print(lecturer_1.get_average_grade(course))
    print(get_lecture_average_grade([lecturer_2, lecturer_1], course))


if __name__ == '__main__':
    student_test()
    lecturers_test()

