import raisedhandsmodule
import openpifpaf
import sys
import os
from PIL import Image, ImageFont, ImageDraw
import glob
import json


directory = sys.argv[1]

globallist = []
filescounter = 0
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		list = raisedhandsmodule.getlist(f)
		globallist = globallist + list
		filescounter = filescounter + 1









with open('allposes.json', 'w') as f:
	json.dump(globallist, f)

print('total files: ', filescounter)
