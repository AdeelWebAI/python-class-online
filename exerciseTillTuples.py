#1. create a program capable of displaying question to the users. #2. Use list data type to store the questions and their correct answers. 
#3. Display the final ammount the person is taking home after the game. 
question1 = "What is the capital of pakistan? :"
answer1 = "islamabad"
question2 = "what is the Manchester of pakistan ? :"
answer2 = "faisalabad"
question3 = "What is the name Largest city of pakistan ? :"
answer3 = "karachi"
questoins = [question1 , question2 , question3] 
winning_cash_amount = 10000
user_input = str(input(question1.title())) 
if user_input == answer1:
    print("Congratulations!,Move to the next question")
else:
    print("Sorry You answer is not correct ! Best of luck for next time") 
user_input = str(input(question2.title())) 
if user_input == answer2:
    print("Congratulations!,Move to the next question")
else:
    print("Sorry You answer is not correct ! Best of luck for next time") 
user_input = str(input(question3.title())) 
if user_input == answer3:
    print("Congratulations!, You have won the ammount", winning_cash_amount)
else:
    print("Sorry You answer is not correct ! Best of luck for next time") 