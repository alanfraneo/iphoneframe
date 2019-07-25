from PIL import Image, ImageOps
import numpy as np
from os import listdir, getcwd, makedirs
from os.path import isfile, join, exists, dirname, abspath
from multiprocessing import Pool
import time


def frame_image(file):
    scriptpath = dirname(abspath(__file__))
    frame = Image.open(scriptpath+"/vertical-frame.png")
    hframe = Image.open(scriptpath+"/horizontal-frame.png")

    try:
        image = Image.open(file)
    except OSError:
        print("can't read file", file)
        return

    if (image.size[0] > image.size[1]):
        frame = hframe
    left = int((frame.size[0] - image.size[0])/2)
    top = int((frame.size[1] - image.size[1])/2)
    newImage = ImageOps.expand(image, border=(left, top, left, top), fill=0)
    newImage.paste(frame, (0, 0), frame)
    outpath = getcwd()+'/framed/'
    if not exists(outpath):
        makedirs(outpath)
    newImage.save(outpath+image.filename,"PNG")
    print("framed: ", image.filename)


start = time.time()
print("started framing images in", getcwd())
onlyfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]

pool = Pool(15)
pool.map(frame_image, onlyfiles)
pool.terminate()
end = time.time()
print("All images framed successfully")
print("Total time taken to process images:", int(end-start), "seconds")


