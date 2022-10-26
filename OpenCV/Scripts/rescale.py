import cv2 as cv # this singular line took 3 days to fix


# IMAGE READING __________________________

# Points to photo of cone
img = cv.imread('Photos/cones2.jpg')

# Name and array size of pixels
cv.imshow('Cone', img)

# Rescaling: Takes a frame and scales it by a scale value
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) # frame.shape[1] is width
    height = int(frame.shape[0] * scale) # frame.shape[0] is length

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Reads video frame by frame
capture = cv.VideoCapture('Videos/dog_shaving.mp4') # Capture is an instance of the VideoCapture class


while True:
        isTrue, frame = capture.read() # uses capture.read() and cv.imshow() to display all frames

        frame_resized = rescaleFrame(frame)
        cv.imshow('Video Resized', frame_resized)

        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
                break

capture.release()
cv.destroyAllWindows()




