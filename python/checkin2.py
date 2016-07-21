done = False

print("to end your list type 'done'")

main_list = []

while done == False:
	item = input("enter a grocery item ")
	if item == ("done"):
		done = True
	main_list.append(item)
if done == True:
	print("grocery list:" )
	print(main_list)
