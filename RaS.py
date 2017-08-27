#Pietro Biondi - Rename and Resize Image

from PIL import Image
import os

#Put your preference here
new_width = 646
new_height = 485

for dirname in os.listdir("."):
	if (dirname == ".git"):
		continue
	if os.path.isdir(dirname):
		for i, filename in enumerate(os.listdir(dirname)):
			pathIn = dirname + "/" + filename
			pathOut = dirname + "/" + str(i) + ".jpg"
			os.rename(pathIn, pathOut)

for dirname in os.listdir("."):
	if (dirname == ".git"):
		continue
	if os.path.isdir(dirname):
		for i, filename in enumerate(os.listdir(dirname)):
			pathIn = dirname + "/" + str(i) + ".jpg"
			pathOut = dirname + "/" + str(i) + "_scaled.jpg"
			photo = Image.open(pathIn)
			photo = photo.resize((new_width,new_height),Image.ANTIALIAS)
			photo.save(pathOut,optimize=True,quality=95)
			photo.close()