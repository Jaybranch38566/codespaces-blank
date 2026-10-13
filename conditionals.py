#Conditional if/else logic-these are keywords that instruct your data
#program to do specific instructions based on specific data
#or conditions
#conditional syntax (how it is written)
bill_amount = int(input("Please type in a number to tender(1s,5s,or 10s):"))
#if usally indicates that something is  possible option
if bill_amount==1:
print("here are 4 quaters")
#else is ALWAYS your last option.
else:
print("Sorry that type of bill is not accepted.")
#eliff allows us to indicate that there are no more possible options
#you can have as many eliff as you want
elif bill_amount==5:
print("here are 20 quaters")
elif bill_amount==10:
print("here are 40 quaters")
#else is ALWAYS your last option.
else:
print("Sorry that type of bill is not accepted.")
elif bill_amount==20:
print("Sorry we do not accept 20s. please enter an accepted amount")
elif bill_amount==10:
print("sorry we do not accept 100s.please enter accepted amount")
else:
print("Sorry that type of bill is not accepted.")

print "Program has started type in a number to add:)
num1=int(input())
num2=int(input())
print "Sory that number is not accepted.")


                         