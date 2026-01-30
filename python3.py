# grade_calculator.py

def calculate_grade(marks):
    """
    Determines grade based on marks using nested conditions
    and logical operators.
    """
    # 5. Handle invalid marks using conditions
    if marks < 0 or marks > 100:
        return "Invalid marks! Marks should be between 0 and 100."

    # 7. Nested conditions to simulate business rules
    if marks >= 90:
        if marks >= 95:
            return "Grade A+ : Outstanding Performance 🌟"
        else:
            return "Grade A : Excellent Performance 🎉"

    elif marks >= 75 and marks < 90:
        return "Grade B : Very Good 👍"

    elif marks >= 60 and marks < 75:
        return "Grade C : Good 🙂"

    elif marks >= 40 and marks < 60:
        return "Grade D : Pass 🟡"

    else:
        return "Grade F : Fail ❌"


# 2. Take marks input from user
try:
    marks_input = input("Enter your marks (0-100): ")
    marks = float(marks_input)

    # 3, 4, 6. Determine grade and display message
    result = calculate_grade(marks)
    print(result)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
