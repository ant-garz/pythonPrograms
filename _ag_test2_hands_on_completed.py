#
#  Code 3 lines of comments with your name amd purpose
#  of the program
# The purpose of this program is to satisfy the test requirements
# This is to show that I understand decision and loop structures
# My name is Anthony Garza
num_of_classes = int(input("Enter number of classes, 1-6 :"))
#max and min variables for number of classes
max_class=6
min_class=1

# write code to ensure that num_of_classes is in the range 1-6
while num_of_classes < min_class:
    print('Invalid Entry!')
    num_of_classes = int(input("Enter number of classes, 1-6 :"))
while num_of_classes > max_class:
    print('Invalid Entry!')
    num_of_classes = int(input("Enter number of classes, 1-6 :"))
while num_of_classes >= min_class and num_of_classes <= max_class:
    print('You Entered', num_of_classes)
    break

print('--- end of program --')




