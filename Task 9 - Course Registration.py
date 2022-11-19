#Name: EP Learning Institution Course Registry.py
# Author: Estalin Peña
# Date Created: october 27, 2022
# Date Last Modified: october 28, 2022
#A program to allow users to register in a course

import os



print("\t","\t","\t","Welcome to EP Learning Institution!")#Welcome Message for the user
print(" - " *40)#Space dash to delimit the information displayed
print("Please introduce your information in the fields below and select your courses.")#This asks the user to introduce its information and course selection
print(" - " *40)#Space dash to delimit the information displayed

firstName = input("Please enter your first name: ")#This takes the first name of the user
lastName = input("Please enter yoru last name: ")#This takes the last name of the user
studentNumber = input("Please enter your student number: ")#This takes the student number
student_info = [firstName, lastName, studentNumber]#This variable takes all the student information
separator = " " #This variable is used as a separator by spaces
dash = " - " #This variable is used as a dash separator as well
print(" - " *40)#Space dash to delimit the information displayed
print("Please choose which course you'd like to register in: ")#Display a message to the user indicating to select the courses
courseCodes = {1 :'ENG123', 2 :'HIS456', 3: 'PROG789', 4: 'MATH639'}#Course codes 
courseName = {"ENG123": "English Class", "HIS456": "History of the Americas", "PROG789": "Programming III", "MATH639": "Mathematics"}#Course codes and courses names

for i, v in courseCodes.items():#this iterates the course codes and prints the selection of the user
    print(str(i) + " - " + v)

print(" - " *40)#Space dash to delimit the information displayed



courseSelection= input("Select your courses: ")#This is the input for the curse selection
selectedCourses=[]#this list will update after the user selects the courses

while courseSelection == "":
    print("Your input is incorrect")
    confirmation = input("Write Y if you want to exit the program, write N if you want to make another selection:")
    if confirmation.upper().strip() == "NO" or confirmation.upper().strip() == "N":
        courseSelection= input("Select your courses: ")
        
    elif confirmation.upper().strip() == "YES" or confirmation.upper().strip() =="Y":
        quit

print(" - "*40)#Space dash to delimit the information displayed
iterate_list = courseSelection.split(",")#Separates the course selection by comma 
for x in iterate_list:#iterates the and update the course selection list
    selectedCourses.append(courseCodes.get(int(x)))


    while int(courseSelection) not in courseCodes:
        print("Your selection is wrong")
        input("The correct selection is from 1 to 4: ")
        break

                              
        

print("Student information:", separator.join(student_info))#prints and separtes the student information with a space
print ("Courses selected:") #Displays the courses selected
for v in selectedCourses:#iterates the selected courses and prints the course codes and course names.
    print(v + " - " + courseName.get(v))
print(" - " *40)#Space dash to delimit the information displayed




