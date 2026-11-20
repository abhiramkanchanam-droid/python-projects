"""Calculate and display a student's result and grade."""

PASS_MARK = 40.0

def calculate_grade(average):
    """Return the grade based on average marks."""

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def get_marks(subject):
    """Read and validate subject marks."""

    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Enter a valid number.")


def main():
    """Display student result and grade report."""

    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    subjects = ["Python", "Mathematics", "Physics",
                "Chemistry", "English"]

    marks = []

    for subject in subjects:
        marks.append(get_marks(subject))

    total = sum(marks)
    average = total / len(subjects)

    if all(mark >= PASS_MARK for mark in marks):
        result = "PASS"
        grade = calculate_grade(average)
    else:
        result = "FAIL"
        grade = "F"

    print("\n----- STUDENT RESULT -----")
    print("Student Name :", name)
    print("Roll Number  :", roll_no)
    print("Total Marks  :", total, "/ 500")
    print("Average      :", round(average, 2))
    print("Result       :", result)
    print("Grade        :", grade)


if __name__ == "__main__":
    main()