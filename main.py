from student import Student
from analyzer import calculate_grade
from utils import save_student, view_students, search_student


def add_student():
    print("\n========== ADD STUDENT ==========")

    name = input("Enter student name: ").strip()
    student = Student(name)

    while True:
        try:
            number = int(input("Enter number of subjects: "))
            if number > 0:
                break
            print("Please enter at least one subject.")
        except ValueError:
            print("Please enter a valid number.")

    for i in range(number):
        subject = input(f"\nEnter subject {i + 1} name: ").strip()

        while True:
            try:
                marks = float(input(f"Enter marks for {subject}: "))

                if 0 <= marks <= 100:
                    student.add_subject(subject, marks)
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = student.total_marks()
    percentage = student.percentage()
    grade = calculate_grade(percentage)

    print("\n========== PERFORMANCE REPORT ==========")
    print(f"Student Name : {student.name}")
    print(f"Total Marks  : {total:.2f}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Highest      : {student.highest_subject()}")
    print(f"Lowest       : {student.lowest_subject()}")

    print("\nSubject-wise Marks")
    print("-" * 30)

    for subject, marks in student.subjects.items():
        print(f"{subject:<15}{marks:.2f}")

    save_student(student, grade)

    print("\nStudent record saved successfully!")


def show_menu():
    print("\n" + "=" * 40)
    print("     STUDENT PERFORMANCE ANALYZER")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")


def main():
    while True:
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            name = input("Enter student name to search: ")
            search_student(name)

        elif choice == "4":
            print("\nThank you for using Student Performance Analyzer.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()