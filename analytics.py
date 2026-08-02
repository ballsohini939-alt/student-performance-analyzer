import csv

FILE_NAME = "data/students.csv"


def load_students():

    students = []

    try:
        with open(FILE_NAME, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except FileNotFoundError:
        print("No student data found.")

    return students



def calculate_average():

    students = load_students()

    if not students:
        return 0

    total = 0

    for student in students:
        total += float(student["Percentage"])

    return total / len(students)



def top_student():

    students = load_students()

    if not students:
        return None

    return max(
        students,
        key=lambda x: float(x["Percentage"])
    )



def grade_statistics():

    students = load_students()

    grades = {}

    for student in students:

        grade = student["Grade"]

        if grade in grades:
            grades[grade] += 1
        else:
            grades[grade] = 1

    return grades