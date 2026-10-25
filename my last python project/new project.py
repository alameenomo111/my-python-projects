class Student:
            def __init__(self,name,age,score):
                self.name = name
                self.age = age
                self.score = score
                    
            def about_student(self):
                print(f"Your name is {self.name},you are {self.age} years old")
                
            def calculate_grade(self):
                if self.score  >= 80:
                    print("A")
                elif self.score >= 65:
                    print("B")
                elif self.score >= 55:
                    print("C")
                elif self.score >= 50:
                    print("D")
                else :
                    print("F")


students = [] 
try:
    with open("students.txt", "r") as file:
        for line in file:
            name, age, score = line.strip().split(",")

            student = Student(name, int(age), int(score))
            students.append(student)

except FileNotFoundError:
    pass
while True:
    print("====== STUDENT MANAGEMENT SYSTEM =====")
    print("1.Add student,Age,Scores")
    print("2.View student")
    print("3.Search student")
    print("4. remove student")
    print("5.Calculate average score")
    print("6.view student who passed")
    print("7.Check number of student that already registered")
    print("8.Exit")
    try:

        choice = int(input("Enter your choice: "))
        print(f"You selected option {choice}" )

        if choice == 1:
            while True :
                student_name = input("Enter student you want to add: ")
                try:
                    student_age =  int(input("Enter your age: "))
                    student_score = int(input("enter student scores: "))

                except ValueError:
                    print("age and score must be numbers")
                    continue
                student1 = Student(student_name,student_age,student_score )

                student1.about_student()

                if student_name in students:
                    print("The student already exists")
                    print("Enter another name")
                else:
                    print("The student has been added")
                students.append(student1)
                with open("students.txt","a") as file:
                    file.write(f"{student1.name},{student1.age},{student1.score}\n")
                again = input("Do u want to add more student (yes/no): ")
                if again == "yes":
                    continue
                elif again == "no" :
                    break
        elif choice == 2:
            if not students:
                print("No student has registered yet.")
            else:
                print("\n===== REGISTERED STUDENTS =====")

                for student in students:
                    print(f"Name: {student.name}")
                    print(f"Age: {student.age}")
                    print(f"Score: {student.score}")
                    print(f"Grade: ", end="")
                    student.calculate_grade()
                    print("--------------------------")

        elif choice == 3:
            search_name = input("Enter student you want to search: ")
            found = False
            for student in students:
                if student.name.lower() == search_name.lower():
                    print("student found")
                    print(f"Age: {student.age}")
                    print(f"Score: {student.score}")
                    print("Grade: ", end="")
                    student.calculate_grade()

                    found = True
                    break

            if  not found:
                print("Student not found.")
        elif choice == 4:
            remove_student = input("Enter the student you want to remove: ")
            found = False
            for student in students:
                if student.name.lower() == remove_student.lower():
                    students.remove(student)
                    print(f"{remove_student} has been removed successfully! ✅")
                    found = True
                    break

            if  not found:
                print("Student not found.")
        elif choice == 5:

            print("Enter student 1st term 2nd term and third term score: ")

            first = int(input("1st term: "))
            second = int(input("2st term: "))
            third = int(input("3st term: "))
            total = first + second + third 
            average=total / 3
            print ("Your Total : ",total)
            print ("Your average : ",average)

            if total >= 50 and total <= 100:
                print("You are promoted to next class")
            else:
                print("you are repeating the current class")

        elif choice == 6:
            print(total > 50)

        elif choice == 7:
            print(len(students))

        elif choice == 8:
            print("thank you for coming")

            break
    except ValueError:
        print("Enter a valid number in the option")

    finally:
        print("student management finished checked finished!")
