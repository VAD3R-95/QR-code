import sys
import re
from PIL import Image, ImageDraw
import zbarlight
import cv2
import numpy as np

img = cv2.imread('test.png')                                                           # your image to be read ,IMREAD_COLOR =  or 1,0..

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)                                 # convert to grayscale(binary image) 
cv2.imwrite('grayscaled.png', thresh)

edged = cv2.Canny(thresh, 50, 50)                                                        # edge detection
cv2.imwrite('edged.png', edged)

edged, contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)      # contour detection

contours = sorted(contours, key=cv2.contourArea, reverse = True)[:3]                             # ! since there are three big rectangles with contours quite
rect_count = 0                                                                                   #   big and hence differentiable than the others. 
for c in contours:                                                                               # we will detect abd draw the contour around that big finder pixel  
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02*peri, True)

    if len(approx) == 4:
        rect_count = approx                                                                      
    
    
im1 = cv2.drawContours(img, [rect_count], -1, (0,255,0), 3)


rows,cols,ch = img.shape

src_points = np.float32([[, ],[, ],[, ]])                                       #  affine transform of image around the detected pixel ! hit and trial values
dst_points = np.float32([[19, 217],[17, 280],[81, 281]])
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(thresh, affine_matrix, (cols,rows))
cv2.imwrite('image.png', img_output)

pts1 = np.float32([[,],[,],[,]])                                                                       # perspective trasnform of image to return a better percspective of image !more like focus
pts2 = np.float32([[0,0],[400,0],[0,400],[400,400]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img_output,M,(300,300))
cv2.imwrite('image.png', dst)


imag = cv2.imread('image.png')
kernel = np.ones((5, 5), np.uint8)
opening=cv2.morphologyEx(imag, cv2.MORPH_OPEN, kernel)                                       # remove stuff from background (false positives)
processed=cv2.morphologyEx(imag, cv2.MORPH_CLOSE, kernel)                                    # remove false negatives !morphological transforms
cv2.imwrite('image.png', processed)

img = 'image.png'
image = cv2.imread(img)
                                                                                            # flip/flop , translational , rotational transforms for alignment 
horizontal_img = cv2.flip(image, 0)                                                         # and better detection of qr code 
vertical_img = cv2.flip(image, 1)
both_img = cv2.flip(image, -1) 

cv2.imwrite('processed2.png', both_img)
cv2.imwrite('processed1.png', vertical_img)
cv2.imwrite('processed.png', horizontal_img)                                                 
  
file_path = 'processed1.png'
with open(file_path, 'rb') as image_file:                                                   # feed the qr code to zbarlight library
    image = Image.open(image_file)                      
    image.load()

codes = zbarlight.scan_codes('qrcode', image)
print('QR codes: %s' % codes)                                                              # print your qr codes

'''
edges=cv2.Canny(processed, 50, 50)          # edge detection
cv2.imwrite('edge.png', edges) 

(averaging)
kernel = np.ones((15,15), np.float32)/225 
smoothed = cv2.filter2D(img, -1, kernel)    # removing noise with 
                                              HUE range filter your !defined filter 
(gaussian blur)
blur = cv2.GaussianBlur(img, (15,15), 0)

(median blur)
median = cv2.medianBlur(img, 15)
'''
