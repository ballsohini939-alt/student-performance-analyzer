import csv


def load_students():
    """Load student performance data from CSV."""

    try:
        with open("data/students.csv", "r") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        return []


def load_subject_marks():
    """Load subject-wise marks from CSV."""

    try:
        with open("data/subject_marks.csv", "r") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        return []


def find_student(students, name):
    """Find a student by name."""

    for student in students:
        if student["Name"].strip().lower() == name.strip().lower():
            return student

    return None


def get_student_subjects(subject_data, student_name):
    """Get subject marks for a particular student."""

    subjects = {}

    for row in subject_data:

        if row["Name"].strip().lower() == student_name.strip().lower():

            subjects[row["Subject"]] = float(row["Marks"])

    return subjects


def calculate_total_marks(subjects):
    """Calculate total marks from subject marks."""

    return sum(subjects.values())


def compare_students():
    """Compare the academic performance of two students."""

    students = load_students()

    if not students:
        print("\nNo student data available.")
        return

    print("\n" + "=" * 60)
    print("                 STUDENT COMPARISON")
    print("=" * 60)

    name1 = input("\nEnter first student name: ").strip()
    name2 = input("Enter second student name: ").strip()

    student1 = find_student(students, name1)
    student2 = find_student(students, name2)

    if not student1:
        print(f"\nStudent '{name1}' was not found.")
        return

    if not student2:
        print(f"\nStudent '{name2}' was not found.")
        return

    if student1["Name"].strip().lower() == student2["Name"].strip().lower():
        print("\nPlease select two different students.")
        return

    percentage1 = float(student1["Percentage"])
    percentage2 = float(student2["Percentage"])

    # --------------------------------------------------
    # Load subject data
    # --------------------------------------------------

    subject_data = load_subject_marks()

    subjects1 = get_student_subjects(
        subject_data,
        student1["Name"]
    )

    subjects2 = get_student_subjects(
        subject_data,
        student2["Name"]
    )

    total1 = calculate_total_marks(subjects1)
    total2 = calculate_total_marks(subjects2)

    # --------------------------------------------------
    # Academic Performance
    # --------------------------------------------------

    print("\n" + "-" * 60)
    print("ACADEMIC PERFORMANCE")
    print("-" * 60)

    print(
        f"{'':20}"
        f"{student1['Name']:<20}"
        f"{student2['Name']:<20}"
    )

    print(
        f"{'Total Marks':20}"
        f"{total1:<20.2f}"
        f"{total2:<20.2f}"
    )

    print(
        f"{'Percentage':20}"
        f"{percentage1:<20.2f}"
        f"{percentage2:<20.2f}"
    )

    print(
        f"{'Grade':20}"
        f"{student1['Grade']:<20}"
        f"{student2['Grade']:<20}"
    )

    # --------------------------------------------------
    # Determine higher performer
    # --------------------------------------------------

    print("\n" + "-" * 60)
    print("COMPARISON RESULT")
    print("-" * 60)

    difference = abs(percentage1 - percentage2)

    if percentage1 > percentage2:

        print(
            f"Higher Performer : {student1['Name']}"
        )

    elif percentage2 > percentage1:

        print(
            f"Higher Performer : {student2['Name']}"
        )

    else:

        print(
            "Result            : Both students have equal performance."
        )

    print(
        f"Score Difference  : "
        f"{difference:.2f} percentage points"
    )

    # --------------------------------------------------
    # Subject comparison
    # --------------------------------------------------

    print("\n" + "-" * 60)
    print("SUBJECT-WISE COMPARISON")
    print("-" * 60)

    common_subjects = sorted(
        set(subjects1.keys()) & set(subjects2.keys())
    )

    if common_subjects:

        print(
            f"{'Subject':20}"
            f"{student1['Name']:<20}"
            f"{student2['Name']:<20}"
        )

        print("-" * 60)

        for subject in common_subjects:

            mark1 = subjects1[subject]
            mark2 = subjects2[subject]

            print(
                f"{subject:<20}"
                f"{mark1:<20.2f}"
                f"{mark2:<20.2f}"
            )

    else:

        print("No common subject data available.")

    # --------------------------------------------------
    # Subject Insights
    # --------------------------------------------------

    print("\n" + "-" * 60)
    print("SUBJECT INSIGHTS")
    print("-" * 60)

    if subjects1:

        strongest1 = max(
            subjects1,
            key=subjects1.get
        )

        weakest1 = min(
            subjects1,
            key=subjects1.get
        )

        print(
            f"{student1['Name']} strongest subject : "
            f"{strongest1} ({subjects1[strongest1]:.2f})"
        )

        print(
            f"{student1['Name']} weakest subject   : "
            f"{weakest1} ({subjects1[weakest1]:.2f})"
        )

    if subjects2:

        strongest2 = max(
            subjects2,
            key=subjects2.get
        )

        weakest2 = min(
            subjects2,
            key=subjects2.get
        )

        print(
            f"{student2['Name']} strongest subject : "
            f"{strongest2} ({subjects2[strongest2]:.2f})"
        )

        print(
            f"{student2['Name']} weakest subject   : "
            f"{weakest2} ({subjects2[weakest2]:.2f})"
        )

    # --------------------------------------------------
    # Subject-by-subject winner
    # --------------------------------------------------

    if common_subjects:

        print("\n" + "-" * 60)
        print("SUBJECT WINNERS")
        print("-" * 60)

        for subject in common_subjects:

            mark1 = subjects1[subject]
            mark2 = subjects2[subject]

            if mark1 > mark2:

                print(
                    f"{subject:<15}: "
                    f"{student1['Name']} "
                    f"(+{mark1 - mark2:.2f})"
                )

            elif mark2 > mark1:

                print(
                    f"{subject:<15}: "
                    f"{student2['Name']} "
                    f"(+{mark2 - mark1:.2f})"
                )

            else:

                print(
                    f"{subject:<15}: Equal performance"
                )

    # --------------------------------------------------
    # Overall Insight
    # --------------------------------------------------

    print("\n" + "-" * 60)
    print("COMPARISON INSIGHT")
    print("-" * 60)

    if percentage1 > percentage2:

        print(
            f"{student1['Name']} is currently performing "
            f"better overall by "
            f"{difference:.2f} percentage points."
        )

        print(
            f"{student2['Name']} can focus on improving "
            "weaker subjects and maintaining regular practice."
        )

    elif percentage2 > percentage1:

        print(
            f"{student2['Name']} is currently performing "
            f"better overall by "
            f"{difference:.2f} percentage points."
        )

        print(
            f"{student1['Name']} can focus on improving "
            "weaker subjects and maintaining regular practice."
        )

    else:

        print(
            "Both students have the same overall percentage."
        )

        print(
            "Both students should continue improving "
            "their weaker subjects."
        )

    print("\n" + "=" * 60)