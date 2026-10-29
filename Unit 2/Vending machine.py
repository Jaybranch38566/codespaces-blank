def vendingmachine():
	print("welcome to the vending machine")
	print("please select a snack")
	print("Nacho_chips=B3")
	print("BBQ_chips=G4")
	print("Plain_chips=G7")
	print("Water=D3")
	print("Cola_soda=G5")
	print("Please select a snack by entering the corresponding code:")
	snack_code=input()
	if snack_code=="B3":
		print("You have selected Nacho chips!")
	elif snack_code=="G4":
		print("You have selected BBQ chips!")
	elif snack_code=="G7":
		print("You have selected Plain chips!")
	elif snack_code=="D3":
		print("You have selected Water!")
	elif snack_code=="G5":
		print("You have selected Cola soda!")
	else:
		print("Invalid selection. Please try again.")
	print("Dispensing item...")
	print("Thank you for your purchase!")

vendingmachine()