from courses.mentor import Mentor


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures = {}
        self.grades = {}

    def add_lecture(self, course, lecture):
        super().add_course(course)
        self.lectures[course] = [lecture]

    def get_average_grade(self, course=None):
        if len(self.grades.keys()) == 0:
            return 0

        grades_sum = 0
        grades_count = 0

        if course is None:
            for grades in self.grades.values():
                grades_sum += sum(sum(grade) for grade in grades.values())
                grades_count += sum(len(grade) for grade in grades.values())
        else:
            grades_sum = sum(sum(grade) for grade in self.grades[course].values())
            grades_count = sum(len(grade) for grade in self.grades[course].values())
        return grades_sum / grades_count

    def is_lecture_exist(self, lecture, course):
        if course not in self.lectures or lecture not in self.lectures[course]:
            return False
        return True

    def add_grade(self, course, lecture, grade):
        if course not in self.grades:
            self.grades[course] = {}
        if lecture in self.grades[course]:
            self.grades[course][lecture].append(grade)
        else:
            self.grades[course][lecture] = [grade]

    def __str__(self):
        result = super().__str__()
        result += f'Средняя оценка за лекции: {self.get_average_grade()}\n'
        return result

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()
