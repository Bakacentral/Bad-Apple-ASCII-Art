import os
from PIL import Image
from natsort import natsorted
from time import sleep
import winsound

asciiChars = ["@", '*', "0", ".", "/", "%", "+", "=", ";", ",", "-", '#', '\'', '"', "'"]

def greyScale(image):
    return image.convert("L")

def resize(image, updatedWidth=50):
    width, height = image.size
    ratio = height / width * 0.5
    updatedHeight = int(updatedWidth * ratio)
    5
    resizedImage = image.resize((updatedWidth, updatedHeight))
    return resizedImage

def pixelsTOascii(image):
    pixels = image.getdata()
    characters = "".join([asciiChars[pixel // 25] for pixel in pixels])
    return characters

def playBadApple(updatedWidth=100):
    folderPath = r'D:\bad_apple_is\image_sequence'
    listofImages = natsorted(os.listdir(folderPath))
    winsound.PlaySound('Bad_apple.wav', winsound.SND_ASYNC)
    for images in listofImages:
        imagePath = os.path.join(folderPath, images)
        image = Image.open(imagePath)
        
        output = pixelsTOascii(greyScale(resize(image, updatedWidth)))
        pixelCount = len(output)
        asciiImage = "\n".join([output[index:(index + updatedWidth)] for index in range(0, pixelCount, updatedWidth)])
        print(asciiImage)
        sleep(0.0209)
playBadApple()

"""
Current issues 4/26: 
~~There is currently no implementation of music, I'm not sure if python can play music but I will be testing that out.~~
*used import winsound

~~Framerate does not sync up to the actual music video, need to see how many frames my code is running at and how many the actual video is running at.~~
~~There seems to be some moments where the code struggles to print out, causing slight lag in the printing process, this will cause it to go off sync from the video.~~
*Fixed by adding in sleep, which will manually slow down the code in order to match the time (this number was figured out through trial and error)*


Desired results: Somehow get the printed result to match the entire width python

~~Make it so that the images are actually printing in order, issue with how python reads the order of numbers .ie 10 comes before 2~~
"""
