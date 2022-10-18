import cv2 as cv # this singular line took 3 days to fix

# IMAGE READING __________________________
# Points to photo of cone
img = cv.imread('Photos/cones2.jpg')

# Name and array size of pixels
cv.imshow('Cone', img)




# VIDEO READING __________________________

# Points to location of video file
capture = cv.VideoCapture('Videos/dog_shaving.mp4')

# Reads video frame by frame
while True:
        isTrue, frame = capture.read()

# Waits for hotkey, time in miliseconds
cv.waitKey(0)
