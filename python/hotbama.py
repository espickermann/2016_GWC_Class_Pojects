from PIL import Image
im = Image.open("hot.jpg")
im.show()

pxl_list = list(im.getdata())
im.getcolors() 

print (im.getcolors())
for n,i in enumerate(pxl_list):
	if i > (121,121,121) and i < (182,182,182):
		pxl_list[n] = (218,112,214)
	if i < (60,60,60):
		pxl_list[n] = (147,112,219)	
	if i > (60,60,60) and i < (121,121,121):
		pxl_list[n] = (216,191,216)	
	if i > (182,182,182): 
		pxl_list[n] = (	200,31,216)


im2 = Image.new(im.mode, im.size)
im2.putdata(pxl_list)
im2.show()



	
	