import csv
import os


FILE_NAME = "data/students.csv"
SUBJECT_FILE_NAME = "data/subject_marks.csv"
STUDY_HOURS_FILE = "data/study_hours.csv"


def save_student(student, grade):
    """
    Save or update a student's performance record.
    Prevents duplicate student records.
    """

    students = []

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    student_found = False

    for row in students:

        if row["Name"].lower() == student.name.lower():

            row["Name"] = student.name
            row["Total"] = f"{student.total_marks():.2f}"
            row["Percentage"] = f"{student.percentage():.2f}"
            row["Grade"] = grade

            student_found = True
            break

    if not student_found:

        students.append({
            "Name": student.name,
            "Total": f"{student.total_marks():.2f}",
            "Percentage": f"{student.percentage():.2f}",
            "Grade": grade
        })

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = [
            "Name",
            "Total",
            "Percentage",
            "Grade"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(students)

    save_subject_marks(student)


def save_subject_marks(student):
    """
    Save or update subject-wise marks
    for a student.
    """

    records = []

    if os.path.exists(SUBJECT_FILE_NAME):

        with open(
            SUBJECT_FILE_NAME,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                records.append(row)

    # Remove old subject records for this student

    records = [
        row
        for row in records
        if row["Name"].lower()
        != student.name.lower()
    ]

    # Add latest subject records

    for subject, marks in student.subjects.items():

        records.append({
            "Name": student.name,
            "Subject": subject,
            "Marks": f"{marks:.2f}"
        })

    with open(
        SUBJECT_FILE_NAME,
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "Name",
            "Subject",
            "Marks"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(records)


def save_study_hours(name, study_hours):
    """
    Save or update study hours.
    Prevents duplicate study-hour records.
    """

    records = []

    if os.path.exists(STUDY_HOURS_FILE):

        with open(
            STUDY_HOURS_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                records.append(row)

    student_found = False

    for row in records:

        if row["Name"].lower() == name.lower():

            row["Name"] = name
            row["StudyHours"] = f"{study_hours:.2f}"

            student_found = True
            break

    if not student_found:

        records.append({
            "Name": name,
            "StudyHours": f"{study_hours:.2f}"
        })

    with open(
        STUDY_HOURS_FILE,
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "Name",
            "StudyHours"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(records)


def view_students():
    """
    Display all student records.
    """

    if not os.path.exists(FILE_NAME):

        print(
            "\nNo student records found.\n"
        )

        return

    with open(
        FILE_NAME,
        "r",
        newline=""
    ) as file:

        reader = csv.reader(file)

        print(
            "\n========== STUDENT RECORDS =========="
        )

        for row in reader:

            print(
                " | ".join(row)
            )

        print(
            "=====================================\n"
        )


def search_student(name):
    """
    Search for a student by name.
    """

    if not os.path.exists(FILE_NAME):

        print(
            "\nNo student records found.\n"
        )

        return

    found = False

    with open(
        FILE_NAME,
        "r",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Name"].lower() == name.lower():

                print(
                    "\nStudent Found"
                )

                print(
                    "---------------------------"
                )

                print(
                    f"Name       : {row['Name']}"
                )

                print(
                    f"Total      : {row['Total']}"
                )

                print(
                    f"Percentage : {row['Percentage']}"
                )

                print(
                    f"Grade      : {row['Grade']}"
                )

                found = True

                break

    if not found:

        print(
            "\nStudent not found.\n"
        )