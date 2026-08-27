import csv
import os

FILE_NAME = "data/students.csv"
SUBJECT_FILE_NAME = "data/subject_marks.csv"


def save_student(student, grade):
    # Save student summary
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["Name", "Total", "Percentage", "Grade"])

        writer.writerow([
            student.name,
            student.total_marks(),
            f"{student.percentage():.2f}",
            grade
        ])

    # Save subject-wise marks
    subject_file_exists = os.path.isfile(SUBJECT_FILE_NAME)

    with open(SUBJECT_FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not subject_file_exists or os.path.getsize(SUBJECT_FILE_NAME) == 0:
            writer.writerow(["Name", "Subject", "Marks"])

        for subject, marks in student.subjects.items():
            writer.writerow([
                student.name,
                subject,
                f"{marks:.2f}"
            ])


def view_students():
    if not os.path.exists(FILE_NAME):
        print("\nNo student records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n========== STUDENT RECORDS ==========")

        for row in reader:
            print(" | ".join(row))

        print("=====================================\n")


def search_student(name):
    if not os.path.exists(FILE_NAME):
        print("\nNo student records found.\n")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Name"].lower() == name.lower():
                print("\nStudent Found")
                print("---------------------------")
                print(f"Name       : {row['Name']}")
                print(f"Total      : {row['Total']}")
                print(f"Percentage : {row['Percentage']}")
                print(f"Grade      : {row['Grade']}")

                found = True
                break

    if not found:
        print("\nStudent not found.\n")