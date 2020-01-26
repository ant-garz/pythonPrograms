# Author : Anthony Garza
#Purpose : The purpose of this program is to take in an integer from user input
#          and then utilizes multithreading in order to output all prime numbers
#          less than or equal to the number entered by the user in a new thread

import _thread
import time

#take in user input and then assign it to userInput
userInput = int(input('Please enter a number: '))

#empty array / list to store the prime numbers
primeArray = []

print("userInput =", userInput)

for i in range(2, (userInput+1)):
   isPrime = True
   # check if # is prime or not  
   for checkNum in range(2,int(i/2)+1):
      if i % checkNum == 0:
         isPrime = False
         break #break out if the number is not prime after flipping bool to false
   if isPrime:
      primeArray.append(i) #add number to list if prime

#dump to confirm contents before using new thread to print it
print("content of primeArray: ", primeArray)

def printPrime():
   print("new thread for output of prime numbers:")
   time.sleep(1) #wait a second to give the print action some time
   for i in primeArray:
      print(i)

#new thread with list of prime numbers to output
_thread.start_new_thread(printPrime, ())

