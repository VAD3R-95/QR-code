'''
for refernce for ddiferent ctf`s and online cracks...(contact me ----VAD3R)
''
import os
import urllib.request
import re
import base64
import http.cookiejar
from PIL import Image, ImageDraw
import time
import zbarlight
import cv2
import numpy as np


def post(passw):
    entry={'metu':passw}                            # entering qrcode with  at metu place
    senddata = urllib.parse.urlencode(entry)
    return bytes(senddata, 'utf-8')



url = 'http://challenge01.root-me.org/programmation/ch7/'

start_time = time.time()
cj = http.cookiejar.CookieJar()                     # using httpcookiejar for automatic handling of cookies
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

req = urllib.request.Request(url)                    # GET request to ch7 page
resp = urllib.request.urlopen(req)
respData = resp.read()
    
print(cj)
print("############################")
print(respData)
print("############################")
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
for eachP in paragraphs:
    r = eachP
print (r)
                                                   # writing our image to a file
with open('quick.png', 'wb') as f:
    data = f.write(text)

                                                     
WHITE =(255,255,255)                                 # drawing finders square on corners
W=                                                  # your width height 
BLACK = (0,0,0)
image = Image.open("quick.png")
draw = ImageDraw.Draw(image)
for (x,y) in [(18, 18), (18,218), (218,18)]:
    draw.rectangle((x,y, , ),BLACK, BLACK)
    draw.rectangle((x+W,y+W, , ),WHITE, WHITE)
    draw.rectangle((x+2*W,y+2*W, , ),BLACK, BLACK)

image.save('result2.png')

'''

 transformation:                                # (optional)
 morhpological , translational, affine           # open saved image to transform the image 
 see:codes.py for more ;-)
 
'''

file_path = 'processed.png'                            
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()                                  # using zbarlight to read qr code

codes = zbarlight.scan_codes('qrcode', image)
print('QR codes: %s' % codes)



  

ans = post(qrcode)
print(ans)
answer = urllib.request.urlopen(url, ans)          # POST req to ch8 page with qrcode
raw = answer.read()
raw = raw.decode('utf-8')
print(raw)
    
print("--- %s seconds ---" % (time.time() - start_time))
