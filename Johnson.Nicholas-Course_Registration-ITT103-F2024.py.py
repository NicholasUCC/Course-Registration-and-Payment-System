
#Defining a class for the courses with the course ID couse Name and the cost of the course
class current_course:
    def __init__(self, course_id, course_name, cost):
        self.course_id = course_id
        self.course_name = course_name
        self.cost = cost
        
#Defining a class for students..
class Student:
    def __init__(self, student_id, course_name, email_address):
        self.student_id = student_id
        self.course_name = course_name
        self.email_address = email_address
        self.selected_courses = []
        self.balance = 0

#   Enroll function..checks if the student is alread in the selected course if not it add them
    def enroll(self, selected_course):
        if selected_course in self.selected_courses:
            raise ValueError(f"Student {self.course_name} is already enrolled in {selected_course.course_name}.")
        self.selected_courses.append(selected_course)
        self.balance += selected_course.cost
        
        
#returns the total cost..by iterating throught the cost of each course and adding them
    def get_total_cost(self):
        return sum(selected_course.cost for selected_course in self.selected_courses)
    
    
#RegistrationSystem Class...Iniatlizing a list and dictionary for the course and student
class RegistrationSystem:
    def __init__(self):
        self.selected_courses = []
        self.students = {}
        
# Adding a course after checking if the course doesnt alerady exists 
    def append_course(self, course_id, course_name, cost):
        for i in self.selected_courses:
            if i.course_id == course_id:
                raise ValueError(f"Selected course with ID {course_id} already exists.")
        full_course = current_course(course_id, course_name, cost)
        self.selected_courses.append(full_course)
        print(f"{course_name} added")

#Fuction to register student but first checking if theyre already registered then registering them
    def register_student(self, student_id, course_name, email_address):
        if student_id in self.students:
            raise ValueError(f"Student with ID {student_id} is already registered.")
        new_student = Student(student_id, course_name, email_address)
        self.students[student_id] = new_student
        print(f"{course_name} registered.")
        
#Fuction to errol a student but first checking if theyre already enroll before errolling them
    def enroll_in_selected_course(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        student = self.students[student_id]
        selected_course = next((c for c in self.selected_courses if c.course_id == course_id), None)
        if not selected_course:
            raise ValueError("Selected course not found.")
        student.enroll(selected_course)
        print(f"Student {student.course_name} enrolled in {selected_course.course_name}.")

#fuction to make and calculate payments 
    def calculate_payment(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        student = self.students[student_id]
        total_cost = student.get_total_cost()
        print(f"{student.course_name}: {total_cost}")
        payment = float(input(f"Enter Amount..the minimium amount is 40% of {total_cost}): "))
        if payment < total_cost * 0.4:
            raise ValueError("Payment must be at least 40% of the total cost.")
        student.balance -= payment
        print(f"Payment processed. balance: {student.balance}")
        
#fuction to check balance
    def check_student_balance(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        student = self.students[student_id]
        print(f"Balance{student.course_name} Balance = {student.balance}")
#function to show the courses
    def show_selected_courses(self):
        if not self.selected_courses:
            print("No selected courses available.")
        for selected_course in self.selected_courses:
            print(f"Selected course ID: {selected_course.course_id}, Name: {selected_course.course_name}, Cost: {selected_course.cost}")
#function to register a student..
    def show_registered_students(self):
        if not self.students:
            print("No students registered.")
        for student in self.students.values():
            print(f"Student ID: {student.student_id}, Name: {student.course_name}, Email: {student.email_address}")
#function to show the courses the student is in..
    def show_students_in_selected_course(self, course_id):
        selected_course = next((c for c in self.selected_courses if c.course_id == course_id), None)
        if not selected_course:
            print("Selected course not found.")
            return
        print(f"Students enrolled in {selected_course.course_name}:")
        for student in self.students.values():
            if selected_course in student.selected_courses:
                print(f"{student.course_name}")

 #the main function:
    # shows a menu and runs a function depending on the input.
    
    # The menu options 
    # adding a course
    # registering a student
    # enrolling a student in a course, 
    # processing payment
    # checking student balance
    # showing courses
    # showing registered students
    # showing students in a course
    # exiting the program.
    
def main():
    system = RegistrationSystem()

    while True:
        print("\n-- Menu --")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll Student in Course")
        print("4. Process Payment")
        print("5. Check Student Balance")
        print("6. Show Courses")
        print("7. Show Registered Students")
        print("8. Show Students in a Course")
        print("9. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        
            if choice == 1:
                course_id = input("Enter Course ID: ")
                course_name = input("Enter Course Name: ")
                cost = float(input("Enter Course Cost: "))
                system.append_course(course_id, course_name, cost)
            
            elif choice == 2:
                student_id = input("Enter student ID: ")
                course_name = input("Enter student Name: ")
                email_address = input("Enter student email: ")
                system.register_student(student_id, course_name, email_address)
            
            elif choice == 3:
                student_id = input("Enter student ID: ")
                course_id = input("Enter Course ID: ")
                system.enroll_in_selected_course(student_id, course_id)
            
            elif choice == 4:
                student_id = input("Enter student ID: ")
                system.calculate_payment(student_id)
            
            elif choice == 5:
                student_id = input("Enter student ID: ")
                system.check_student_balance(student_id)
            
            elif choice == 6:
                system.show_selected_courses()
            
            elif choice == 7:
                system.show_registered_students()
            
            elif choice == 8:
                course_id = input("Enter Course ID: ")
                system.show_students_in_selected_course(course_id)
            
            elif choice == 9:
                break
            
            else:
                print("no option selected try again")
        except Exception as e:
            print(f"Error: {e}")



# to run the code
if __name__ == "__main__":
    main()
    
#
#
#
#
#