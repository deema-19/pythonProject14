# """ITF 08 Final Project Attendance System
# # TODO 1 Enter your name and submission date
# Name :"Deema Junaina"
# Delivery Date :"31/8/2023"
# """


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
import uuid


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark


# class Student:
#     # TODO 3 define static variable indicates total student count $'$"$"$"$"$

#     # TODO 4 define a constructor which includes
#     # student_id (unique using uuid module)
#     # student_name (user input)
#     # student_age (user input)
#     # student_number (user_input)
#     # courses_list (List of Course Objects)
#     def __init__(self):


#
# import uuid
#

class Student:
    total_count = 0

    def __init__(self, student_name, student_age, student_number):

        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.course_list = []
        Student.total_count += 1

    #
    # #     # TODO 5 define a method to enroll new course to student courses list
    # #
    # #     # method to get_student_details as dict
    # #     def get_student_details(self):
    # #         return self.__dict__
    # #
    # #     # method to get_student_courses
    # #     def get_student_courses(self):
    #

    def enroll_new_course(self, course_name, course_mark):
        new_course = Course(course_name, course_mark)
        self.course_list.append(new_course)

    # TODO 6 print student courses with their marks
    # pass
    #
    #     # method to get student_average as a value
    #     def get_student_average(self):
    # def __inti__(self, marks):
    #     self.marks = marks
    #
    # def print_student_courses(self):
    #     for course in self.courses_list:
    #         print(f"Course: {course.course_name}, Marks: {course.course_mark}")
    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    # x = student.print_student_courses

    # TODO 7 return the student average
    def get_student_average(self):
        marks = [course.marks for course in self.course_list]
        if not marks:
            return 0

        total_sum = sum(marks)
        average = total_sum / len(marks)
        return average


# student = Student()

# #
# # in Global Scope
# # TODO 8 declare empty students list
students_list = []

# while True:
#
#     # TODO 9 handle Exception for selection input
#     selection = int(input("1.Add New Student\n"
#                           "2.Delete Student\n"
#                           "3.Display Student\n"
#                           "4.Get Student Average\n"
#                           "5.Add Course to student with mark.\n"
#                           "6.Exit"))
#

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit: \n"
                              "Enter Your Choice : "))


    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    #

    # TODO 10 make sure that Student number is not exists before
    if selection == 1:
        student_number = input("Enter Student Number")

        if any(student.student_number == student_number for student in students_list):
            print("The student number already exists.")
            continue

        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except ValueError:
                print("Invalid Value")
        new_student = Student(student_name, student_age, student_number)
        students_list.append(new_student)
        print("Student Added Successfully")
    #         # TODO 11 create student object and append it to students list
    #
    #         print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number")
        index_to_remove = None
        for index, student in enumerate(selection):

            if student.student_number == student_number:
                index_to_remove = index
                break

        if index_to_remove is not None:
            removed_student = students_list.pop(index_to_remove)
            print(f"Student {removed_student.student_name} with student number {student_number} has been deleted.")
        else:
            print("Student not found with the given student number.")

    #  # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
    elif selection == 3:

        student_number = input("Enter Student Number to Display: ")

        target_student = None
        for student in students_list:
            if student.student_number == student_number:
                target_student = student
                break

        if target_student is not None:
            print("Student Information:")
            print("Student Number:", target_student.student_number)
            print("Student Name:", target_student.student_name)
            print("Student Age:", target_student.student_age)
        else:
            print("Student not found with the given student number.")

    # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
    #
    # if selection == 4:
    #     student_number = input("Enter Student Number")
    #
    #
    # elif selection == 4:
    #     student_number = input("Enter Student Number to Calculate Average: ")
    elif selection == 4:
        student_number = input("Enter Student Number")
    # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
    target_student = None
    for student in students_list:
        if student.student_number == student:
            target_student = None
            break



    if target_student is not None:
        while True:
            course_name = input("Enter Course Name (or 'exit' to finish): ")
            if course_name.lower() == "exit":
                break

            try:
                course_mark = float(input("Enter Course Mark: "))
                target_student.enroll_new_course(course_name, course_mark)
                print(
                    f"Course {course_name} with mark {course_mark} added to student {target_student.student_name}'s courses.")
            except ValueError:
                print("Invalid input. Please enter a valid course mark.")
        else:
            print("Student not found with the given student number.")

    # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        target_student = None
        for student in students_list:
            if student.student_number == student_number:
                target_student = student
            break

        if target_student is not None:
            average = target_student.get_student_average()
            print(f"Student {target_student.student_name}'s average: {average}")
        else:
            print("Student not found with the given student number.")


    elif selection == 6:
        print("Exiting the program.")
        break

    else:
        print("Invalid selection. Please choose a valid option.")

# TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
# # TODO 16 call a function to exit the program
#         pass
#
# TODO 16
#    elif selection == 6:
#     # TODO 16
#     print("Exiting the program.")
#     break

