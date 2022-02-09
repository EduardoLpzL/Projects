#Step 1: Taking a image from the user
import argparse
import cv2
import numpy as np
import pandas as pd
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Image Path')
args = vars(ap.parse_args())
img_path = args['image']
#reading the image with openCV
img = cv2.imread(img_path)

clicked = False
r = g = b = xpos = ypos = 0

# Step2: Reading the file from pandas
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
csv = pd.read_csv('colors.csv', names=index, header=None)

#step4: Create the draw_function
## it will calculate the rgb values of the pixel which we couble click
def DrawFunction(event, x,y, flags, param):
    '''x,y are the coordinates of the mouse position'''
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

#step5: Calculate distance to get color name
## We need another function which will return us the color name from RGB values

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, 'R'])) + abs(G - int(csv.loc[i, 'G'])) +abs(B - int(csv.loc[i, 'B']))
        if (d <= minimum):
            minimum = d
            cname = csv.loc[i,'color_name']
    return cname

#step3: Set a mosue callback event on a window
    #create a window  in wchic the input image will display
cv2.namedWindow('image')
cv2.setMouseCallback('image', DrawFunction)


#Step7: Display the imagen on the window
while True:
    cv2.imshow('image',img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display ( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) +' B='+ str(b)
        print('Color:',getColorName(r,g,b))

        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

        clicked=False

    #Break the loop when user hits 'esc' key 
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()  