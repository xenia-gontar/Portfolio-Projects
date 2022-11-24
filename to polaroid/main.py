import cv2
import os
from PIL import Image

path_of_the_directory = os. getcwd()
ext = '.jpg'
num = 0
jpeglist = []
for files in os.listdir(path_of_the_directory):
    if files.endswith(ext):
        num += 1
        jpeglist.append(files)
    else:
        continue
print(f"Num of files is {num}")
print(f"The list of files is {jpeglist}")

names =["result.png", "result2.png", "res.png"]

# os.mkdir(path_of_the_directory + "/result")

for index in range(0, num - 1, 2):
    image = cv2.imread(jpeglist[index])

    y = 0
    x = 0
    w = image.shape[0]
    h = image.shape[0]  # height

    # if width is smaller than height
    # square image

    image_as_square = image[y:y + w, x:x + h]

    pic = cv2.resize(image_as_square, (809, 809))

    # cv2.imshow("Resized image", resized)

    # cv2.waitKey(0)
    #
    #
    # cv2.destroyAllWindows()

    borderoutput = cv2.copyMakeBorder(
        pic, 52, 320, 40, 40, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    cv2.imwrite('shitty_dpi.png', borderoutput)

    im = Image.open("shitty_dpi.png")
    im.save("good_dpi.png", dpi=(300, 300))
    os.remove("shitty_dpi.png")

    image = cv2.imread(jpeglist[index + 1])

    y = 0
    x = 0
    w = image.shape[0]
    h = image.shape[0]  # height

    # if width is smaller than height
    # square image

    image_as_square = image[y:y + w, x:x + h]

    pic = cv2.resize(image_as_square, (809, 809))

    # cv2.imshow("Resized image", resized)

    # cv2.waitKey(0)
    #
    #
    # cv2.destroyAllWindows()

    borderoutput = cv2.copyMakeBorder(
        pic, 52, 320, 40, 40, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    cv2.imwrite('shitty_dpi.png', borderoutput)

    im = Image.open("shitty_dpi.png")
    im.save("good_dpi1.png", dpi=(300, 300))
    os.remove("shitty_dpi.png")


    # showing the image with border

    # opening up of images
    img = Image.open("good_dpi.png")
    img1 = Image.open("good_dpi1.png")

    # creating a new image and pasting
    # the images
    img2 = Image.new("RGB", (1772, 1181), "white")

    # pasting the first image (image_name,
    # (position))
    img2.paste(img, (0, 0))

    # pasting the second image (image_name,
    # (position))
    img2.paste(img1, (886, 0))
    img2.save(path_of_the_directory + "/result/" + names[index], dpi=(300, 300))

    os.remove("good_dpi.png")
    os.remove("good_dpi1.png")

print("Succesfully finished!")

face_cascade = cv2.CascadeClassifier('ai.xml')
# Read the input image
img = cv2.imread('test.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
# (x, y) and (x, x + w)

# central x is x+ int(w/2)

# if central x < int(height/2)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
