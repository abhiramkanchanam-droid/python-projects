"""Calculate student marks, percentage and grade."""

def calculate_grade(percentage):
    """Return grade based on percentage."""

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def main():
    """Read student details and display the grade."""

    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    number = int(input("Enter number of subjects: "))

    marks = []

    for i in range(number):
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / number

    grade = calculate_grade(percentage)

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n----- STUDENT GRADE REPORT -----")
    print("Student Name :", name)
    print("Roll Number  :", roll_no)
    print("Total Marks  :", total)
    print("Percentage  :", percentage, "%")
    print("Grade        :", grade)
    print("Result       :", result)


if __name__ == "__main__":
    main()