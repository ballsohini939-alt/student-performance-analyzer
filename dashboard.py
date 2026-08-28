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
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .dashboard-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .dashboard-subtitle {
        font-size: 1.05rem;
        color: #64748b;
        margin-bottom: 1.5rem;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 650;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }

    .insight-box {
        padding: 1rem;
        border-radius: 10px;
        background-color: #eef2ff;
        border-left: 5px solid #6366f1;
        margin-bottom: 1rem;
    }

    .attention-box {
        padding: 1rem;
        border-radius: 10px;
        background-color: #fff7ed;
        border-left: 5px solid #f97316;
        margin-bottom: 1rem;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    students = pd.read_csv(DATA_DIR / "students.csv")
    subjects = pd.read_csv(DATA_DIR / "subject_marks.csv")
    study = pd.read_csv(DATA_DIR / "study_hours.csv")

    return students, subjects, study


students, subjects, study_hours = load_data()


# ============================================================
# NORMALIZE COLUMN NAMES
# ============================================================

students.columns = [
    str(column).strip().lower()
    for column in students.columns
]

subjects.columns = [
    str(column).strip().lower()
    for column in subjects.columns
]

study_hours.columns = [
    str(column).strip().lower()
    for column in study_hours.columns
]


# ============================================================
# COLUMN DETECTION
# ============================================================

def detect_column(df, possible_names):

    for column in possible_names:

        if column in df.columns:
            return column

    return None


student_name = detect_column(
    students,
    ["name", "student_name"]
)

percentage = detect_column(
    students,
    ["percentage", "percent"]
)

total_marks = detect_column(
    students,
    ["total", "total_marks"]
)

grade = detect_column(
    students,
    ["grade"]
)

category = detect_column(
    students,
    ["category", "performance_category"]
)

subject_student = detect_column(
    subjects,
    ["name", "student_name"]
)

subject_name = detect_column(
    subjects,
    ["subject", "subject_name"]
)

subject_marks = detect_column(
    subjects,
    ["marks", "mark", "score"]
)

study_student = detect_column(
    study_hours,
    ["name", "student_name"]
)

study_value = detect_column(
    study_hours,
    ["study_hours", "hours", "hours_per_day"]
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-title">📊 Student Performance Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Academic Performance & Learning Analytics Dashboard'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📊 Dashboard")

st.sidebar.markdown(
    "### Navigation"
)

page = st.sidebar.radio(
    "Choose a section",
    [
        "🏠 Class Overview",
        "👨‍🎓 Student Analysis",
        "📚 Subject Analysis",
        "🕐 Study Habits"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Student Performance Analyzer\n\n"
    "Python • Pandas • Matplotlib • Streamlit"
)


# ============================================================
# CLASS OVERVIEW
# ============================================================

if page == "🏠 Class Overview":

    st.header("Class Performance Overview")

    total_students = len(students)

    avg_percentage = (
        students[percentage].mean()
        if percentage
        else 0
    )

    highest = (
        students[percentage].max()
        if percentage
        else 0
    )

    lowest = (
        students[percentage].min()
        if percentage
        else 0
    )

    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "👨‍🎓 Total Students",
        total_students
    )

    c2.metric(
        "📊 Class Average",
        f"{avg_percentage:.2f}%"
    )

    c3.metric(
        "🏆 Highest Score",
        f"{highest:.2f}%"
    )

    c4.metric(
        "⚠️ Lowest Score",
        f"{lowest:.2f}%"
    )

    st.markdown("---")

    # --------------------------------------------------------
    # TOP PERFORMERS + ATTENTION
    # --------------------------------------------------------

    left, right = st.columns(2)

    with left:

        st.subheader("🏆 Top Performers")

        top_students = students.sort_values(
            percentage,
            ascending=False
        ).head(3)

        for index, (_, row) in enumerate(
            top_students.iterrows(),
            start=1
        ):

            student = row[student_name]
            score = row[percentage]

            st.success(
                f"{index}. {student} — {score:.2f}%"
            )

    with right:

        st.subheader("⚠️ Students Needing Attention")

        attention = students[
            students[percentage] < 50
        ]

        if attention.empty:

            st.success(
                "No students are currently below 50%."
            )

        else:

            for _, row in attention.iterrows():

                st.warning(
                    f"{row[student_name]} — "
                    f"{row[percentage]:.2f}%"
                )

    st.markdown("---")

    # --------------------------------------------------------
    # PERFORMANCE TABLE
    # --------------------------------------------------------

    st.subheader("📋 Student Performance")

    display_columns = [
        column
        for column in [
            student_name,
            total_marks,
            percentage,
            grade,
            category
        ]
        if column
    ]

    performance_table = students[
        display_columns
    ].sort_values(
        percentage,
        ascending=False
    )

    st.dataframe(
        performance_table,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------------
    # PERFORMANCE CHART
    # --------------------------------------------------------

    st.subheader("📈 Student Performance")

    fig, ax = plt.subplots(figsize=(10, 5))

    sorted_students = students.sort_values(
        percentage,
        ascending=False
    )

    ax.bar(
        sorted_students[student_name],
        sorted_students[percentage]
    )

    ax.axhline(
        avg_percentage,
        linestyle="--",
        label=f"Class Average: {avg_percentage:.2f}%"
    )

    ax.set_ylabel("Percentage")
    ax.set_xlabel("Student")
    ax.set_title("Student Performance vs Class Average")

    plt.xticks(rotation=35)
    ax.legend()

    st.pyplot(fig)

    # --------------------------------------------------------
    # GRADE DISTRIBUTION
    # --------------------------------------------------------

    if grade:

        st.subheader("🎓 Grade Distribution")

        grade_counts = students[
            grade
        ].value_counts()

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.bar(
            grade_counts.index,
            grade_counts.values
        )

        ax.set_xlabel("Grade")
        ax.set_ylabel("Students")
        ax.set_title("Grade Distribution")

        st.pyplot(fig)

    # --------------------------------------------------------
    # CLASS INSIGHT
    # --------------------------------------------------------

    st.markdown(
        '<div class="insight-box">'
        '<b>💡 Class Insight</b><br>'
        f'The class average is {avg_percentage:.2f}%. '
        f'The highest score is {highest:.2f}%, while '
        f'the lowest score is {lowest:.2f}%.'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# STUDENT ANALYSIS
# ============================================================

elif page == "👨‍🎓 Student Analysis":

    st.header("👨‍🎓 Individual Student Analysis")

    selected_student = st.selectbox(
        "Select a student",
        students[student_name].tolist()
    )

    student_row = students[
        students[student_name] == selected_student
    ].iloc[0]

    # --------------------------------------------------------
    # STUDENT METRICS
    # --------------------------------------------------------

    c1, c2, c3 = st.columns(3)

    if total_marks:

        c1.metric(
            "Total Marks",
            f"{student_row[total_marks]:.2f}"
        )

    if percentage:

        c2.metric(
            "Percentage",
            f"{student_row[percentage]:.2f}%"
        )

    if grade:

        c3.metric(
            "Grade",
            student_row[grade]
        )

    st.markdown("---")

    # --------------------------------------------------------
    # CATEGORY
    # --------------------------------------------------------

    if category:

        st.info(
            f"Performance Category: "
            f"**{student_row[category]}**"
        )

    # --------------------------------------------------------
    # SUBJECT PERFORMANCE
    # --------------------------------------------------------

    st.subheader("📚 Subject Performance")

    if (
        subject_student
        and subject_name
        and subject_marks
    ):

        student_subjects = subjects[
            subjects[subject_student] == selected_student
        ]

        if not student_subjects.empty:

            subject_table = student_subjects[
                [subject_name, subject_marks]
            ].copy()

            subject_table = subject_table.sort_values(
                subject_marks,
                ascending=False
            )

            st.dataframe(
                subject_table,
                use_container_width=True,
                hide_index=True
            )

            fig, ax = plt.subplots(figsize=(8, 4))

            ax.bar(
                subject_table[subject_name],
                subject_table[subject_marks]
            )

            ax.set_title(
                f"{selected_student} — Subject Performance"
            )

            ax.set_ylabel("Marks")

            plt.xticks(rotation=35)

            st.pyplot(fig)

            strongest = subject_table.iloc[0]
            weakest = subject_table.iloc[-1]

            st.success(
                f"Strongest Subject: "
                f"{strongest[subject_name]} "
                f"({strongest[subject_marks]:.2f})"
            )

            st.warning(
                f"Subject Needing Most Improvement: "
                f"{weakest[subject_name]} "
                f"({weakest[subject_marks]:.2f})"
            )

    # --------------------------------------------------------
    # STUDY HOURS
    # --------------------------------------------------------

    st.subheader("🕐 Study Habits")

    if (
        study_student
        and study_value
    ):

        student_study = study_hours[
            study_hours[study_student] == selected_student
        ]

        if not student_study.empty:

            hours = float(
                student_study[study_value].iloc[0]
            )

            st.metric(
                "Average Study Hours",
                f"{hours:.2f} hrs/day"
            )

        else:

            st.info(
                "Study-hour data is not available "
                "for this student."
            )


# ============================================================
# SUBJECT ANALYSIS
# ============================================================

elif page == "📚 Subject Analysis":

    st.header("📚 Subject Performance Analysis")

    if (
        subject_name
        and subject_marks
    ):

        subject_summary = (
            subjects
            .groupby(subject_name)[subject_marks]
            .agg(
                Average="mean",
                Highest="max",
                Lowest="min",
                Students="count"
            )
            .round(2)
        )

        # ----------------------------------------------------
        # SUBJECT METRICS
        # ----------------------------------------------------

        strongest_subject = subject_summary[
            "Average"
        ].idxmax()

        weakest_subject = subject_summary[
            "Average"
        ].idxmin()

        c1, c2 = st.columns(2)

        c1.metric(
            "💪 Strongest Subject",
            strongest_subject
        )

        c2.metric(
            "📌 Needs Most Attention",
            weakest_subject
        )

        st.markdown("---")

        st.subheader("📊 Subject Statistics")

        st.dataframe(
            subject_summary,
            use_container_width=True
        )

        # ----------------------------------------------------
        # SUBJECT CHART
        # ----------------------------------------------------

        st.subheader("📈 Average Performance by Subject")

        fig, ax = plt.subplots(figsize=(9, 5))

        ax.bar(
            subject_summary.index,
            subject_summary["Average"]
        )

        ax.set_ylabel("Average Marks")
        ax.set_xlabel("Subject")
        ax.set_title("Subject-wise Average Performance")

        plt.xticks(rotation=35)

        st.pyplot(fig)

        # ----------------------------------------------------
        # INSIGHT
        # ----------------------------------------------------

        strongest_score = subject_summary.loc[
            strongest_subject,
            "Average"
        ]

        weakest_score = subject_summary.loc[
            weakest_subject,
            "Average"
        ]

        st.markdown(
            '<div class="insight-box">'
            '<b>💡 Subject Insight</b><br>'
            f'{strongest_subject} is currently the strongest '
            f'subject with an average of {strongest_score:.2f}%. '
            f'{weakest_subject} has the lowest average at '
            f'{weakest_score:.2f}%.'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# STUDY HABITS
# ============================================================

elif page == "🕐 Study Habits":

    st.header("🕐 Study Habits & Learning Analysis")

    if (
        study_student
        and study_value
    ):

        study_data = study_hours.copy()

        study_data[study_value] = pd.to_numeric(
            study_data[study_value],
            errors="coerce"
        )

        study_data = study_data.dropna(
            subset=[study_value]
        )

        if not study_data.empty:

            average_hours = study_data[
                study_value
            ].mean()

            highest_hours = study_data[
                study_value
            ].max()

            lowest_hours = study_data[
                study_value
            ].min()

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Average Study Time",
                f"{average_hours:.2f} hrs/day"
            )

            c2.metric(
                "Highest Study Time",
                f"{highest_hours:.2f} hrs/day"
            )

            c3.metric(
                "Lowest Study Time",
                f"{lowest_hours:.2f} hrs/day"
            )

            st.markdown("---")

            # ------------------------------------------------
            # STUDY HOURS TABLE
            # ------------------------------------------------

            st.subheader("📋 Study Hours by Student")

            st.dataframe(
                study_data,
                use_container_width=True,
                hide_index=True
            )

            # ------------------------------------------------
            # STUDY HOURS CHART
            # ------------------------------------------------

            st.subheader("📊 Study Hours Distribution")

            fig, ax = plt.subplots(figsize=(9, 5))

            ax.bar(
                study_data[study_student],
                study_data[study_value]
            )

            ax.axhline(
                average_hours,
                linestyle="--",
                label=f"Average: {average_hours:.2f}"
            )

            ax.set_xlabel("Student")
            ax.set_ylabel("Hours / Day")
            ax.set_title("Study Hours by Student")

            plt.xticks(rotation=35)
            ax.legend()

            st.pyplot(fig)

            # ------------------------------------------------
            # TOP STUDY TIME
            # ------------------------------------------------

            highest_student = study_data.loc[
                study_data[study_value].idxmax(),
                study_student
            ]

            lowest_student = study_data.loc[
                study_data[study_value].idxmin(),
                study_student
            ]

            st.success(
                f"Highest study time: **{highest_student}**"
            )

            st.info(
                f"Lowest recorded study time: **{lowest_student}**"
            )

            st.markdown(
                '<div class="insight-box">'
                '<b>💡 Learning Insight</b><br>'
                'Study time can provide useful context for '
                'understanding academic performance, but '
                'study hours alone do not establish causation.'
                '</div>',
                unsafe_allow_html=True
            )

        else:

            st.warning(
                "No valid study-hour data available."
            )

    else:

        st.warning(
            "Study-hour columns could not be detected."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Student Performance Analyzer • "
    "Python | Pandas | Matplotlib | Streamlit"
)