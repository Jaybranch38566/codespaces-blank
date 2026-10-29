#What is a Loops--> Code that repeats.
#While loops= a block code that repeats itself until the triggering
#condition is no longer TRUE. CAN BE INFINITE
#For loops= a type of loop(code block that repeats itself) BUT
#it only repeats itself upto a certain number of times.
#IT IS INFINITE
#THINK OF FOR LOOPS AS THE COUNTING LOOPS
#FOR LOOP SYNTAX
#1 stand for itterator= programmers decided make this the universial
#symbol for a placeholder for counting.
for i in range(1,5):
	print(i)
	for i in "school":
		print (i)
		#LIST --> A collection type that acts as a container for
		#multiple data types and pieces of data.
		#List Syntax
		#A list is written like a variable BUT after the equal assignment
		#symbol we use square brackets and put all of the data inside of them.
		fooditem1="popcorn"
		groceryList=["popcorn", "apples", "water", "chips", "fish", "celery"]
		print("I need to buy " + str(i))
		itemPrices = [10.00,20.00,13.25,7.95,349.00]
		tax=0.07
		for i in itemPrices:
			#I want to know how much in taces i need to pay on each item
			print("you will pay this in taxes: " + str(tax*i))
			semesterGrades=[90,100,78,76,74,82,84]
			for grade in semesterGrades:
				#I want to find ALL the grades lower than 85.
				if grade<85:
					print(grade)
				