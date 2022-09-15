import os
import glob
from PIL import Image

# Actually converts the images.
def convertIMG(imgPath):
    image1 = Image.open(fr"{imgPath}")
    convertedIMG = image1.convert("RGB")
    imgPath = imgPath.split(".")
    imgPath[1] = ".pdf"
    imgPath = imgPath[0] + imgPath[1]
    convertedIMG.save(fr"{imgPath}")

print("!!! Important !!! If you're not running the script in the exactly same directory the image is located, it's not gonna find the image, so you need to type the complete file path too.")

# Deals with values.
def howMany(value):
    pathes = []
    value+=1
    times = range(1, value)
    for i in times:
        if i == 1:
            pathes.append(input(f"Type the path for the first image: "))
        elif i == 2:
            pathes.append(input(f"Type the path for the second image: "))
        elif i == 3:
            pathes.append(input(f"Type the path for the third image: "))
        else:
            pathes.append(input(f"Type the path for the {i}th image: "))
    return pathes

# Main function: get how many images user will convert and calls the convertIMG function only if finds the file.
def main():
    imgList = []
    pathes = howMany(int(input("How many images do you want to convert? ")))
    for path in pathes:
        if path in glob.glob(f"{path}", recursive=True):
            print(f"File {path} encountered!")
            imgList.append(path)
        else:
            print(f"File {path} not found!")

    for img in imgList:
        convertIMG(img)
        print(f"File {img} converted to PDF.")

main()
