class Student:
    def __init__(self, name):
        name = name.strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        self.name = name
        self.subjects = {}

    def add_subject(self, subject, marks):
        subject = subject.strip()

        if not subject:
            raise ValueError("Subject name cannot be empty.")

        if subject in self.subjects:
            raise ValueError(f"Subject '{subject}' already exists.")

        if not isinstance(marks, (int, float)):
            raise ValueError("Marks must be a number.")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

        self.subjects[subject] = marks

    def total_marks(self):
        return sum(self.subjects.values())

    def percentage(self):
        if not self.subjects:
            return 0

        return self.total_marks() / len(self.subjects)

    def highest_subject(self):
        if not self.subjects:
            return None

        return max(self.subjects, key=self.subjects.get)

    def lowest_subject(self):
        if not self.subjects:
            return None

        return min(self.subjects, key=self.subjects.get)