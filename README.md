# QR-code
### QR code Processing and Detection (Python)
Here is a guide to scan and decode qrcodes/barcodes with opencv, python & zbarlight. It deals more with pre-processing of the image before feeding to the zbarlight for qr code detection rather than the algorithm involving with the scanning of the image.
So it's more of a image processing guide than qr decoding but nonetheless it works for both.

**To Further proceed you have to download the following on your system(preferably linux):grin:**
1. Install opencv if you already haven`t. I have worked with the opencv-python which you can install with pip on your system:

**sudo apt-get install python-opencv**
**pip3 install python-opencv**

Install the different dependencies and libraries etc... if any problem refer:[Opencv](http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)

2. Install zbar and zbarlight(python3 wrapper for zbar) to scan the image ,use the pip commands:

**apt-get install libzbar0 libzbar-dev**
**pip3 install zbarlight**

For any problem refer to [zbarlight](https://pypi.python.org/pypi/zbarlight)

The Image processing involves many differet functions resulting in a readable image. For simplicity we wil take some of the functions for a qr code image which may change depending upon the image you take but the logic to process the image will be more or less same. I would recommend watching this playlist befor continuing [OpenCV tutorial](https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq)

Read more about qr code : [Qrcode](https://en.wikipedia.org/wiki/QR_code)

**Following are the steps**
 
 1. Raw messed up image. *raw.png*
 
 2. The drawings are done with PIL draw function.*email.png*
 
 3. The image is converted to grayscale (binary) image first for better processing. *grayscaled.png*
 
 4. Performing geometric transformations on the image. *processed.png*, *edge.png*, *contour.png*
 
 5. Resizing image if needed *email.png*
 
 6. Note : thresholding , edging , contour detection , transformations will differ for different images. These are for refernce  and the output will chnange upon using the script. It is basically hit and trial for transformations after these methods.
 
 7. Feed the image to the zbarlight for reading the qr code .

Play with the image to get the qr code output and use the above images as reference.
After this the qr codes will properlly print (hopefully) on your python terminal.

Happy Cracking :metal:
