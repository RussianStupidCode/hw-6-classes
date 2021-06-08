from courses.person import Person


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def add_course(self, course):
        self.courses_attached.append(course)
