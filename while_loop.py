#Loop- a loop is construct (special function) that repeats itsef.
#In programming, a loop allows to repeat code instructions.
#There are two types of loops:For loop and While  loop
#While loop-a type of loop where so long as a condition is equal
#to true it will keep running forever.
#the keyboard  is while --> do while
#syntax
num=4
while 2+2==num: #Condition --> operations-must be true
    print("the programs is running...")
    #While loops will ALWAYS run unless you change the conditon !
    #we can do this by writing instructions to manually change it.
    num=int(input("Please type in a number:"))

def guessingGame():
    correctanswer=12
correctanswer=12
attempts=0
attempts=0
print("GUESSING GAME HAS STARTED")
userGuess=input("Please guess a number between 1 and 50.")
while userGuess !=correctAnswer:
   print("Incorrect.Please try again...")
   attempts +=1
   print("guess attempts:  " +str(attempts))
   guessingGame()





   def passwordReset():
       correctPassword="1234"
       print("Please login with your password)...")
       attempts=4
       userPwAttempt=input()
       while userPwAttempt!=correctPassword:
           print("password incorrect.")
           print("try again...")
           print("Please log in with your Password...")
           userPwAttempt=input()
           passwordReset()
           attempts -=1
           print("You have "+str(attempts)+" attempts left.")
           userPwAttempt=input()
           print("Too many attempts,you have been locked out of your account.")
           print("welcome you have acess...")
           passwordReset()
