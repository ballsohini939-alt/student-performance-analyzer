class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks

    def total_marks(self):
        return sum(self.subjects.values())

    def percentage(self):
        return self.total_marks() / len(self.subjects)

    def highest_subject(self):
        return max(self.subjects, key=self.subjects.get)

    def lowest_subject(self):
        return min(self.subjects, key=self.subjects.get)