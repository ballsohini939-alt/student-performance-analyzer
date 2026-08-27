import os
import pandas as pd
import matplotlib.pyplot as plt


# ==============================
# FILE PATHS
# ==============================

STUDENTS_FILE = "data/students.csv"
SUBJECT_FILE = "data/subject_marks.csv"
STUDY_FILE = "data/study_hours.csv"

CHARTS_FOLDER = "charts"


# ==============================
# HELPER FUNCTIONS
# ==============================

def create_charts_folder():
    """Create the charts folder if it does not exist."""

    os.makedirs(CHARTS_FOLDER, exist_ok=True)


def save_and_show_chart(filename):
    """Save the current chart and display it."""

    create_charts_folder()

    filepath = os.path.join(
        CHARTS_FOLDER,
        filename
    )

    plt.tight_layout()
    plt.savefig(
        filepath,
        dpi=150,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print(f"Chart saved: {filepath}")


# ==============================
# LOAD STUDENT DATA
# ==============================

def load_student_data():
    """Load student performance data."""

    if not os.path.exists(STUDENTS_FILE):
        print("Student data file not found.")
        return pd.DataFrame()

    try:
        df = pd.read_csv(STUDENTS_FILE)

    except Exception as error:
        print(f"Error reading student data: {error}")
        return pd.DataFrame()

    if df.empty:
        print("No student data available.")
        return pd.DataFrame()

    if "Percentage" not in df.columns:
        print("Percentage column not found.")
        return pd.DataFrame()

    df["Percentage"] = pd.to_numeric(
        df["Percentage"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["Percentage"]
    )

    return df


# ==============================
# LOAD SUBJECT DATA
# ==============================

def load_subject_data():
    """Load subject-wise performance data."""

    if not os.path.exists(SUBJECT_FILE):
        print("Subject data file not found.")
        return pd.DataFrame()

    try:
        df = pd.read_csv(SUBJECT_FILE)

    except Exception as error:
        print(f"Error reading subject data: {error}")
        return pd.DataFrame()

    if df.empty:
        print("No subject data available.")
        return pd.DataFrame()

    required_columns = [
        "Subject",
        "Marks"
    ]

    for column in required_columns:

        if column not in df.columns:
            print(
                f"Required column '{column}' "
                f"not found in subject data."
            )

            return pd.DataFrame()

    df["Marks"] = pd.to_numeric(
        df["Marks"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["Marks"]
    )

    return df


# ==============================
# LOAD STUDY DATA
# ==============================

def load_study_data():
    """
    Load study-hour data and merge it
    with academic performance data.
    """

    if not os.path.exists(STUDY_FILE):
        print("Study hours data file not found.")
        return pd.DataFrame()

    if not os.path.exists(STUDENTS_FILE):
        print("Student performance data file not found.")
        return pd.DataFrame()

    try:
        study_df = pd.read_csv(STUDY_FILE)
        student_df = pd.read_csv(STUDENTS_FILE)

    except Exception as error:
        print(f"Error reading study data: {error}")
        return pd.DataFrame()

    if study_df.empty:
        print("No study-hour data available.")
        return pd.DataFrame()

    if student_df.empty:
        print("No student performance data available.")
        return pd.DataFrame()

    # Check required columns

    if "Name" not in study_df.columns:
        print("Name column not found in study data.")
        return pd.DataFrame()

    if "StudyHours" not in study_df.columns:
        print(
            "StudyHours column not found "
            "in study data."
        )

        return pd.DataFrame()

    if "Name" not in student_df.columns:
        print(
            "Name column not found "
            "in student data."
        )

        return pd.DataFrame()

    if "Percentage" not in student_df.columns:
        print(
            "Percentage column not found "
            "in student data."
        )

        return pd.DataFrame()

    # Convert numeric values

    study_df["StudyHours"] = pd.to_numeric(
        study_df["StudyHours"],
        errors="coerce"
    )

    student_df["Percentage"] = pd.to_numeric(
        student_df["Percentage"],
        errors="coerce"
    )

    # Remove invalid records

    study_df = study_df.dropna(
        subset=["StudyHours"]
    )

    student_df = student_df.dropna(
        subset=["Percentage"]
    )

    # Merge study hours with performance

    merged_df = pd.merge(
        study_df[
            ["Name", "StudyHours"]
        ],
        student_df[
            ["Name", "Percentage"]
        ],
        on="Name",
        how="inner"
    )

    return merged_df


# ==============================
# 1. STUDENT PERFORMANCE CHART
# ==============================

def show_student_performance_chart():
    """Display student percentage comparison."""

    df = load_student_data()

    if df.empty:
        return

    df = df.sort_values(
        "Percentage",
        ascending=False
    )

    plt.figure(
        figsize=(10, 6)
    )

    plt.bar(
        df["Name"],
        df["Percentage"]
    )

    plt.title(
        "Student Performance Comparison"
    )

    plt.xlabel(
        "Students"
    )

    plt.ylabel(
        "Percentage (%)"
    )

    plt.ylim(
        0,
        100
    )

    plt.xticks(
        rotation=45
    )

    # Add percentage labels

    for index, value in enumerate(
        df["Percentage"]
    ):

        plt.text(
            index,
            value + 1,
            f"{value:.1f}%",
            ha="center"
        )

    save_and_show_chart(
        "student_performance.png"
    )


# ==============================
# 2. SUBJECT PERFORMANCE CHART
# ==============================

def show_subject_performance_chart():
    """Display average performance for each subject."""

    df = load_subject_data()

    if df.empty:
        return

    subject_average = (
        df.groupby("Subject")["Marks"]
        .mean()
        .sort_values(
            ascending=False
        )
    )

    plt.figure(
        figsize=(10, 6)
    )

    plt.bar(
        subject_average.index,
        subject_average.values
    )

    plt.title(
        "Subject-wise Average Performance"
    )

    plt.xlabel(
        "Subjects"
    )

    plt.ylabel(
        "Average Marks (%)"
    )

    plt.ylim(
        0,
        100
    )

    plt.xticks(
        rotation=45
    )

    # Add average labels

    for index, value in enumerate(
        subject_average.values
    ):

        plt.text(
            index,
            value + 1,
            f"{value:.1f}%",
            ha="center"
        )

    save_and_show_chart(
        "subject_performance.png"
    )


# ==============================
# 3. GRADE DISTRIBUTION CHART
# ==============================

def show_grade_distribution_chart():
    """Display grade distribution."""

    df = load_student_data()

    if df.empty:
        return

    if "Grade" not in df.columns:
        print("Grade column not found.")
        return

    grade_counts = (
        df["Grade"]
        .value_counts()
        .sort_index()
    )

    plt.figure(
        figsize=(8, 6)
    )

    plt.bar(
        grade_counts.index,
        grade_counts.values
    )

    plt.title(
        "Grade Distribution"
    )

    plt.xlabel(
        "Grade"
    )

    plt.ylabel(
        "Number of Students"
    )

    # Add count labels

    for index, value in enumerate(
        grade_counts.values
    ):

        plt.text(
            index,
            value + 0.05,
            str(value),
            ha="center"
        )

    save_and_show_chart(
        "grade_distribution.png"
    )


# ==============================
# 4. PERFORMANCE CATEGORY CHART
# ==============================

def show_performance_categories_chart():
    """Display performance categories."""

    df = load_student_data()

    if df.empty:
        return

    def categorize(score):

        if score >= 90:
            return "Excellent"

        elif score >= 75:
            return "Good"

        elif score >= 60:
            return "Average"

        else:
            return "Needs Attention"

    categories = df[
        "Percentage"
    ].apply(
        categorize
    )

    category_order = [
        "Excellent",
        "Good",
        "Average",
        "Needs Attention"
    ]

    category_counts = (
        categories
        .value_counts()
        .reindex(
            category_order,
            fill_value=0
        )
    )

    plt.figure(
        figsize=(9, 6)
    )

    plt.bar(
        category_counts.index,
        category_counts.values
    )

    plt.title(
        "Performance Categories"
    )

    plt.xlabel(
        "Category"
    )

    plt.ylabel(
        "Number of Students"
    )

    plt.xticks(
        rotation=15
    )

    # Add count labels

    for index, value in enumerate(
        category_counts.values
    ):

        plt.text(
            index,
            value + 0.05,
            str(value),
            ha="center"
        )

    save_and_show_chart(
        "performance_categories.png"
    )


# ==============================
# 5. STUDY HOURS VS PERFORMANCE
# ==============================

def show_study_hours_vs_performance():
    """
    Display the relationship between
    study hours and academic performance.
    """

    df = load_study_data()

    if df.empty:
        print(
            "Not enough study-hour data "
            "available for visualization."
        )

        return

    plt.figure(
        figsize=(9, 6)
    )

    plt.scatter(
        df["StudyHours"],
        df["Percentage"],
        s=100
    )

    plt.title(
        "Study Hours vs Academic Performance"
    )

    plt.xlabel(
        "Study Hours per Day"
    )

    plt.ylabel(
        "Percentage (%)"
    )

    plt.ylim(
        0,
        100
    )

    # Add student names

    for _, row in df.iterrows():

        plt.annotate(
            row["Name"],
            (
                row["StudyHours"],
                row["Percentage"]
            ),
            xytext=(5, 5),
            textcoords="offset points"
        )

    plt.grid(
        True,
        alpha=0.3
    )

    save_and_show_chart(
        "study_hours_vs_performance.png"
    )


# ==============================
# 6. SHOW ALL VISUALIZATIONS
# ==============================

def show_all_visualizations():
    """Display all available visualizations."""

    print(
        "\n========== DATA VISUALIZATIONS =========="
    )

    print(
        "\nOpening Student Performance Chart..."
    )

    show_student_performance_chart()

    print(
        "\nOpening Subject Performance Chart..."
    )

    show_subject_performance_chart()

    print(
        "\nOpening Grade Distribution Chart..."
    )

    show_grade_distribution_chart()

    print(
        "\nOpening Performance Categories Chart..."
    )

    show_performance_categories_chart()

    print(
        "\nOpening Study Hours vs Performance Chart..."
    )

    show_study_hours_vs_performance()

    print(
        "\nAll visualizations completed."
    )

    print(
        "Charts are available in the 'charts' folder."
    )

    print(
        "=========================================="
    )