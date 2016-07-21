answer = 0
while answer == 0:
	print("left o right mate?")
	user_input = input()
	if user_input == "left":
		print("yay left")
		answer = 1
	elif user_input == "right":
		print("woo right")
		answer = 1
	else:
		print("that was not an option")
print("eyy we made it out")