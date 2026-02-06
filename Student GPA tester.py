# Brooke Nafziger
# Student GPA tester

# program that accepts student names and GPAs
# program tests if student qualifies for Dean's List or Honor Roll
# app will:
    # ask and accept last name
    # quit if entered 'ZZZ'
    # ask and accept first name
    # ask and accept GPA as float
    # test GPA > 3.5 = Dean's List
        # print's Dean's List
    # test GPA > 3.25 = honor roll
        # print honor roll
# test with at least 5 students
# print final list of students entered

# set variables
last_name = ""
first_name = ""
gpa = 0.0
students = []

# loop to accept students until 'ZZZ' is entered
while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name == "ZZZ":
        break
    else:
        first_name = input("Enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))
        if gpa > 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa > 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} has not qualified for the Dean's List or Honor Roll.")
        students.append((first_name, last_name, gpa))

print("\nList of the students entered:")
for student in students:
    print(f"{student[0]} {student[1]} - GPA: {student[2]}")