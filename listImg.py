from os import listdir, getcwd
from os.path import isfile, join
import json
import time
import datetime
import sys

onlyfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]

title = "NeoGallery"
if len(sys.argv) > 1:
    title = sys.argv[1]
wholeJson = []
imageid = 0
for file in onlyfiles:
	if file != '.DS_Store':
		image = {"imageID": imageid, "imageURL": "img/"+file}
		imageid = imageid+1
		wholeJson.append(image)

today = datetime.date.today()
imgConfig = {"Images":[{"pagename": title, "imgList": wholeJson}], "imageCount": imageid-1, "createdDate": today.strftime("%d %b, %Y"), "title": title}
output = json.dumps(imgConfig)
print("var imgconfig =",output+";")
