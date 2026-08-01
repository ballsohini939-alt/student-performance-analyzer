print("=" * 40)
print("      STUDENT PERFORMANCE ANALYZER")
print("=" * 40)

student_name = input("Enter your name: ")

while True:
    try:
        number_of_subjects = int(input("Enter number of subjects: "))

        if number_of_subjects > 0:
            break

        print("Please enter at least 1 subject.")

    except ValueError:
        print("Please enter a valid number.")


subjects = {}

for i in range(number_of_subjects):

    subject_name = input(f"Enter subject {i + 1} name: ")

    while True:
        try:
            marks = float(input(f"Enter marks for {subject_name}: "))

            if 0 <= marks <= 100:
                break

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    subjects[subject_name] = marks


total_marks = sum(subjects.values())
percentage = total_marks / number_of_subjects


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


highest_subject = max(subjects, key=subjects.get)
lowest_subject = min(subjects, key=subjects.get)


print("\n" + "=" * 40)
print("         PERFORMANCE REPORT")
print("=" * 40)

print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

print(f"Highest Scoring Subject: {highest_subject}")
print(f"Lowest Scoring Subject: {lowest_subject}")

print("\nSubject-wise Marks:")

for subject, marks in subjects.items():
    print(f"{subject}: {marks:.2f}")

print("=" * 40)
print("       Analysis Complete!")
print("=" * 40)