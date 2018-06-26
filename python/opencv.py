# Many codes were obtained from the Udemy course:
# Mastering Computer Vision OpenCV3 in Python & Machine Learning by Rajeev Ratan
# Do check it out!

import cv2
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

### READING & WRITING IMAGE --------------------------
# Read
img = plt.imread('hopea_odorata5.jpg') #read as BGR
B, G, R = cv2.split(img) #can change it to RGB so matplotlib can render properly
img = cv2.merge([R, G, B])
    # gray scale, two ways of doing it
img_gray = cv2.imread('hopea_odorata5.jpg',0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # LAB
brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
    # YCrCb
brightYCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)


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

    # create new dummy images
ones = np.ones(image.shape, dtype = "uint8") #all ones
blank = np.zeros((image.shape[0], image.shape[1], 3))



### PLOT --------------------------
    #subplot
fig, (ax1,ax2) = plt.subplots(ncols=2, nrows=1, figsize=(15, 10))
ax1.imshow(img);
ax2.imshow(img_gray);

    #draw shapes
cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2) #coordinate, color, thickness
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) #top left, top right coordinates, color, thickness
cv2.circle(image,(cx, cy), r, (255, 0, 0), -1) #centre coordinates, radius, color, -1 means fill the shape
cv2.ellipse(img,(cx,cy),(width,height),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))


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


### BITWISE CALCULATIONS --------------------------
# Intersect
And = cv2.bitwise_and(square, ellipse)
# Either Or
bitwiseOr = cv2.bitwise_or(square, ellipse)
# No Intersect
bitwiseXor = cv2.bitwise_xor(square, ellipse)
# Not
bitwiseNot_sq = cv2.bitwise_not(square)



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
kernel = np.ones((5,5), np.uint8)
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


### COLOR FILTERING --------------------------
# define range of PURPLE color in HSV
lower_range = np.array([125,0,0])
upper_range = np.array([175,255,255])

# Convert image from RBG/BGR to HSV so we easily filter
hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# Use inRange to capture only the values between lower & upper_values
mask = cv2.inRange(hsv_img, lower_range, upper_range)
# Perform Bitwise AND on mask and our original frame
res = cv2.bitwise_and(img, img, mask=mask)



### THRESHOLDING --------------------------
# For grayscale
# https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
    #manual threshold
    #THRESH_BINARY; THRESH_BINARY_INV; THRESH_TRUNC; THRESH_TOZERO; THRESH_TOZERO_INV
    #cv2.threshold(image, lower_range, upper_range, thresh_type)
ret,thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret,thresh = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY) # just isolate white color only
plt.imshow(thresh);
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

    #area
cv2.contourArea(contour)
    #centroid
cv2.moments(contours)
    #bounding box
x,y,w,h = cv2.boundingRect(c)
cv2.rectangle(orig_image,(x,y),(x+w,y+h),(0,0,255),2)   


#Approximate Contours
    #cv2.approxPolyDP(contour, Approximation Accuracy, Closed)
for c in contours:
    # Calculate accuracy as a percent of the contour perimeter
    accuracy = 0.03 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    cv2.imshow('Approx Poly DP', image)

#Convex Hull
for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)
    cv2.imshow('Convex Hull', image)

#Contour Matching
    #http://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html
    #cv2.matchShapes(contour template, contour, method, method parameter)
for c in contours:
    # Iterate through each contour in the target image and 
    # use cv2.matchShapes to compare contour shapes
    # methods = 1, 2 or 3
    match = cv2.matchShapes(template_contour, c, 3, 0.0)
    print match
    # If the match value is less than 0.15 we
    if match < 0.15:
        closest_contour = c
    else:
        closest_contour = []                 
cv2.drawContours(target, [closest_contour], -1, (0,255,0), 3)
cv2.imshow('Output', target)


### SEGMENTATION

# WaterShed
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_watershed/py_watershed.html



### OBJECT DETECTION --------------------------

#Template Matching
    #http://docs.opencv.org/2.4/modules/imgproc/doc/object_detection.html
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#Corner Detection
    # HARRIS CORNER
    # The cornerHarris function requires the array datatype to be float32
gray = np.float32(gray)
harris_corners = cv2.cornerHarris(gray, 3, 3, 0.05)
    #We use dilation of the corner points to enlarge them\
kernel = np.ones((7,7),np.uint8)
harris_corners = cv2.dilate(harris_corners, kernel, iterations = 2)
    # Threshold for an optimal value, it may vary depending on the image.
image[harris_corners > 0.025 * harris_corners.max() ] = [255, 127, 127]
plt.imshow(image)

    # GOOD FEATURES TO TRACK
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 150)



### FEATURE DETECTION --------------------------

#SIFT; patented, not in opencv3
sift = cv2.SIFT()
    #Detect key points
keypoints = sift.detect(gray, None)
print("Number of keypoints Detected: ", len(keypoints))
    # Draw rich key points on input image
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(image)

#SURF; patented, not in opencv3
surf = cv2.SURF()
    # Only features, whose hessian is larger than hessianThreshold are retained by the detector
surf.hessianThreshold = 500
keypoints, descriptors = surf.detectAndCompute(gray, None)
print "Number of keypoints Detected: ", len(keypoints)
    # Draw rich key points on input image
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(image)

#FAST
fast = cv2.FastFeatureDetector()
    # Obtain Key points, by default non max suppression is On
    # to turn off set fast.setBool('nonmaxSuppression', False)
keypoints = fast.detect(gray, None)
print "Number of keypoints Detected: ", len(keypoints)
    # Draw rich keypoints on input image
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#BRIEF
fast = cv2.FastFeatureDetector()
    # Create BRIEF extractor object
brief = cv2.DescriptorExtractor_create("BRIEF")
    # Determine key points
keypoints = fast.detect(gray, None)
    # Obtain descriptors and new final keypoints using BRIEF
keypoints, descriptors = brief.compute(gray, keypoints)
print "Number of keypoints Detected: ", len(keypoints)
    # Draw rich keypoints on input image
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#ORB; FAST + BRIEF
orb = cv2.ORB()
    # Determine key points
keypoints = orb.detect(gray, None)
    # Obtain the descriptors
keypoints, descriptors = orb.compute(gray, keypoints)
print("Number of keypoints Detected: ", len(keypoints))
    # Draw rich keypoints on input image
image = cv2.drawKeypoints(image, keypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


### OTHERS --------------------------
#inpainting
    #cv2.inpaint(input image, mask, inpaintRadius, Inpaint Method)
    #inpaint method: NPAINT_NS,INPAINT_TELEA = Navier-Stokes based method, Method by Alexandru Telea (better)
restored = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)


### MACHINE LEARNING --------------------------
# trained classifiers
# https://github.com/opencv/opencv/tree/master/data



### MOTION TRACKING --------------------------


### OBJECT TRACKING --------------------------



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