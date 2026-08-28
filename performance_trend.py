import csv
import os
from datetime import datetime


HISTORY_FILE = "data/performance_history.csv"
STUDENT_FILE = "data/students.csv"


def _ensure_history_file():
    """Create the performance history file if it does not exist."""

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Percentage", "Grade", "Date"])


def record_performance(name, percentage, grade):
    """Save a student's current performance into history."""

    _ensure_history_file()

    today = datetime.now().strftime("%Y-%m-%d")

    with open(HISTORY_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        existing_records = list(reader)

    # Avoid duplicate record for same student,
    # same date and same percentage.
    for record in existing_records:
        if (
            record["Name"].strip().lower() == name.strip().lower()
            and record["Date"] == today
            and abs(float(record["Percentage"]) - float(percentage)) < 0.001
        ):
            return

    with open(HISTORY_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            f"{float(percentage):.2f}",
            grade,
            today
        ])


def _load_history():
    """Load all performance history records."""

    _ensure_history_file()

    with open(HISTORY_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def _load_current_student(name):
    """Find the current student record."""

    if not os.path.exists(STUDENT_FILE):
        return None

    with open(STUDENT_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if (
                student["Name"].strip().lower()
                == name.strip().lower()
            ):
                return student

    return None


def _get_student_history(name):
    """Return performance history for one student."""

    history = _load_history()

    records = []

    for record in history:
        if (
            record["Name"].strip().lower()
            == name.strip().lower()
        ):
            records.append(record)

    records.sort(key=lambda x: x["Date"])

    return records


def _get_trend(previous, current):
    """Determine performance trend."""

    difference = current - previous

    if difference > 0.5:
        return "Improving"

    if difference < -0.5:
        return "Declining"

    return "Stable"


def compare_current_performance(name):
    """
    Compare the latest historical performance
    with the student's current performance.
    """

    student = _load_current_student(name)

    if student is None:
        print(f"\nStudent '{name}' was not found.")
        return

    current_percentage = float(student["Percentage"])
    current_grade = student["Grade"]

    history = _get_student_history(name)

    # First performance record
    if not history:

        record_performance(
            student["Name"],
            current_percentage,
            current_grade
        )

        print("\nNo previous performance record was available.")
        print("The current performance has been saved as the first record.")

        print(
            f"\nCurrent Percentage : "
            f"{current_percentage:.2f}%"
        )

        print(
            f"Current Grade      : "
            f"{current_grade}"
        )

        return

    latest = history[-1]

    previous_percentage = float(latest["Percentage"])
    previous_date = latest["Date"]

    today = datetime.now().strftime("%Y-%m-%d")

    # Already recorded today
    if (
        previous_date == today
        and abs(previous_percentage - current_percentage) < 0.001
    ):

        print("\nCurrent performance is already recorded for today.")

        print(
            f"Percentage : "
            f"{current_percentage:.2f}%"
        )

        print(
            f"Grade      : "
            f"{current_grade}"
        )

        return

    difference = current_percentage - previous_percentage

    trend = _get_trend(
        previous_percentage,
        current_percentage
    )

    print("\n" + "=" * 60)
    print("                 PERFORMANCE TREND")
    print("=" * 60)

    print(f"\nStudent: {student['Name']}")

    print("\nPERFORMANCE COMPARISON")
    print("-" * 60)

    print(
        f"Previous Percentage : "
        f"{previous_percentage:.2f}%"
    )

    print(
        f"Current Percentage  : "
        f"{current_percentage:.2f}%"
    )

    print(
        f"Change              : "
        f"{difference:+.2f} percentage points"
    )

    print(
        f"Previous Grade      : "
        f"{latest['Grade']}"
    )

    print(
        f"Current Grade       : "
        f"{current_grade}"
    )

    print(
        f"Previous Date       : "
        f"{previous_date}"
    )

    print("\nTREND")
    print("-" * 60)

    if trend == "Improving":
        print("UP Improving")

    elif trend == "Declining":
        print("DOWN Declining")

    else:
        print("SAME Stable")

    print("\nTREND INSIGHT")
    print("-" * 60)

    if trend == "Improving":

        print(
            f"{student['Name']} has shown "
            "improvement in academic performance."
        )

        print(
            "Continue maintaining the current "
            "study routine."
        )

    elif trend == "Declining":

        print(
            f"{student['Name']} has experienced "
            "a decline in academic performance."
        )

        print(
            "Focus on weaker subjects and "
            "maintain consistent practice."
        )

    else:

        print(
            f"{student['Name']}'s performance "
            "is currently stable."
        )

        print(
            "Continue regular practice to "
            "achieve further improvement."
        )

    print("\n" + "=" * 60)

    # Save current performance
    record_performance(
        student["Name"],
        current_percentage,
        current_grade
    )


def display_performance_history(name):
    """Display complete performance history."""

    student = _load_current_student(name)

    if student is None:
        print(f"\nStudent '{name}' was not found.")
        return

    history = _get_student_history(name)

    # Create first record if none exists
    if not history:

        record_performance(
            student["Name"],
            float(student["Percentage"]),
            student["Grade"]
        )

        history = _get_student_history(name)

    print("\n" + "=" * 60)
    print("              PERFORMANCE HISTORY")
    print("=" * 60)

    print(f"\nStudent: {student['Name']}")

    print("\nDate            Percentage      Grade")
    print("-" * 60)

    for record in history:

        print(
            f"{record['Date']:<16}"
            f"{float(record['Percentage']):<16.2f}"
            f"{record['Grade']:<10}"
        )

    print("-" * 60)

    if len(history) >= 2:

        first = float(history[0]["Percentage"])
        latest = float(history[-1]["Percentage"])

        total_change = latest - first

        print(
            f"\nOverall Change : "
            f"{total_change:+.2f} percentage points"
        )

        if total_change > 0.5:
            print("Overall Trend  : UP Improving")

        elif total_change < -0.5:
            print("Overall Trend  : DOWN Declining")

        else:
            print("Overall Trend  : SAME Stable")

    else:

        print(
            "\nMore performance records are "
            "needed to calculate a long-term trend."
        )

    print("\n" + "=" * 60)


def performance_trend_menu():
    """Display the performance trend menu."""

    while True:

        print("\n" + "=" * 50)
        print("          PERFORMANCE TREND")
        print("=" * 50)

        print("1. Compare Current Performance")
        print("2. View Performance History")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            name = input(
                "Enter student name: "
            ).strip()

            if name:
                compare_current_performance(name)

            else:
                print(
                    "\nStudent name cannot be empty."
                )

        elif choice == "2":

            name = input(
                "Enter student name: "
            ).strip()

            if name:
                display_performance_history(name)

            else:
                print(
                    "\nStudent name cannot be empty."
                )

        elif choice == "3":
            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-3."
            )


if __name__ == "__main__":
    performance_trend_menu()