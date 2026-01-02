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
    # Predefined values (NO user input)
    name = "Rakesh"
    department = "Computer Science"
    semester = "5"

    m1 = 78
    m2 = 85
    m3 = 72

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
