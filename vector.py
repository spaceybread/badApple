import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

input = "img/"
output = "output/"
images = sorted([f for f in os.listdir(input) if f.endswith(".png")])

for i in range(len(images)):
    if i % 10 == 0: print(i)
    pth = os.path.join(input, images[i])
    bw = cv2.imread(pth, cv2.IMREAD_GRAYSCALE)
    blah, bim = cv2.threshold(bw, 127, 255, cv2.THRESH_BINARY)
    edge = cv2.Canny(bim, 100, 200)
    out = os.path.join(output, images[i])
    plt.imsave(out, edge, cmap="gray")
    
print("DONE!")
