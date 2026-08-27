import csv


STUDENTS_FILE = "data/students.csv"
SUBJECT_MARKS_FILE = "data/subject_marks.csv"
STUDY_HOURS_FILE = "data/study_hours.csv"


def load_students():

    students = []

    try:

        with open(
            STUDENTS_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                students.append(row)

    except FileNotFoundError:

        print(
            "No student data found."
        )

    return students


def load_subject_marks():

    subjects = []

    try:

        with open(
            SUBJECT_MARKS_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                subjects.append(row)

    except FileNotFoundError:

        print(
            "No subject marks data found."
        )

    return subjects


def load_study_hours():

    study_data = []

    try:

        with open(
            STUDY_HOURS_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                study_data.append(row)

    except FileNotFoundError:

        print(
            "No study hour data found."
        )

    return study_data


def calculate_average():

    students = load_students()

    if not students:
        return 0

    total = 0

    for student in students:

        total += float(
            student["Percentage"]
        )

    return total / len(students)


def top_student():

    students = load_students()

    if not students:
        return None

    return max(
        students,
        key=lambda x:
        float(x["Percentage"])
    )


def lowest_student():

    students = load_students()

    if not students:
        return None

    return min(
        students,
        key=lambda x:
        float(x["Percentage"])
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


def average_study_hours():

    study_data = load_study_hours()

    if not study_data:
        return 0

    total_hours = 0

    for student in study_data:

        total_hours += float(
            student["StudyHours"]
        )

    return (
        total_hours
        / len(study_data)
    )


def highest_study_hours():

    study_data = load_study_hours()

    if not study_data:
        return None

    return max(
        study_data,
        key=lambda x:
        float(x["StudyHours"])
    )


def lowest_study_hours():

    study_data = load_study_hours()

    if not study_data:
        return None

    return min(
        study_data,
        key=lambda x:
        float(x["StudyHours"])
    )


def study_performance_analysis():

    students = load_students()

    study_data = load_study_hours()

    if not students or not study_data:
        return []

    performance_map = {}

    for student in students:

        performance_map[
            student["Name"].lower()
        ] = float(
            student["Percentage"]
        )

    results = []

    for study in study_data:

        name = study["Name"]

        percentage = performance_map.get(
            name.lower()
        )

        if percentage is not None:

            results.append({
                "Name": name,
                "StudyHours":
                    float(
                        study["StudyHours"]
                    ),
                "Percentage":
                    percentage
            })

    return results


def performance_category(
    percentage
):

    if percentage >= 90:

        return "Excellent"

    elif percentage >= 75:

        return "Good"

    elif percentage >= 60:

        return "Average"

    else:

        return "Needs Attention"


def performance_categories():

    students = load_students()

    categories = {
        "Excellent": 0,
        "Good": 0,
        "Average": 0,
        "Needs Attention": 0
    }

    for student in students:

        percentage = float(
            student["Percentage"]
        )

        category = performance_category(
            percentage
        )

        categories[category] += 1

    return categories


def subject_statistics():

    subject_data = load_subject_marks()

    if not subject_data:
        return {}

    subject_totals = {}

    subject_counts = {}

    for record in subject_data:

        subject = record["Subject"]

        marks = float(
            record["Marks"]
        )

        if subject not in subject_totals:

            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] += marks

        subject_counts[subject] += 1

    statistics = {}

    for subject in subject_totals:

        statistics[subject] = (
            subject_totals[subject]
            / subject_counts[subject]
        )

    return statistics


def strongest_subject():

    statistics = subject_statistics()

    if not statistics:
        return None

    return max(
        statistics,
        key=statistics.get
    )


def weakest_subject():

    statistics = subject_statistics()

    if not statistics:
        return None

    return min(
        statistics,
        key=statistics.get
    )


def learning_insight():

    data = study_performance_analysis()

    if len(data) < 2:

        return (
            "More student data is needed "
            "to compare learning patterns."
        )

    average_hours = (
        sum(
            student["StudyHours"]
            for student in data
        )
        / len(data)
    )

    high_study_students = [
        student
        for student in data
        if student["StudyHours"]
        >= average_hours
    ]

    low_study_students = [
        student
        for student in data
        if student["StudyHours"]
        < average_hours
    ]

    if (
        not high_study_students
        or not low_study_students
    ):

        return (
            "More varied study-hour data "
            "is needed to compare "
            "learning patterns."
        )

    high_average = (
        sum(
            student["Percentage"]
            for student
            in high_study_students
        )
        / len(high_study_students)
    )

    low_average = (
        sum(
            student["Percentage"]
            for student
            in low_study_students
        )
        / len(low_study_students)
    )

    difference = abs(
        high_average
        - low_average
    )

    if high_average > low_average:

        return (
            f"Students studying at or above "
            f"the average study time scored "
            f"about {difference:.2f} percentage "
            f"points higher on average. "
            f"This shows an association in "
            f"the current sample, not causation."
        )

    elif low_average > high_average:

        return (
            f"Students studying below the "
            f"average study time scored about "
            f"{difference:.2f} percentage points "
            f"higher on average. More data is "
            f"needed before drawing conclusions."
        )

    else:

        return (
            "Students with higher and lower "
            "study hours have similar average "
            "performance in the current sample."
        )


def generate_recommendations():

    students = load_students()

    recommendations = {}

    if not students:
        return recommendations

    subject_data = load_subject_marks()

    subject_map = {}

    for record in subject_data:

        name = record["Name"]

        subject = record["Subject"]

        marks = float(
            record["Marks"]
        )

        if name not in subject_map:

            subject_map[name] = []

        subject_map[name].append(
            (subject, marks)
        )

    for student in students:

        name = student["Name"]

        percentage = float(
            student["Percentage"]
        )

        student_recommendations = []

        if percentage < 60:

            student_recommendations.append(
                "Focus on improving overall "
                "academic performance."
            )

        elif percentage < 75:

            student_recommendations.append(
                "Strengthen your fundamentals "
                "and practice regularly."
            )

        elif percentage < 90:

            student_recommendations.append(
                "Good performance. Continue "
                "practicing to reach the "
                "excellent category."
            )

        else:

            student_recommendations.append(
                "Excellent performance. Maintain "
                "your current study routine."
            )

        if name in subject_map:

            weak_subjects = [
                subject
                for subject, marks
                in subject_map[name]
                if marks < 60
            ]

            if weak_subjects:

                student_recommendations.append(
                    "Give additional attention to: "
                    + ", ".join(
                        weak_subjects
                    )
                    + "."
                )

        recommendations[name] = (
            student_recommendations
        )

    return recommendations


def dataset_summary():

    students = load_students()

    if not students:
        return None

    percentages = [
        float(student["Percentage"])
        for student in students
    ]

    study_data = load_study_hours()

    return {
        "total_students":
            len(students),

        "students_with_study_data":
            len(study_data),

        "average_percentage":
            sum(percentages)
            / len(percentages),

        "highest_percentage":
            max(percentages),

        "lowest_percentage":
            min(percentages),

        "average_study_hours":
            average_study_hours()
    }