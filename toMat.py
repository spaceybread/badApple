import cv2 as cv
import time as t

frames = []
MAX_FRAMES = 6573
frame = 1

while frame < MAX_FRAMES:
    img = cv.imread(str(frame) + ".png")
    print("Processing frame {}...".format(str(frame)))
    matrix = []
    i = 0
    while i < 360:
        j = 0
        a = []
        while j < 480:
            b, g, r = (img[i][j])
            val = ""
            if r > 250:
                val = "0"
            else:
                val = " "
            a.append(val)
            j = j + 1
        matrix.append("".join(a))
        i = i + 1
    
    frames.append(matrix)
    frame = frame + 1

input("Processing complete... Press any key to start.")
frame = 1
while frame < MAX_FRAMES:
    print(frames[frame - 1])
    frame = frame + 1
    t.sleep(1/30)
