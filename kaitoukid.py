from PIL import Image

# RGB values for recoloring.
white = (245, 245, 245)
red = (217, 26, 33)
orange = (255, 69, 0)
yellow = (252, 227, 166)
lightBlue = (112, 150, 158)
darkBlue = (0, 51, 76)
green = (34, 139, 34)
purple = (153, 50, 204)
black = (0, 0, 0)

print("Please chose four colors - a dark color, a medium color, a light color, and a super light color.")
print("Your choices are white(245, 245, 245), red(217, 26, 33), orange(255, 69, 0), yellow(252, 227, 166), lightBlue(112, 150, 158), darkBlue(0, 51, 76), green(34, 139, 34), purple(153, 50, 204), and black(0, 0, 0).")
print("Type in the stuff in the ()")
dark = input("Dark Color: ")
medium = input("Medium Color: ")
light = input("Light Color: ")
super = input("Super Light Color: ")






# Import image.
my_image = Image.open("kaitoukid.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for rgb in image_list:
	newc = rgb[0] + rgb[1] + rgb[2]
	if newc < 182:
		recolored.append(black)
	elif newc < 364:
		recolored.append(white)
	elif newc < 546:
		recolored.append(green)
	else:
		recolored.append(yellow)
	
	
	


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"

