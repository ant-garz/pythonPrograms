# script name: ag_assignment4_completed.py
# author: Anthony Garza\
# the purpose of this program is to utilize loops and access files in
# order to grade an exam. The file accessed is a user's answers that is
# then compared to a pre-determined list inside the program, here being the
# answer key. It then decides what is correct and incorrect, updates the score
# and displays the result of the exam for the user.





def main():
    # set up variables
    corr_ans_list = ["A", "C", "A", "A", "D", "B",
                     "C", "A", "C", "B", "A", "D",
                     "C", "A", "D", "C", "B", "B",
                     "D", "A"]
    user_ans_list = []
    corr_count = 0
    num_questions = 20

    #setup file variable and open the user_answers.txt file
    user_ans_list = open(r'c:\Doc\user_answers.txt').read().replace('\n', '')
    
    

    #code loop to process each element and grade the exam
    for i, j in zip(corr_ans_list, user_ans_list):
            if i == j:
                corr_count = corr_count + 1
            else:
                corr_corr = corr_count + 0
            
    #formatting output dislay    
    print("Q\tCorr\tYour\tStatus")
    print("#\tAnswer\tAnswer\n------------------------------")
    #set question numbers
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #display answers and status of answer
    for a, i, j in zip(numbers,corr_ans_list,user_ans_list):
        if i == j:
            print(a,'\t',i,'\t',j)
        else:
            print(a,'\t',i,'\t',j,'\tX')
        
    #code to process exam and display final score
    percent_corr = (corr_count/num_questions) * 100
    percent_corr_fmt = format(percent_corr, ".1f")
    print("\nGrade :", corr_count, "/", num_questions, " = ",
          percent_corr_fmt, sep="")

    #determine if student passed and display the result
    if percent_corr >= 75:
        print("Congratulations! You passed the Exam!")
    else:
        print("Sorry, you did not pass the exam.")

main()

    
