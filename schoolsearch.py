
# Schoolsearch Program: Meant to parse a file of students named "students.txt" and retrieve
#  various bits of data about a student based on input

# Authors: Griffin Cloonan, Nick Ponce, and Landon Woollard
# Date: April 6, 2018

import sys

# Print statement for testing
def print2(s):
   if(len(sys.argv) > 1 and sys.argv[1] == "-t"):
      return
   else:
      print s,

# Takes a criteria and a search type (0-7) and returns a list of strings representing students
# type:
#     0           1           2        3     4     5     6           7
# StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName
def queryStudentsByCriteria(criteria, search_type):
   try:
      file = open("students.txt", "r")
   except:
      print("Error opening file")
      exit()
   studentList = []
   for student in file:
      studentData = student.split(",")
      if studentData[search_type] == criteria:
         studentList.append(student)
   return studentList

# Takes an array of student data strings and prints the student's name, grade, classroom, and teacher
def printStudentDataByName(studentQuery):
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      print("Student: " + studentData[1] + " " + studentData[0] + "\nGrade: " + studentData[2] + "\nClassroom: " + studentData[3] + "\nTeacher: " + studentData[7][:-2] + " " + studentData[6])

# Takes an array of student data strings and prints the student's name and bus route
def printStudentBusData(studentQuery):
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      print "Student: " + studentData[1] + " " + studentData[0] + "\nBus Route: " + studentData[4]

# Takes an array of student data strings and prints the student's name
def printStudents(studentQuery):
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      print "Student: " + studentData[1] + " " + studentData[0]

# Takes an array of student data strings and prints the student's name
def printStudentsByBus(studentQuery):
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      print "Student: " + studentData[1] + " " + studentData[0] + "\nGrade: " + studentData[2] + "\nClassroom: " + studentData[3]

# Takes an array of student data strings, calculates the student with the highest gpa and prints their name, gpa, teacher, and bus route
def printHighestGPAStudent(studentQuery):
   highestGPAStudent = studentQuery[0].split(",")
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      if(float(studentData[5]) > float(highestGPAStudent[5])):
         highestGPAStudent = studentData
   print "Highest GPA Student: " + highestGPAStudent[1] + " " + highestGPAStudent[0] + "\nGPA: " + highestGPAStudent[5] + "\nTeacher: " + highestGPAStudent[7][:-2] + " " + highestGPAStudent[6] + "\nBus Route: " + highestGPAStudent[4]

# Takes an array of student data strings, calculates the student with the lowest gpa and prints their name, gpa, teacher, and bus route
def printLowestGPAStudent(studentQuery):
   lowestGPAStudent = studentQuery[0].split(",")
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      if(float(studentData[5]) < float(lowestGPAStudent[5])):
         lowestGPAStudent = studentData
   print "Lowest GPA Student: " + lowestGPAStudent[1] + " " + lowestGPAStudent[0] + "\nGPA: " + lowestGPAStudent[5] + "\nTeacher: " + lowestGPAStudent[7][:-2] + " " + lowestGPAStudent[6] + "\nBus Route: " + lowestGPAStudent[4]

# Takes an array of student data strings, calculates the average GPA for a grade and prints it out
def printAverageGPAForGrade(studentQuery, query):
   avgGPA = 0
   for s in range(0, len(studentQuery)):
      avgGPA += float(studentQuery[s].split(",")[5])
   if(len(studentQuery) > 0):
      print("Grade: %s\nAverage GPA: %.2f\n" % (studentQuery[0].split(",")[2], (avgGPA / len(studentQuery))))
   elif(len(studentQuery) == 0):
      print("Grade: %s\nAverage GPA: 0\n" % query)

# Prints the number of students in each grade level
def printStudentsPerGrade(studentsPerGrade):
   for grade in range(0, len(studentsPerGrade)):
      print("Grade %d: Students: %d\n" % (grade, studentsPerGrade[grade]))

def main():
   print2("Welcome to SchoolSearch")
   choice = ""
   name = ""
   dataQuery = ""
   studentsPerGrade = []
   while(choice.lower() != "q"):
      print2("\n\nEnter a letter to begin a search:\n")
      print2("   S[tudent]\n   T[eacher]\n   B[us]\n   G[rade]\n   A[verage]\n"
             "   C[lassroom]\n   E[nrollment]\n   I[nfo]\n   Q[uit]\n> ")
      try:
         choice = raw_input()
      except EOFError:
         return

      if(choice.lower() == "s"):
         print2("S[tudent]: <lastname> [B[us]]\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         parts = query.split()
         name = parts[0].upper()
         dataQuery = queryStudentsByCriteria(name, 0);
         if(len(parts) == 1):
            printStudentDataByName(dataQuery)
            #Valid format
            #Call function to search name and print details + class
         elif(len(parts) == 2):
            if(parts[1].lower() == "b"):
               #valid format
               printStudentBusData(dataQuery)
               #Call function to search name and print details + bus
            else:
               print("Invalid query.")
         else:
            print("Invalid query.")

      elif(choice.lower() == "t"):
         print2("T[eacher]: <lastname>\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         parts = query.split()
         name = parts[0].upper()
         dataQuery = queryStudentsByCriteria(name, 6);
         if(len(parts) == 1 and len(dataQuery) > 0):
            printStudents(dataQuery)
         else:
            print("Invalid query.")
         #function to search teacher name


      elif(choice.lower() == "b"):
         print2("B[us]: <number>\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         #function to search bus by number
         if(query.isdigit()):
            dataQuery = queryStudentsByCriteria(query, 4)
            printStudentsByBus(dataQuery)
         else:
            print("Invalid query.")

      elif(choice.lower() == "g"):
         print2("G[rade]: (<number> [H[igh]|L[ow]]) | (<number> <T[eacher]>)\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         parts = query.split()
         if(len(parts) > 2 or not parts[0].isdigit()):
            print("Invalid query.")
         elif(len(parts) == 2):
            #first entry is a number, check for valid H or L flags
            if(parts[1].lower() == "t"):
               print("Find all teachers who teach grade " + str(parts[0]) ) #NICK
            else:
               dataQuery = queryStudentsByCriteria(parts[0], 2)
               if(parts[1].lower() == "h"):
                  printHighestGPAStudent(dataQuery)
               elif(parts[1].lower() == "l"):
                  printLowestGPAStudent(dataQuery)
               else:
                  print("Invalid query.")
         else:
            #First entry is a number, no flags present
            dataQuery = queryStudentsByCriteria(parts[0], 2)
            printStudents(dataQuery)

      elif(choice.lower() == "a"):
         print2("A[verage]: <number>\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         #function to search GPA average by grade
         if(query.isdigit()):
            dataQuery = queryStudentsByCriteria(query, 2)
            printAverageGPAForGrade(dataQuery, query)
         else:
            print("Invalid query.")


      elif(choice.lower() == "i"):
         #function for grade by grade breakdown
         print2("I[nfo]")
         for grade in range(0, 7):
            dataQuery = queryStudentsByCriteria(str(grade), 2)
            studentsPerGrade.append(len(dataQuery))
         printStudentsPerGrade(studentsPerGrade)

      elif(choice.lower() == "c"):
         print2("C[lassroom]: <number> [T[eacher]]")
         try:
            query = raw_input()
         except EOFError:
            return
         parts = query.split()
         if(len(parts) > 2 or not parts[0].isdigit()):
            print("Invalid query.")
         elif(len(parts) == 2):
            if(parts[1].lower() == "t"):
               print("Find all teachers who use classroom number " + str(parts[0])) #NICK
            else:
               print("Invalid query.")
         else:
            print("List all students assigned to classroom number " + str(parts[0])) #NICK
      elif(choice.lower() == "e"):
         print("Output:\nClass number lowest, num students\n.\n.\n.\nClass number highest, num students") #NICK
      else:
         x = 6 #AKA DO NOTHING

   print2("Goodbye!")

if __name__ == "__main__":
    main()
