import cv2
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#set image to variable
out = cv2.imread("red.png",-1)
#get height and width of original image
height,width,channels = out.shape
#reduce image size by weight and blur image
weight = 7
smaller_img = cv2.resize(out, (int(width/weight),int(height/weight))) 
blurred_img = cv2.GaussianBlur(smaller_img, (3, 3), 0)
#new heights of modified image
height_2, width_2, channels_2 = blurred_img.shape
#instantiate lists to be used later for regression analysis
left_x = []
right_x = []
right_y = []
left_y = []

#find the cones and split them into right side and left side
for y in range(height_2):
    for x in range(width_2):
        g = blurred_img[y,x][1]
        b = blurred_img[y,x][0]
        r = blurred_img[y,x][2]
        if r > 150 and g < 60 and b < 60:
            if x > int(width_2/2):
                        right_x.append(x*weight)
                        right_y.append(y*weight)
            else:
                left_x.append(x*weight)
                left_y.append(y*weight)
           
rx = np.array(right_x)
ry = np.array(right_y)

lx = np.array(left_x)
ly = np.array(left_y)
#regression for right side
slope, intercept, r_value, p_value, std_err = stats.linregress(rx, ry)
#regression for left side
slopel, interceptl, r_valuel, p_valuel, std_errl = stats.linregress(lx, ly)

#overlay lines onto image
for h in range(height):
     for w in range(width):
        if (h <= slope * w + intercept +5) and (h >= slope * w + intercept - 5):
            out[h,w] = [225,0,0]
        if (h <= slopel * w + interceptl + 5) and (h >= slopel*w + interceptl - 5):
             out[h,w] = [225,0,0]
        
cv2.imwrite('answer.png', out)
cv2.imshow('image',out)
cv2.waitKey(0)
cv2.destroyAllWindows()

