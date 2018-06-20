import cv2
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

### READING & WRITING IMAGE --------------------------
# Read
img = plt.imread('hopea_odorata5.jpg')
    # gray scale, two ways of doing it
img_gray = cv2.imread('hopea_odorata5.jpg',0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Writing
cv2.imwrite('img_hsv.jpg', img_hsv)


### BASICS --------------------------
    # dimensions
print('In RGB:', img.shape)
print('In GrayScale:',img_gray.shape)

    # cropping
img[:,80:370] #y-axis, x-axis

    # duplicate image
img2 = img.copy()



### PLOT --------------------------
    #subplot
fig, (ax1,ax2) = plt.subplots(ncols=2, nrows=1, figsize=(15, 10))
ax1.imshow(img);
ax2.imshow(img_gray);



### MERGING, SPLITTING, AMPLIFYING --------------------------
R, G, B = cv2.split(img)
    #increase red by 100
merged = cv2.merge([R+100, G, B])
plt.figure(figsize=(7,7))
plt.imshow(merged);

    #brightness & darkness
M = np.ones(image.shape, dtype = "uint8")*75 #create array of image with fixed values
bright = cv2.add(image, M)
dark = cv2.subtract(image, M)



### HISTOGRAM --------------------------
    #separate colors
color = ('b', 'g', 'r')
    #arg: image in [], color channel, mask image, histogram size, range
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,20])



### TRANSFORMATIONS --------------------------
    #rotation
    #rotation_center_x, rotation_center_y, theta, scale
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    #resize
    #image, dsize(output image size), x scale, y scale, interpolation
image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)



### DILATION, EROSION --------------------------
erosion = cv2.erode(image, kernel, iterations = 1)
dilation = cv2.dilate(image, kernel, iterations = 1)



### CONVOLUTIONS --------------------------
    #blurs
kernel_3x3 = np.ones((3, 3), np.float32) / 9
blurred = cv2.filter2D(image, -1, kernel_3x3) #custom blur with own kernel
blur = cv2.blur(image, (3,3))
Gaussian = cv2.GaussianBlur(image, (7,7), 0)
median = cv2.medianBlur(image, 5)
median = cv2.medianBlur(image, 5)
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
    #sharpen
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel_sharpening)



### THRESHOLDING --------------------------
    #manual threshold
    #THRESH_BINARY; THRESH_BINARY_INV; THRESH_TRUNC; THRESH_TOZERO; THRESH_TOZERO_INV
ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    #adaptive threshold
    #ADAPTIVE_THRESH_MEAN_C; THRESH_OTSU
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY, 3, 5) 


### EDGE DETECTION --------------------------
    #sobel: emphasize vertical & horizontal edge
sobel_x = cv2.Sobel(image, cv2.CV_64F, ksize=5)
    #canny: low error rate, well defined edges
canny = cv2.Canny(image, 50, 120)



### LINE, CIRCLE, BLOB DETECTION --------------------------
    # Run HoughLines using a rho accuracy of 1 pixel
    # theta accuracy of np.pi / 180 which is 1 degree
    # Our line threshold is set to 240 (number of points on line)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 240)

    #circle detection
circles = cv2.HoughCircles(blur, cv.CV_HOUGH_GRADIENT, 1.5, 10)

    #blob detection
detector = cv2.SimpleBlobDetector()
keypoints = detector.detect(image)
blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,255),
                                      cv2.DRAW_MATCHES_FLAGS_DEFAULT) #ensure blob size same as circle size
plt.imshow(blobs)

    #circle & ellipse detection
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True  # Set Area filtering parameters
params.minArea = 100
params.filterByCircularity = True # Set Circularity filtering parameters
params.minCircularity = 0.9
params.filterByConvexity = False # Set Convexity filtering parameters
params.minConvexity = 0.2
params.filterByInertia = True # Set inertia filtering parameters
params.minInertiaRatio = 0.01
detector = cv2.SimpleBlobDetector(params) # Create a detector with the parameters
keypoints = detector.detect(image) # Detect blobs
blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,0),# Draw blobs on our image as red circles
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
plt.imshow("Filtering Circular Blobs Only", blobs)



### CONTOURS --------------------------
    #hierarchy type: RETR_LIST, RETR_EXTERNAL, RETR_TREE = all contours, external contours only, full hierarchy
    #approximation method: CHAIN_APPROX_SIMPLE,CHAIN_APPROX_NONE = stores start & end bounding points, stores all bounding points
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(originalimage, contours, -1, (0,255,0), 3)
plt.imshow(image)



### VIDEO CAPTURE TO FRAME --------------------------
    #define a function to change the image
def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask
# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was sucessful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()   