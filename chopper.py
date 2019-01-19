from PIL import Image
strip = Image.open("2019-01-19.gif")
strip.load()
strip.show()

width, height = strip.size   # Get dimensions
panelW = 360
midX = width/2
cpyRt = 20
left0 = midX - panelW/2 - cpyRt

for i in range(3):
    left = left0 + (panelW + cpyRt) * i
    top = 0
    right = left + panelW + cpyRt
    right = min(right, width)
    bottom = height
    panel = strip.crop((left, top, right, bottom))
    panel.show()

#Display Image



#Applying Grayscale filter to image
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Saving filtered image to new file
#cv2.imwrite('graytest.jpg',img)
