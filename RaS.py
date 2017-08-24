#rename and resize
from PIL import Image
import os
for dirname in os.listdir("."):
	if os.path.isdir(dirname):
		for i, filename in enumerate(os.listdir(dirname)):
			pathIn = dirname + "/" + filename
			pathOut = dirname + "/" + str(i) + ".jpg"
			os.rename(dirname + "/" + filename, pathOut)

for dirname in os.listdir("."):
	if os.path.isdir(dirname):
		for i, filename in enumerate(os.listdir(dirname)):
			pathIn = dirname + "/" + str(i) + ".jpg"
			#print pathIn
			pathOut = dirname + "/" + str(i) + "_scaled.jpg"
			#print pathOut 
			photo = Image.open(pathIn)
			photo = photo.resize((646,485),Image.ANTIALIAS)
			photo.save(dirname + "/" + str(i) + "_scaled.jpg",optimize=True,quality=95)
