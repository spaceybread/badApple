import cv2
import os

out = "rendered.mp4"

input = "output/"
fps = 30
images = [str(i) + ".png" for i in range(1, 6573)]


first = os.path.join(input, images[0])
frame = cv2.imread(first)
height, width, channels = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(out, fourcc, fps, (width, height))

for image in images:
    image_path = os.path.join(input, image)
    frame = cv2.imread(image_path)
    video.write(frame)

video.release()
print("video made!")
