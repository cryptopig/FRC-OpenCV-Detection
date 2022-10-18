import cv2 as cv # this singular line took 3 days to fix

'''
# IMAGE READING __________________________
# Points to photo of cone
img = cv.imread('Photos/cones2.jpg')

# Name and array size of pixels
cv.imshow('Cone', img)

# Waits for hotkey, time in miliseconds
cv.waitKey(0)
'''


# VIDEO READING __________________________

# Points to location of video file
capture = cv.VideoCapture('Videos/dog_shaving.mp4') # Capture is an instance of the VideoCapture class

# Reads video frame by frame
while True:
        isTrue, frame = capture.read() # uses capture.read() and cv.imshow() to display all frames
        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
                break

capture.release()
cv.destroyAllWindows()

