def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    m1 = float(input("Enter marks of subject 1: "))
    m2 = float(input("Enter marks of subject 2: "))
    m3 = float(input("Enter marks of subject 3: "))

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Average Marks:", avg)
    print("Grade:", grade)


if __name__ == "__main__":
    main()