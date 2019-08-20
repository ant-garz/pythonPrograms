# Author: Anthony Garza
# Purpose: The purpose of this program is to display information regarding
#          myself and my school semester, while properly utilizing
#          the heirarchy chart given to us as the standard regarding
#          nested functions.

#------------ function definition for main --------
def main():
    displayName()
    displayCourses()
    displayEnd()

#------------ function definition for displayName --------
def displayName():
    print ("My name is Anthony Garza")

#------------ function definition for displayCourses --------
def displayCourses():
    print("Classes for this semester :")
    print ("\t-\tCHM121")
    print ("\t-\tCIS115")
    print ("\t-\tHUM101")
    print ("\t-\tMTH132")

#------------ function definition for displayEnd --------
def displayEnd():
    print("\nI graduated from Waubonsee in 2016!")
    print("\nI will graduate from Lewis Univesity in 2020!")
    def displayHours():
      print('\nI am taking 14 credit hours this semester!')
    displayHours()
      
#--------------- invoke main function  ----
main()

