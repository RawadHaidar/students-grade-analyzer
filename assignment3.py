import string

number_of_students = int(input("How many students do you want to enter for this class? "))
names = []
grades = []

print("Please enter the names and grades of the students:")
for i in range(number_of_students):
    
    print("Student", i + 1)
    name = input("Enter student name: ")
    names.append(name)
    while True:
        grade = float(input("Enter the student's grade: "))
        if grade < 0 or grade > 100:
            print("Invalid grade, please enter a value between 0 and 100.")
        else:
            grades.append(grade)
            break

def display_student_summary():
    print("-> Printing students' names and grades:")
    for i in range(number_of_students):
        print(f"{i+1}. Name: {names[i]}, Grade: {grades[i]}")
    print("\n")

def get_avg_grade():
    avg = (sum(grades) / len(grades))
    print("-> The class average grade is:", avg, "\n")

def get_highest_grade():
    max = grades[0]
    name = names[0]
    for i in range(number_of_students):
        if grades[i] > max:
            max = grades[i]
            name = names[i]
    print("-> Stundent",name,"has the highest grade:",str(max), "\n")

def count_passed():
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    print("-> The number of students who passed is:" , str(count), "\n")
print('\n')
stop_program = False
while not stop_program:
    print("Choose an option:")
    print("1. Display student summary")
    print("2. Get average grade")
    print("3. Get highest grade")
    print("4. Count passed students")
    print("5. Exit")
    choice = input("Enter you choice: ")
    if choice == '1':
        display_student_summary()
    elif choice == '2':
        get_avg_grade()
    elif choice == '3':
        get_highest_grade()
    elif choice == '4':
        count_passed()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("-> Invalid choice, please try again.\n")