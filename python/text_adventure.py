start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant labrynth.
A sign is hanging from the slimy wall: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left. Also just so you know your current total health is 100
'''

health = 100
print(start)
done = ("game over")


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
	answer = 0
	while answer == 0:
		print("You decide to go left and you run into a troll")
		user_input = input("do you fight the troll, yes or no?	")
		if user_input == "yes":
			print("sorry dude your totally dead")
			done = True
			answer += 1
		elif user_input == "no":
			print("congrats you live")
			print("you continue down the mossy corridor")
			print("...")
			answer = 0
			while answer == 0:
				print("you come to a slimy river that crosses your cave")
				user_input = input("do you cross the river, yes or no?	")
				if user_input == "yes":
					print("sorry dude you are totally dead, armour is great but it doesnt float very well")
					done = True
					answer += 1
				elif user_input == "no":
					print("congrats you live")
					print("but whilst you were walking away from the river you tripped and fell")
					print("health:")
					health -= 5
					print(health)
					if health <= 0:
						done = True
					answer = 0
					while answer == 0 and health > 0:
						print("will you stop and 'patch up' your ankle or 'keep walking'?")
						user_input = input()
						if user_input == "patch up":
							print("wise decision")
							answer += 1
						elif user_input == "keep walking":
							print("for every step you take your health depletes by 6, your injury was worse than you thought")
							print("but remember whilst sitting you are vulnerable to any enemies that may find you")
							print("you take five steps")
							health -= 30
							print(health)
							if health <= 0:
								done = True
							if done == True:
								print("game over")
					answer += 1		
				else:
					print("that was not an option")
			answer +=1
		else:
			print("not an option bro")
elif user_input == "right":
	answer = 0
	while answer == 0:
		print("You choose to go right and you come to a slimy river that crosses your cave")
		user_input = input("do you cross the river, yes or no? ")
		if user_input == "yes":
			print("sorry dude your totally dead, armour is great but it doesnt float very well")
			done = True
			answer += 1
		elif user_input == "no":
			print("congrats you live")
			print("you turn around and discover the corridor has changed behind you")
			print("you enter the new corridor and you continue down it for some time")
			print("and some more")
			print("and some more")
			print("...")
			print("...")
			print("...")
			print("...")
			print("trust me this is a super long corridor")
			print("you run into a troll")
			print("do you fight the troll, yes or no?	")
			while answer == 0:
				user_input = input()
				if user_input == "yes":
					print("sorry dude your totally dead")
					done = True
					answer += 1
				elif user_input == "no":
					print("congrats you live, you successfully run around the troll and continue to sprint down the corridor")
					answer = 0
					while answer == 0:
						print("should you keep running? yes or no? if you stop you may be caught by the troll; however, if you keep going you will deplete your health by 5")
						user_input = input()
						if user_input == "yes":
							health -= 5
							print(health)
							answer += 1
						elif user_input == "no":
							print("the troll was not following you, you survive")							
							answer += 1
						else:
							print("that was not an option, yes or no???")
					answer += 1
				else: 
					print("that was not an option, you should die of dumbness but ill let you off this time")
			answer +=1		
		else:
			print("that was not an option")
else: 
	print("that was not an option, you die of dumbness")
	done = True
if health <= 0:
	done = True
if done == True:
	print("game over")

	
