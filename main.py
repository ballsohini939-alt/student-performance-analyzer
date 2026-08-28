
from student import Student
from analyzer import calculate_grade

from utils import (
    save_student,
    view_students,
    search_student
)

from analytics import (
    calculate_average,
    top_student,
    grade_statistics
)

from data_analysis import (
    pandas_class_statistics,
    pandas_grade_distribution,
    pandas_student_ranking,
    pandas_subject_statistics,
    pandas_study_statistics,
    pandas_performance_categories,
    pandas_top_student,
    pandas_lowest_student,
    pandas_study_performance,
    pandas_correlation
)

from visualizations import (
    show_student_performance_chart,
    show_subject_performance_chart,
    show_grade_distribution_chart,
    show_performance_categories_chart,
    show_study_hours_vs_performance
)

from student_profile import get_student_profile

from performance_comparison import compare_students

from class_dashboard import display_class_dashboard

from performance_trend import performance_trend_menu


# ============================================================
# ADD / UPDATE STUDENT
# ============================================================

def add_student():
    """
    Add a new student or update an existing student.

    Stores academic performance, subject marks,
    and study hours.
    """

    print("\n========== ADD / UPDATE STUDENT ==========")

    # --------------------------------------------------------
    # Student Name
    # --------------------------------------------------------

    while True:

        name = input(
            "Enter student name: "
        ).strip()

        if name:
            break

        print(
            "Student name cannot be empty."
        )

    student = Student(name)

    # --------------------------------------------------------
    # Number of Subjects
    # --------------------------------------------------------

    while True:

        try:

            number = int(
                input(
                    "Enter number of subjects: "
                )
            )

            if number > 0:
                break

            print(
                "Please enter at least one subject."
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )

    # --------------------------------------------------------
    # Subject-wise Marks
    # --------------------------------------------------------

    print("\nEnter subject-wise marks:")

    for i in range(number):

        while True:

            subject = input(
                f"\nEnter subject {i + 1} name: "
            ).strip()

            if not subject:

                print(
                    "Subject name cannot be empty."
                )

                continue

            break

        while True:

            try:

                marks = float(
                    input(
                        f"Enter marks for {subject}: "
                    )
                )

                if 0 <= marks <= 100:

                    student.add_subject(
                        subject,
                        marks
                    )

                    break

                print(
                    "Marks must be between "
                    "0 and 100."
                )

            except ValueError:

                print(
                    "Please enter a valid number."
                )

    # --------------------------------------------------------
    # Performance Calculation
    # --------------------------------------------------------

    total = student.total_marks()

    percentage = student.percentage()

    grade = calculate_grade(
        percentage
    )

    # --------------------------------------------------------
    # Performance Report
    # --------------------------------------------------------

    print(
        "\n========== PERFORMANCE REPORT =========="
    )

    print(
        f"Student Name : {student.name}"
    )

    print(
        f"Total Marks  : {total:.2f}"
    )

    print(
        f"Percentage   : {percentage:.2f}%"
    )

    print(
        f"Grade        : {grade}"
    )

    print(
        f"Highest      : "
        f"{student.highest_subject()}"
    )

    print(
        f"Lowest       : "
        f"{student.lowest_subject()}"
    )

    print("\nSubject-wise Marks")

    print("-" * 30)

    for subject, marks in student.subjects.items():

        print(
            f"{subject:<15}"
            f"{marks:.2f}"
        )

    # --------------------------------------------------------
    # Study Hours
    # --------------------------------------------------------

    print(
        "\n========== LEARNING HABITS =========="
    )

    while True:

        try:

            study_hours = float(
                input(
                    "Enter average study hours per day: "
                )
            )

            if study_hours < 0:

                print(
                    "Study hours cannot be negative."
                )

                continue

            break

        except ValueError:

            print(
                "Please enter a valid number."
            )

    # --------------------------------------------------------
    # Save Data
    # --------------------------------------------------------

    save_student(
        student,
        grade,
        study_hours
    )

    print(
        "\nStudent record saved/updated successfully!"
    )

    print(
        "Academic data and study habits "
        "are synchronized."
    )


# ============================================================
# MAIN MENU
# ============================================================

def show_menu():
    """
    Display the main application menu.
    """

    print("\n" + "=" * 40)

    print(
        "     STUDENT PERFORMANCE ANALYZER"
    )

    print("=" * 40)

    print("1. Add Student")

    print("2. View All Students")

    print("3. Search Student")

    print("4. Student Profile")

    print("5. Student Comparison")

    print("6. Class Performance Dashboard")

    print("7. Performance Trend")

    print("8. View Analytics")

    print("9. Pandas Data Analysis")

    print("10. Data Visualizations")

    print("11. Exit")


# ============================================================
# PERSONALIZED LEARNING RECOMMENDATIONS
# ============================================================

def display_learning_recommendations():
    """
    Display personalized learning recommendations
    based on student performance.
    """

    students = []

    try:

        import csv

        with open(
            "data/students.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                students.append(row)

    except FileNotFoundError:

        print(
            "\nNo student data available."
        )

        return

    if not students:

        print(
            "\nNo student data available."
        )

        return

    print(
        "\nPersonalized Learning Recommendations"
    )

    print("-" * 40)

    for student in students:

        name = student["Name"]

        percentage = float(
            student["Percentage"]
        )

        print(
            f"\n{name}:"
        )

        if percentage >= 90:

            print(
                "  • Excellent performance. "
                "Maintain your current study routine "
                "and continue challenging yourself."
            )

        elif percentage >= 70:

            print(
                "  • Good performance. "
                "Continue practicing to reach "
                "the excellent category."
            )

        elif percentage >= 50:

            print(
                "  • Average performance. "
                "Focus on weak subjects and "
                "increase regular practice."
            )

        else:

            print(
                "  • Focus on improving overall "
                "academic performance."
            )


# ============================================================
# ADVANCED ANALYTICS
# ============================================================

def view_analytics():
    """
    Display advanced academic and learning analytics.
    """

    print(
        "\n========== ADVANCED ANALYTICS =========="
    )

    # --------------------------------------------------------
    # Load Student Data
    # --------------------------------------------------------

    try:

        import csv

        with open(
            "data/students.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            students = list(reader)

    except FileNotFoundError:

        students = []

    # --------------------------------------------------------
    # Dataset Summary
    # --------------------------------------------------------

    print("\nDataset Summary")

    print("-" * 28)

    if students:

        percentages = [
            float(student["Percentage"])
            for student in students
        ]

        print(
            f"Total Students          : "
            f"{len(students)}"
        )

        print(
            f"Average Percentage      : "
            f"{sum(percentages) / len(percentages):.2f}%"
        )

        print(
            f"Highest Percentage      : "
            f"{max(percentages):.2f}%"
        )

        print(
            f"Lowest Percentage       : "
            f"{min(percentages):.2f}%"
        )

    else:

        print(
            "No student data available."
        )

    # --------------------------------------------------------
    # Study Hours Summary
    # --------------------------------------------------------

    try:

        with open(
            "data/study_hours.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            study_data = list(reader)

    except FileNotFoundError:

        study_data = []

    print(
        f"Students With Study Data: "
        f"{len(study_data)}"
    )

    if study_data:

        hours = [
            float(row["StudyHours"])
            for row in study_data
        ]

        print(
            f"Average Study Hours     : "
            f"{sum(hours) / len(hours):.2f} hours/day"
        )

    else:

        print(
            "Average Study Hours     : "
            "No data"
        )

    # --------------------------------------------------------
    # Class Average
    # --------------------------------------------------------

    print("\nClass Average")

    print("-" * 28)

    average = calculate_average()

    print(
        f"{average:.2f}%"
    )

    # --------------------------------------------------------
    # Top Student
    # --------------------------------------------------------

    top = top_student()

    print("\nTop Performing Student")

    print("-" * 28)

    if top:

        print(
            f"Name       : {top['Name']}"
        )

        print(
            f"Percentage : "
            f"{float(top['Percentage']):.2f}%"
        )

        print(
            f"Grade      : {top['Grade']}"
        )

    else:

        print(
            "No student data available."
        )

    # --------------------------------------------------------
    # Student Needing Attention
    # --------------------------------------------------------

    if students:

        lowest = min(
            students,
            key=lambda x: float(
                x["Percentage"]
            )
        )

        print(
            "\nStudent Needing Most Attention"
        )

        print("-" * 28)

        print(
            f"Name       : {lowest['Name']}"
        )

        print(
            f"Percentage : "
            f"{float(lowest['Percentage']):.2f}%"
        )

        print(
            f"Grade      : {lowest['Grade']}"
        )

    # --------------------------------------------------------
    # Grade Statistics
    # --------------------------------------------------------

    grades = grade_statistics()

    print("\nGrade Statistics")

    print("-" * 28)

    if grades:

        for grade, count in grades.items():

            print(
                f"{grade}: "
                f"{count} student(s)"
            )

    else:

        print(
            "No grade data available."
        )

    # --------------------------------------------------------
    # Performance Categories
    # --------------------------------------------------------

    print("\nPerformance Categories")

    print("-" * 28)

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

        if percentage >= 90:

            categories["Excellent"] += 1

        elif percentage >= 70:

            categories["Good"] += 1

        elif percentage >= 50:

            categories["Average"] += 1

        else:

            categories["Needs Attention"] += 1

    for category, count in categories.items():

        print(
            f"{category}: "
            f"{count} student(s)"
        )

    # --------------------------------------------------------
    # Subject Performance
    # --------------------------------------------------------

    try:

        with open(
            "data/subject_marks.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            subject_data = list(reader)

    except FileNotFoundError:

        subject_data = []

    subject_averages = {}

    for row in subject_data:

        subject = row["Subject"]

        marks = float(
            row["Marks"]
        )

        if subject not in subject_averages:

            subject_averages[subject] = []

        subject_averages[subject].append(
            marks
        )

    print("\nSubject Performance")

    print("-" * 28)

    for subject in sorted(
        subject_averages
    ):

        average_marks = (
            sum(
                subject_averages[subject]
            )
            /
            len(
                subject_averages[subject]
            )
        )

        print(
            f"{subject:<15}"
            f"Average: "
            f"{average_marks:.2f}%"
        )

    if subject_averages:

        subject_average_values = {
            subject:
            sum(marks) / len(marks)
            for subject, marks
            in subject_averages.items()
        }

        strongest = max(
            subject_average_values,
            key=subject_average_values.get
        )

        weakest = min(
            subject_average_values,
            key=subject_average_values.get
        )

        print(
            f"\nStrongest Subject : "
            f"{strongest}"
        )

        print(
            f"Weakest Subject   : "
            f"{weakest}"
        )

    # --------------------------------------------------------
    # Learning Habits
    # --------------------------------------------------------

    print("\nLearning Habits")

    print("-" * 28)

    if study_data:

        study_hours = {
            row["Name"]:
            float(row["StudyHours"])
            for row in study_data
        }

        average_hours = (
            sum(study_hours.values())
            /
            len(study_hours)
        )

        highest_name = max(
            study_hours,
            key=study_hours.get
        )

        lowest_name = min(
            study_hours,
            key=study_hours.get
        )

        print(
            f"Average Study Hours : "
            f"{average_hours:.2f} hours/day"
        )

        print(
            f"Highest Study Time  : "
            f"{highest_name} "
            f"({study_hours[highest_name]:.2f} "
            f"hours/day)"
        )

        print(
            f"Lowest Study Time   : "
            f"{lowest_name} "
            f"({study_hours[lowest_name]:.2f} "
            f"hours/day)"
        )

        # ----------------------------------------------------
        # Study vs Performance
        # ----------------------------------------------------

        print(
            "\nStudy Hours vs Performance"
        )

        print("-" * 28)

        student_percentages = {
            student["Name"]:
            float(student["Percentage"])
            for student in students
        }

        matching_data = []

        for name, hours_value in study_hours.items():

            if name in student_percentages:

                matching_data.append(
                    (
                        name,
                        hours_value,
                        student_percentages[name]
                    )
                )

                print(
                    f"{name:<12}"
                    f"Study: "
                    f"{hours_value:.2f} hrs/day   "
                    f"Score: "
                    f"{student_percentages[name]:.2f}%"
                )

        # ----------------------------------------------------
        # Learning Insight
        # ----------------------------------------------------

        print("\nLearning Insight")

        print("-" * 28)

        if len(matching_data) >= 2:

            above_average = [
                score
                for name, hours_value, score
                in matching_data
                if hours_value >= average_hours
            ]

            below_average = [
                score
                for name, hours_value, score
                in matching_data
                if hours_value < average_hours
            ]

            if above_average and below_average:

                above_score = (
                    sum(above_average)
                    /
                    len(above_average)
                )

                below_score = (
                    sum(below_average)
                    /
                    len(below_average)
                )

                difference = (
                    above_score
                    -
                    below_score
                )

                if difference > 0:

                    print(
                        "Students studying at or "
                        "above the average study "
                        "time scored about "
                        f"{difference:.2f} "
                        "percentage points higher "
                        "on average."
                    )

                    print(
                        "This shows an association "
                        "in the current sample, "
                        "not causation."
                    )

                else:

                    print(
                        "Students studying at or "
                        "above the average study "
                        "time did not score higher "
                        "on average in the current "
                        "sample."
                    )

            else:

                print(
                    "More student data is needed "
                    "to compare learning patterns."
                )

        else:

            print(
                "More student data is needed "
                "to compare learning patterns."
            )

    else:

        print(
            "No study-hour data available."
        )

    # --------------------------------------------------------
    # Personalized Recommendations
    # --------------------------------------------------------

    display_learning_recommendations()

    print(
        "\n=========================================="
    )


# ============================================================
# PANDAS DATA ANALYSIS
# ============================================================

def view_pandas_analysis():
    """
    Display Pandas-based data analysis.
    """

    print(
        "\n========== PANDAS DATA ANALYSIS =========="
    )

    # --------------------------------------------------------
    # Statistical Summary
    # --------------------------------------------------------

    statistics = pandas_class_statistics()

    print("\nStatistical Summary")

    print("-" * 35)

    if not statistics:

        print(
            "No student data available."
        )

        return

    print(
        f"Total Students : "
        f"{statistics['total_students']}"
    )

    print(
        f"Mean           : "
        f"{float(statistics['average_percentage']):.2f}%"
    )

    print(
        f"Median         : "
        f"{float(statistics['median_percentage']):.2f}%"
    )

    print(
        f"Highest        : "
        f"{float(statistics['highest_percentage']):.2f}%"
    )

    print(
        f"Lowest         : "
        f"{float(statistics['lowest_percentage']):.2f}%"
    )

    # --------------------------------------------------------
    # Student Ranking
    # --------------------------------------------------------

    ranking = pandas_student_ranking()

    print("\nStudent Ranking")

    print("-" * 55)

    if not ranking.empty:

        print(
            f"{'Rank':<8}"
            f"{'Name':<15}"
            f"{'Percentage':<15}"
            f"{'Grade':<8}"
        )

        print("-" * 55)

        for _, row in ranking.iterrows():

            print(
                f"{int(row['Rank']):<8}"
                f"{str(row['Name']):<15}"
                f"{float(row['Percentage']):<15.2f}"
                f"{str(row['Grade']):<8}"
            )

    # --------------------------------------------------------
    # Grade Distribution
    # --------------------------------------------------------

    grades = pandas_grade_distribution()

    print("\nGrade Distribution")

    print("-" * 35)

    if grades:

        for grade, count in grades.items():

            print(
                f"{grade}: "
                f"{count} student(s)"
            )

    else:

        print(
            "No grade data available."
        )

    # --------------------------------------------------------
    # Performance Categories
    # --------------------------------------------------------

    categories = pandas_performance_categories()

    print("\nPerformance Categories")

    print("-" * 35)

    if categories:

        for category, count in categories.items():

            print(
                f"{category}: "
                f"{count} student(s)"
            )

    # --------------------------------------------------------
    # Subject Statistics
    # --------------------------------------------------------

    subjects = pandas_subject_statistics()

    print("\nSubject Statistics")

    print("-" * 70)

    if not subjects.empty:

        print(
            f"{'Subject':<15}"
            f"{'Average':<15}"
            f"{'Highest':<15}"
            f"{'Lowest':<15}"
            f"{'Students':<10}"
        )

        print("-" * 70)

        for _, row in subjects.iterrows():

            print(
                f"{str(row['Subject']):<15}"
                f"{float(row['Average']):<15.2f}"
                f"{float(row['Highest']):<15.2f}"
                f"{float(row['Lowest']):<15.2f}"
                f"{int(row['Students']):<10}"
            )

    else:

        print(
            "No subject data available."
        )

    # --------------------------------------------------------
    # Top Performing Student
    # --------------------------------------------------------

    top = pandas_top_student()

    print("\nTop Performing Student")

    print("-" * 35)

    if top:

        print(
            f"Name       : {top['Name']}"
        )

        print(
            f"Percentage : "
            f"{float(top['Percentage']):.2f}%"
        )

        print(
            f"Grade      : {top['Grade']}"
        )

    # --------------------------------------------------------
    # Lowest Performing Student
    # --------------------------------------------------------

    lowest = pandas_lowest_student()

    print(
        "\nStudent Needing Most Attention"
    )

    print("-" * 35)

    if lowest:

        print(
            f"Name       : {lowest['Name']}"
        )

        print(
            f"Percentage : "
            f"{float(lowest['Percentage']):.2f}%"
        )

        print(
            f"Grade      : {lowest['Grade']}"
        )

    # --------------------------------------------------------
    # Study Statistics
    # --------------------------------------------------------

    study = pandas_study_statistics()

    print("\nStudy Habits Statistics")

    print("-" * 35)

    if study:

        print(
            f"Average Study Hours : "
            f"{float(study['average_hours']):.2f} "
            f"hours/day"
        )

        print(
            f"Median Study Hours  : "
            f"{float(study['median_hours']):.2f} "
            f"hours/day"
        )

        print(
            f"Highest Study Hours : "
            f"{float(study['highest_hours']):.2f} "
            f"hours/day"
        )

        print(
            f"Lowest Study Hours  : "
            f"{float(study['lowest_hours']):.2f} "
            f"hours/day"
        )

    else:

        print(
            "No study-hour data available."
        )

    # --------------------------------------------------------
    # Study Hours vs Performance
    # --------------------------------------------------------

    study_performance = (
        pandas_study_performance()
    )

    print(
        "\nStudy Hours vs Performance"
    )

    print("-" * 45)

    if not study_performance.empty:

        for _, row in (
            study_performance.iterrows()
        ):

            print(
                f"{str(row['Name']):<12}"
                f"Study: "
                f"{float(row['StudyHours']):.2f} "
                f"hrs/day   "
                f"Score: "
                f"{float(row['Percentage']):.2f}%"
            )

    else:

        print(
            "No matching study and "
            "performance data available."
        )

    # --------------------------------------------------------
    # Correlation
    # --------------------------------------------------------

    correlation = pandas_correlation()

    print(
        "\nStudy Hours / Performance Correlation"
    )

    print("-" * 45)

    if correlation is not None:

        print(
            f"Correlation : "
            f"{float(correlation):.3f}"
        )

        if correlation > 0.7:

            print(
                "Strong positive association."
            )

        elif correlation > 0.3:

            print(
                "Moderate positive association."
            )

        elif correlation > 0:

            print(
                "Weak positive association."
            )

        elif correlation < -0.3:

            print(
                "Negative association."
            )

        else:

            print(
                "Weak or no clear association."
            )

    else:

        print(
            "Not enough matching data "
            "to calculate correlation."
        )

    print(
        "\n=========================================="
    )


# ============================================================
# VISUALIZATION MENU
# ============================================================

def visualization_menu():
    """
    Display the visualization menu and generate charts.
    """

    while True:

        print(
            "\n========== DATA VISUALIZATIONS =========="
        )

        print("1. Student Performance")

        print("2. Subject Performance")

        print("3. Grade Distribution")

        print("4. Performance Categories")

        print("5. Study Hours vs Performance")

        print("6. Generate All Charts")

        print("7. Back to Main Menu")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Student Performance Chart
        # ----------------------------------------------------

        if choice == "1":

            show_student_performance_chart()

        # ----------------------------------------------------
        # Subject Performance Chart
        # ----------------------------------------------------

        elif choice == "2":

            show_subject_performance_chart()

        # ----------------------------------------------------
        # Grade Distribution Chart
        # ----------------------------------------------------

        elif choice == "3":

            show_grade_distribution_chart()

        # ----------------------------------------------------
        # Performance Categories Chart
        # ----------------------------------------------------

        elif choice == "4":

            show_performance_categories_chart()

        # ----------------------------------------------------
        # Study Hours vs Performance Chart
        # ----------------------------------------------------

        elif choice == "5":

            show_study_hours_vs_performance()

        # ----------------------------------------------------
        # Generate All Charts
        # ----------------------------------------------------

        elif choice == "6":

            print(
                "\nGenerating all charts...\n"
            )

            show_student_performance_chart()

            show_subject_performance_chart()

            show_grade_distribution_chart()

            show_performance_categories_chart()

            show_study_hours_vs_performance()

            print(
                "\nAll charts generated successfully."
            )

        # ----------------------------------------------------
        # Back to Main Menu
        # ----------------------------------------------------

        elif choice == "7":

            break

        # ----------------------------------------------------
        # Invalid Choice
        # ----------------------------------------------------

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-7."
            )


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():
    """
    Main application loop.
    """

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Add / Update Student
        # ----------------------------------------------------

        if choice == "1":

            add_student()

        # ----------------------------------------------------
        # View Students
        # ----------------------------------------------------

        elif choice == "2":

            view_students()

        # ----------------------------------------------------
        # Search Student
        # ----------------------------------------------------

        elif choice == "3":

            name = input(
                "Enter student name to search: "
            ).strip()

            if name:

                search_student(name)

            else:

                print(
                    "\nStudent name cannot be empty."
                )

        # ----------------------------------------------------
        # Student Profile
        # ----------------------------------------------------

        elif choice == "4":

            name = input(
                "Enter student name: "
            ).strip()

            if name:

                get_student_profile(name)

            else:

                print(
                    "\nStudent name cannot be empty."
                )

        # ----------------------------------------------------
        # Student Comparison
        # ----------------------------------------------------

        elif choice == "5":

            compare_students()

        # ----------------------------------------------------
        # Class Performance Dashboard
        # ----------------------------------------------------

        elif choice == "6":

            display_class_dashboard()

        # ----------------------------------------------------
        # Performance Trend
        # ----------------------------------------------------

        elif choice == "7":

            performance_trend_menu()

        # ----------------------------------------------------
        # Existing Analytics
        # ----------------------------------------------------

        elif choice == "8":

            view_analytics()

        # ----------------------------------------------------
        # Pandas Analytics
        # ----------------------------------------------------

        elif choice == "9":

            view_pandas_analysis()

        # ----------------------------------------------------
        # Data Visualizations
        # ----------------------------------------------------

        elif choice == "10":

            visualization_menu()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "11":

            print(
                "\nThank you for using "
                "Student Performance Analyzer."
            )

            break

        # ----------------------------------------------------
        # Invalid Choice
        # ----------------------------------------------------

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-11."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()

