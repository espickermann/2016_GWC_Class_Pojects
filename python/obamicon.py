from PIL import Image
im = Image.open("hot.jpg")
im.show()
# ima = Image.new("RGB", (512, 512), "green")
# ima.show()
pxl_list = list(im.getdata())
im.getcolors() 

print (im.getcolors())
for n,i in enumerate(pxl_list):
	if i > (121,121,121) and i < (182,182,182):
		pxl_list[n] = (112,150,158)
	if i < (60,60,60):
		pxl_list[n] = (0,51,76)	
	if i > (60,60,60) and i < (121,121,121):
		pxl_list[n] = (217,26,33)	
	if i > (182,182,182): 
		pxl_list[n] = (252,227,166)
		
# pxl_list.replace(2,(217,26,33))
# Do something to the pixels...
im2 = Image.new(im.mode, im.size)
im2.putdata(pxl_list)
im2.show()

# if pxl_list < 182: 
	# pxl_list = [0,51,76] 


	
	