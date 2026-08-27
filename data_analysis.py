import pandas as pd
import os


STUDENTS_FILE = "data/students.csv"
SUBJECT_MARKS_FILE = "data/subject_marks.csv"
STUDY_HOURS_FILE = "data/study_hours.csv"


def load_student_data():
    """
    Load student performance data using Pandas.
    """

    if not os.path.exists(STUDENTS_FILE):
        return pd.DataFrame()

    try:
        df = pd.read_csv(STUDENTS_FILE)

        if df.empty:
            return pd.DataFrame()

        # Convert numeric columns safely
        df["Total"] = pd.to_numeric(
            df["Total"],
            errors="coerce"
        )

        df["Percentage"] = pd.to_numeric(
            df["Percentage"],
            errors="coerce"
        )

        # Remove invalid records
        df = df.dropna(
            subset=["Name", "Percentage"]
        )

        return df

    except Exception as error:

        print(
            f"Error loading student data: {error}"
        )

        return pd.DataFrame()


def load_subject_data():
    """
    Load subject-wise performance data.
    """

    if not os.path.exists(SUBJECT_MARKS_FILE):
        return pd.DataFrame()

    try:

        df = pd.read_csv(
            SUBJECT_MARKS_FILE
        )

        if df.empty:
            return pd.DataFrame()

        if "Marks" in df.columns:

            df["Marks"] = pd.to_numeric(
                df["Marks"],
                errors="coerce"
            )

        df = df.dropna(
            subset=["Marks"]
        )

        return df

    except Exception as error:

        print(
            f"Error loading subject data: {error}"
        )

        return pd.DataFrame()


def load_study_data():
    """
    Load study-hour data using Pandas.
    """

    if not os.path.exists(STUDY_HOURS_FILE):
        return pd.DataFrame()

    try:

        df = pd.read_csv(
            STUDY_HOURS_FILE
        )

        if df.empty:
            return pd.DataFrame()

        if "StudyHours" in df.columns:

            df["StudyHours"] = pd.to_numeric(
                df["StudyHours"],
                errors="coerce"
            )

        df = df.dropna(
            subset=["StudyHours"]
        )

        return df

    except Exception as error:

        print(
            f"Error loading study data: {error}"
        )

        return pd.DataFrame()


def pandas_class_statistics():
    """
    Calculate overall class statistics.
    """

    df = load_student_data()

    if df.empty:
        return {}

    return {
        "total_students": len(df),

        "average_percentage":
            df["Percentage"].mean(),

        "highest_percentage":
            df["Percentage"].max(),

        "lowest_percentage":
            df["Percentage"].min(),

        "median_percentage":
            df["Percentage"].median()
    }


def pandas_grade_distribution():
    """
    Calculate grade distribution.
    """

    df = load_student_data()

    if df.empty or "Grade" not in df.columns:

        return {}

    return (
        df["Grade"]
        .value_counts()
        .to_dict()
    )


def pandas_student_ranking():
    """
    Rank students according to percentage.
    """

    df = load_student_data()

    if df.empty:
        return pd.DataFrame()

    ranking = df[
        ["Name", "Percentage", "Grade"]
    ].copy()

    ranking = ranking.sort_values(
        by="Percentage",
        ascending=False
    )

    ranking.insert(
        0,
        "Rank",
        range(1, len(ranking) + 1)
    )

    return ranking


def pandas_subject_statistics():
    """
    Calculate average marks for every subject.
    """

    df = load_subject_data()

    if df.empty:
        return pd.DataFrame()

    if "Subject" not in df.columns:
        return pd.DataFrame()

    result = (
        df.groupby("Subject")["Marks"]
        .agg(
            ["mean", "max", "min", "count"]
        )
        .reset_index()
    )

    result.columns = [
        "Subject",
        "Average",
        "Highest",
        "Lowest",
        "Students"
    ]

    result = result.sort_values(
        by="Average",
        ascending=False
    )

    return result


def pandas_study_statistics():
    """
    Calculate study-hour statistics.
    """

    df = load_study_data()

    if df.empty:
        return {}

    return {
        "average_hours":
            df["StudyHours"].mean(),

        "highest_hours":
            df["StudyHours"].max(),

        "lowest_hours":
            df["StudyHours"].min(),

        "median_hours":
            df["StudyHours"].median()
    }


def pandas_merge_learning_data():
    """
    Merge academic performance and
    study-hour data.
    """

    students = load_student_data()

    study = load_study_data()

    if students.empty or study.empty:
        return pd.DataFrame()

    if "Name" not in students.columns:
        return pd.DataFrame()

    if "Name" not in study.columns:
        return pd.DataFrame()

    merged = pd.merge(
        students,
        study,
        on="Name",
        how="inner"
    )

    return merged


def pandas_study_performance():
    """
    Analyze relationship between
    study hours and performance.
    """

    df = pandas_merge_learning_data()

    if df.empty:
        return pd.DataFrame()

    return df[
        [
            "Name",
            "StudyHours",
            "Percentage"
        ]
    ].sort_values(
        by="Percentage",
        ascending=False
    )


def pandas_performance_categories():
    """
    Categorize students based on percentage.
    """

    df = load_student_data()

    if df.empty:
        return {}

    def category(percentage):

        if percentage >= 90:
            return "Excellent"

        elif percentage >= 70:
            return "Good"

        elif percentage >= 50:
            return "Average"

        else:
            return "Needs Attention"

    df["Category"] = (
        df["Percentage"]
        .apply(category)
    )

    return (
        df["Category"]
        .value_counts()
        .to_dict()
    )


def pandas_top_student():
    """
    Find the highest-performing student.
    """

    df = load_student_data()

    if df.empty:
        return None

    student = df.loc[
        df["Percentage"].idxmax()
    ]

    return {
        "Name": student["Name"],
        "Percentage": student["Percentage"],
        "Grade": student["Grade"]
    }


def pandas_lowest_student():
    """
    Find the student requiring
    the most academic attention.
    """

    df = load_student_data()

    if df.empty:
        return None

    student = df.loc[
        df["Percentage"].idxmin()
    ]

    return {
        "Name": student["Name"],
        "Percentage": student["Percentage"],
        "Grade": student["Grade"]
    }


def pandas_correlation():
    """
    Calculate correlation between
    study hours and academic percentage.
    """

    df = pandas_merge_learning_data()

    if len(df) < 2:
        return None

    correlation = df[
        ["StudyHours", "Percentage"]
    ].corr().iloc[0, 1]

    return correlation