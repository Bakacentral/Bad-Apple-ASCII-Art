import os
from PIL import Image
from natsort import natsorted

asciiChars = ["@", '*', "0", ".", "/", "%", "+", "=", ";", ",", "-", '#', '\'', '"', "'"]

def greyScale(image):
    return image.convert("L")

def resize(image, updatedWidth=160):
    width, height = image.size
    ratio = height / width * 0.6
    updatedHeight = int(updatedWidth * ratio)
    
    resizedImage = image.resize((updatedWidth, updatedHeight))
    return resizedImage

def pixelsTOascii(image):
    pixels = image.getdata()
    characters = "".join([asciiChars[pixel // 25] for pixel in pixels])
    return characters

def convert(updatedWidth=100):
    folderPath = r'D:\bad_apple_is\image_sequence'
    listofImages = natsorted(os.listdir(folderPath))  # Fixes ordering
    for image_name in listofImages:
        image_path = os.path.join(folderPath, image_name)
        image = Image.open(image_path)
        output = pixelsTOascii(greyScale(resize(image, updatedWidth)))
        pixelCount = len(output)
        asciiImage = "\n".join([output[index:(index + updatedWidth)] for index in range(0, pixelCount, updatedWidth)])
        print(asciiImage)
    
convert()
