import random
sauce_list = ["lemon", "rice", 
				"tabasco", "tapatillo", 
				"sriracha", "chili", 
				"lime", "water",
				"peanut", "hoy sin"]
main_list = ["chicken", "cow", 
				"duck", "unicorn", 
				"crab", "unagi", 
				"masago", "table",
				"salmon", "clam"]
style_list = ["steamed", "beaten", 
			"tender", "brutally murdered",
			"boiled", "stir fry",
			"walked on", "imaginary",
			"fried", "volcano rotisserie"]
var = 0
while var < 10:
	main_list[var] = input("enter a protein ")
	var += 1
var = 0
while var < 10:
	style_list[var] = input("enter a style of cooking ")
	var += 1
var = 0
while var < 10:
	sauce_list[var] = input("enter a sauce ")
	var += 1
print("on our menu tonight we have:")
var = 1
for i in range(20):
	random_number = random.randint(0,9)
	random_number2 = random.randint(0,9)
	random_number3 = random.randint(0,9)
	print(var)
	print(style_list[random_number] +" " + main_list[random_number3] + " with " + sauce_list[random_number2] + ".")
	var +=1
print("input a menu number in order to veiw its price")

user_inputness = int(input())

price_list = ["50", "3,000.9", "1,284", "2.50", "400", "5", "789.12", "123,456,789", "1", "67"]

if user_inputness > 0:
	print("your menu item\'s price is: $" + price_list[random_number] + ".")
	