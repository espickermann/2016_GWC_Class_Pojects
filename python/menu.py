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
print("on our menu tonight we have")
for i in range(20):
	random_number = random.randint(0,9)
	random_number2 = random.randint(0,9)
	random_number3 = random.randint(0,9)
	print(style_list[random_number] +" "+ sauce_list[random_number2] + " " + main_list[random_number3])