from PIL import Image, ImageOps
import numpy as np
from os import listdir, getcwd, makedirs
from os.path import isfile, join, exists, dirname, abspath
from multiprocessing import Pool
import time


def couple_image(file):
    path = getcwd()+"/framed/"
    try:
        image = Image.open(path+file)
    except OSError:
        print("can't read file", file)
        return
    fname = file.split('.')[0]
    name, number = fname.split('~')
    if(int(number) == 1):   
        secondimage = Image.open(path+name+'~2.png')
        #landscape
        if (image.size[0] > image.size[1]): 
            newImage = ImageOps.expand(image, border=(0, 0, 0, secondimage.size[1]+500), fill=0)
            newImage.paste(secondimage, (0, image.size[1]+500), secondimage)
        else:
            #potrait
            newImage = ImageOps.expand(image, border=(0, 0, secondimage.size[0]+500, 0), fill=0)
            newImage.paste(secondimage, (image.size[0]+500, 0), secondimage)
        outpath = getcwd()+'/coupled/'
        print(outpath)
        print(name)
        if not exists(outpath):
            makedirs(outpath)
        newImage.save(outpath+name+".png","PNG")
        print("coupled: ", name+".png")
    

start = time.time()
workingdir = getcwd()+'/framed/'
print("started coupling images in", workingdir)
onlyfiles = [f for f in listdir(workingdir) if isfile(join(workingdir, f))]
pool = Pool(15)
pool.map(couple_image, onlyfiles)
pool.terminate()
end = time.time()
print("All images coupled successfully")
print("Total time taken to process images:", int(end-start), "seconds")


