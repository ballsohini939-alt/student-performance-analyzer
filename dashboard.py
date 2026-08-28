import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

STUDENTS_FILE = DATA_DIR / "students.csv"
SUBJECT_FILE = DATA_DIR / "subject_marks.csv"
STUDY_FILE = DATA_DIR / "study_hours.csv"
HISTORY_FILE = DATA_DIR / "performance_history.csv"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    students = pd.read_csv(STUDENTS_FILE)
    subjects = pd.read_csv(SUBJECT_FILE)

    study = None
    history = None

    if STUDY_FILE.exists():
        study = pd.read_csv(STUDY_FILE)

    if HISTORY_FILE.exists():
        history = pd.read_csv(HISTORY_FILE)

    return students, subjects, study, history


students, subjects, study, history = load_data()


# ============================================================
# TITLE
# ============================================================

st.title("📊 Student Performance Analyzer")

st.markdown(
    """
    ### Academic Performance & Learning Analytics Dashboard

    Analyze academic performance, subject strengths, learning habits,
    rankings, and student progress using **Python, Pandas,
    Matplotlib, and Streamlit**.
    """
)

st.divider()


# ============================================================
# CLASS OVERVIEW
# ============================================================

st.subheader("📈 Class Performance Overview")

col1, col2, col3, col4 = st.columns(4)

total_students = len(students)
class_average = students["Percentage"].mean()
highest = students["Percentage"].max()
lowest = students["Percentage"].min()

with col1:
    st.metric("👥 Total Students", total_students)

with col2:
    st.metric("📊 Class Average", f"{class_average:.2f}%")

with col3:
    st.metric("🏆 Highest Percentage", f"{highest:.2f}%")

with col4:
    st.metric("⚠️ Lowest Percentage", f"{lowest:.2f}%")

st.divider()


# ============================================================
# SIDEBAR FILTER
# ============================================================

st.sidebar.title("🎛️ Dashboard Controls")

student_names = sorted(students["Name"].tolist())

selected_student = st.sidebar.selectbox(
    "Select Student",
    student_names
)

st.sidebar.markdown("---")

grade_filter = st.sidebar.multiselect(
    "Filter by Grade",
    options=sorted(students["Grade"].unique()),
    default=sorted(students["Grade"].unique())
)

filtered_students = students[
    students["Grade"].isin(grade_filter)
]


# ============================================================
# STUDENT PROFILE
# ============================================================

st.subheader("👤 Student Profile")

student = students[
    students["Name"].str.lower() == selected_student.lower()
].iloc[0]

profile_col1, profile_col2, profile_col3, profile_col4 = st.columns(4)

with profile_col1:
    st.metric("Student", student["Name"])

with profile_col2:
    st.metric("Percentage", f"{student['Percentage']:.2f}%")

with profile_col3:
    st.metric("Grade", student["Grade"])

with profile_col4:
    if student["Percentage"] >= 90:
        category = "Excellent"
    elif student["Percentage"] >= 80:
        category = "Good"
    elif student["Percentage"] >= 60:
        category = "Average"
    else:
        category = "Needs Attention"

    st.metric("Category", category)


# ============================================================
# STUDENT SUBJECT PERFORMANCE
# ============================================================

student_subjects = subjects[
    subjects["Name"].str.lower() == selected_student.lower()
]

if not student_subjects.empty:

    st.subheader("📚 Subject-wise Performance")

    chart_col, table_col = st.columns([2, 1])

    with chart_col:

        fig, ax = plt.subplots()

        ax.bar(
            student_subjects["Subject"],
            student_subjects["Marks"]
        )

        ax.set_title(
            f"{selected_student.title()} - Subject Performance"
        )

        ax.set_xlabel("Subject")
        ax.set_ylabel("Marks (%)")

        ax.set_ylim(0, 100)

        plt.xticks(rotation=30)

        st.pyplot(fig)

        plt.close(fig)

    with table_col:

        st.dataframe(
            student_subjects[["Subject", "Marks"]],
            use_container_width=True,
            hide_index=True
        )

        strongest = student_subjects.loc[
            student_subjects["Marks"].idxmax()
        ]

        weakest = student_subjects.loc[
            student_subjects["Marks"].idxmin()
        ]

        st.success(
            f"💪 Strongest Subject: **{strongest['Subject']} "
            f"({strongest['Marks']:.2f}%)**"
        )

        st.info(
            f"📌 Lowest Subject: **{weakest['Subject']} "
            f"({weakest['Marks']:.2f}%)**"
        )

else:

    st.info(
        f"No subject-wise data available for {selected_student}."
    )


st.divider()


# ============================================================
# CLASS RANKING
# ============================================================

st.subheader("🏆 Student Ranking")

ranking = students.sort_values(
    "Percentage",
    ascending=False
).reset_index(drop=True)

ranking.insert(0, "Rank", ranking.index + 1)

ranking_display = ranking[
    ["Rank", "Name", "Percentage", "Grade"]
]

st.dataframe(
    ranking_display,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# CLASS PERFORMANCE CHART
# ============================================================

st.subheader("📊 Student Performance")

fig, ax = plt.subplots(figsize=(10, 5))

sorted_students = students.sort_values(
    "Percentage",
    ascending=False
)

ax.bar(
    sorted_students["Name"],
    sorted_students["Percentage"]
)

ax.set_title("Student Performance")
ax.set_xlabel("Student")
ax.set_ylabel("Percentage")

ax.set_ylim(0, 100)

plt.xticks(rotation=30)

st.pyplot(fig)

plt.close(fig)


# ============================================================
# GRADE DISTRIBUTION
# ============================================================

st.subheader("🎓 Grade Distribution")

grade_counts = students["Grade"].value_counts()

fig, ax = plt.subplots()

ax.bar(
    grade_counts.index,
    grade_counts.values
)

ax.set_title("Grade Distribution")
ax.set_xlabel("Grade")
ax.set_ylabel("Number of Students")

st.pyplot(fig)

plt.close(fig)


# ============================================================
# PERFORMANCE CATEGORIES
# ============================================================

st.subheader("📌 Performance Categories")


def get_category(score):

    if score >= 90:
        return "Excellent"

    elif score >= 80:
        return "Good"

    elif score >= 60:
        return "Average"

    else:
        return "Needs Attention"


students_with_category = students.copy()

students_with_category["Category"] = (
    students_with_category["Percentage"]
    .apply(get_category)
)

category_counts = (
    students_with_category["Category"]
    .value_counts()
)

fig, ax = plt.subplots()

ax.bar(
    category_counts.index,
    category_counts.values
)

ax.set_title("Performance Categories")
ax.set_xlabel("Category")
ax.set_ylabel("Number of Students")

plt.xticks(rotation=20)

st.pyplot(fig)

plt.close(fig)


# ============================================================
# SUBJECT PERFORMANCE
# ============================================================

st.subheader("📚 Class Subject Performance")

subject_average = (
    subjects.groupby("Subject")["Marks"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    subject_average.index,
    subject_average.values
)

ax.set_title("Average Subject Performance")
ax.set_xlabel("Subject")
ax.set_ylabel("Average Marks (%)")

ax.set_ylim(0, 100)

plt.xticks(rotation=30)

st.pyplot(fig)

plt.close(fig)


# ============================================================
# STUDY HOURS
# ============================================================

if study is not None and not study.empty:

    st.subheader("⏱️ Study Hours vs Performance")

    study_data = study.merge(
        students[["Name", "Percentage"]],
        on="Name",
        how="inner"
    )

    if not study_data.empty:

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.scatter(
            study_data["StudyHours"],
            study_data["Percentage"]
        )

        ax.set_title(
            "Study Hours vs Academic Performance"
        )

        ax.set_xlabel("Study Hours / Day")
        ax.set_ylabel("Percentage")

        ax.set_ylim(0, 100)

        st.pyplot(fig)

        plt.close(fig)

        st.dataframe(
            study_data,
            use_container_width=True,
            hide_index=True
        )

        if len(study_data) >= 2:

            correlation = (
                study_data["StudyHours"]
                .corr(study_data["Percentage"])
            )

            st.metric(
                "Study Hours / Performance Correlation",
                f"{correlation:.3f}"
            )


# ============================================================
# PERFORMANCE TREND
# ============================================================

if history is not None and not history.empty:

    st.subheader("📈 Performance Trend")

    history_student = history[
        history["Name"].str.lower()
        == selected_student.lower()
    ]

    if not history_student.empty:

        date_column = None

        for column in ["Date", "date", "Timestamp", "timestamp"]:
            if column in history_student.columns:
                date_column = column
                break

        percentage_column = None

        for column in [
            "Percentage",
            "percentage",
            "Score",
            "score"
        ]:
            if column in history_student.columns:
                percentage_column = column
                break

        if percentage_column:

            if date_column:

                history_student = history_student.sort_values(
                    date_column
                )

                fig, ax = plt.subplots(figsize=(9, 5))

                ax.plot(
                    history_student[date_column],
                    history_student[percentage_column],
                    marker="o"
                )

                ax.set_title(
                    f"{selected_student.title()} - Performance Trend"
                )

                ax.set_xlabel("Date")
                ax.set_ylabel("Percentage")

                ax.set_ylim(0, 100)

                plt.xticks(rotation=30)

                st.pyplot(fig)

                plt.close(fig)

            else:

                st.line_chart(
                    history_student[percentage_column]
                )

    else:

        st.info(
            f"No performance history available for {selected_student}."
        )


# ============================================================
# PERSONALIZED INSIGHT
# ============================================================

st.divider()

st.subheader("💡 Personalized Learning Insight")

percentage = float(student["Percentage"])

if percentage >= 90:

    st.success(
        f"""
        **{selected_student.title()} is performing at an excellent level.**

        Maintain the current study routine, continue practicing consistently,
        and focus on advanced problems to achieve further growth.
        """
    )

elif percentage >= 80:

    st.info(
        f"""
        **{selected_student.title()} is performing well.**

        Continue regular practice and focus on improving weaker subjects
        to move toward the excellent category.
        """
    )

elif percentage >= 60:

    st.warning(
        f"""
        **{selected_student.title()} has average academic performance.**

        More consistent practice and additional attention to weaker subjects
        can help improve the overall score.
        """
    )

else:

    st.error(
        f"""
        **{selected_student.title()} needs additional academic attention.**

        Focus on foundational concepts, regular practice, and targeted support
        in weaker subjects.
        """
    )


# ============================================================
# FILTERED CLASS DATA
# ============================================================

st.divider()

st.subheader("🔎 Filtered Class Data")

st.write(
    f"Showing **{len(filtered_students)}** student(s) "
    f"matching the selected grade filters."
)

st.dataframe(
    filtered_students[
        ["Name", "Total", "Percentage", "Grade"]
    ],
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Student Performance Analyzer | "
    "Python • Pandas • Matplotlib • Streamlit"
)