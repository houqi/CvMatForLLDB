# Function to visualize image quantities.
#
# 8/17/15


################################
# Imports.
################################

import sys
import cv2
import numpy as np


################################
# Check inputs.
################################

if len(sys.argv) < 2:
    print "Not enough arguments"
    sys.exit()
else:
    IMG_NAME = str(sys.argv[1])


################################
# Constants.
################################

SCALE_MIN = 1
SCALE_MAX = 8
MIN_SCALE_FOR_LINES = 4
MIN_SCALE_FOR_TEXT = 5


################################
# Initializations.
################################

img = cv2.imread(IMG_NAME)
size = img.shape[0], img.shape[1]

if len(img.shape) == 2:
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
grayScale = True
for r in range(0, size[0]):
    for c in range(0, size[1]):
        if (img[r, c, 0] != img[r, c, 1] or img[r, c, 0] != img[r, c, 2]):
            grayScale = False
grayScale = False
scale = SCALE_MIN
xMap = np.zeros(size, dtype=np.float32)
for r in range(0, size[0]):
    for c in range(0, size[1]):
        xMap[r, c] = c

yMap = np.zeros(size, dtype=np.float32)
for r in range(0, size[0]):
    for c in range(0, size[1]):
        yMap[r, c] = r


################################
# External methods.
################################

"""
onMouseEvent
"""
def onMouseEvent(event, x, y, flags, param):
    global scale, xMap, yMap
    pointX = xMap[y, x]
    pointY = yMap[y, x]

    # Change scale.
    scaleChanged = False
    if event == cv2.EVENT_LBUTTONDOWN:
        if scale < SCALE_MAX:
            scale = scale + 1
            scaleChanged = True
    elif event == cv2.EVENT_RBUTTONDOWN:
        if scale > SCALE_MIN:
            scale = scale - 1
            scaleChanged = True
    if scale == SCALE_MIN:
        xMap = np.zeros(size, dtype=np.float32)
        for r in range(0, size[0]):
            for c in range(0, size[1]):
                xMap[r, c] = c
        yMap = np.zeros(size, dtype=np.float32)
        for r in range(0, size[0]):
            for c in range(0, size[1]):
                yMap[r, c] = r

    # Compute new interpolation map.
    if scaleChanged:
        xBump = ()
        yBump = ()
        for r in range (0, size[0]):
            yMap[r, :] = np.round(pointY + (r - y) / np.exp2(scale-1))
            if (yMap[r, 0] == yMap[r-1, 0]) == False:
                yBump = yBump + (r,)
        for c in range (0, size[1]):
            xMap[:, c] = np.round(pointX + (c - x) / np.exp2(scale-1))
            if (xMap[0, c] == xMap[0, c-1]) == False:
                xBump = xBump + (c,)

        # Add lines for visualization.
        visualImg = cv2.remap(img, xMap, yMap, cv2.INTER_NEAREST)
        if scale > MIN_SCALE_FOR_LINES:
            for r in range(1, len(yBump)):
                visualImg[yBump[r], :] = 63
            for c in range(1, len(xBump)):
                visualImg[:, xBump[c]] = 63

        # Add text for visualization.
        if scale > MIN_SCALE_FOR_TEXT:
            for r in range(1, len(yBump)):
                for c in range(1, len(xBump)):
                    if grayScale:
                        cv2.putText(visualImg, (img[yMap[yBump[r]-1, xBump[c]], xMap[yBump[r]-1, xBump[c]], 0]).astype(str), (xBump[c], yBump[r]-3), cv2.FONT_HERSHEY_PLAIN, 0.4 * scale - 1.8, (0, 0, 0), 3)
                        cv2.putText(visualImg, (img[yMap[yBump[r]-1, xBump[c]], xMap[yBump[r]-1, xBump[c]], 0]).astype(str), (xBump[c], yBump[r]-3), cv2.FONT_HERSHEY_PLAIN, 0.4 * scale - 1.8, (0, 0, 255))
                    else:
                        cv2.putText(visualImg, (img[yMap[yBump[r]-1, xBump[c]], xMap[yBump[r]-1, xBump[c]], 0]).astype(str), (xBump[c], yBump[r]-3), cv2.FONT_HERSHEY_PLAIN, 0.4 * scale - 1.8, (0, 0, 0), 3)
                        cv2.putText(visualImg, (img[yMap[yBump[r]-1, xBump[c]], xMap[yBump[r]-1, xBump[c]], 0]).astype(str), (xBump[c], yBump[r]-3), cv2.FONT_HERSHEY_PLAIN, 0.4 * scale - 1.8, (255, 0, 0))
                        cv2.putText(visualImg, (img[yMap[yBump[r]-1, xBump[c]], xMap[yBump[r]-1, xBump[c]], 1]).astype(str), (xBump[c], yBump[r]-13 - 8 * (scale - 6)), cv2.FONT_HERSHEY_PLAIN, 0.4 * scale - 1.8, (0, 0, 0), 3)
                        cv2.putText(visualImg, (img[yMap[yBump[r]-1, xBump[c]], xMap[yBump[r]-1, xBump[c]], 1]).astype(str), (xBump[c], yBump[r]-13 - 8 * (scale - 6)), cv2.FONT_HERSHEY_PLAIN, 0.4 * scale - 1.8, (0, 255, 0))
                        cv2.putText(visualImg, (img[yMap[yBump[r]-1, xBump[c]], xMap[yBump[r]-1, xBump[c]], 2]).astype(str), (xBump[c], yBump[r]-23 -16 * (scale - 6)), cv2.FONT_HERSHEY_PLAIN, 0.4 * scale - 1.8, (0, 0, 0), 3)
                        cv2.putText(visualImg, (img[yMap[yBump[r]-1, xBump[c]], xMap[yBump[r]-1, xBump[c]], 2]).astype(str), (xBump[c], yBump[r]-23 -16 * (scale - 6)), cv2.FONT_HERSHEY_PLAIN, 0.4 * scale - 1.8, (0, 0, 255))
        cv2.imshow('Visualizer', visualImg)



################################
# Pipeline.
################################

cv2.namedWindow('Visualizer')
cv2.setMouseCallback('Visualizer', onMouseEvent)
visualImg = cv2.remap(img, xMap, yMap, cv2.INTER_NEAREST)
cv2.imshow('Visualizer', visualImg)
cv2.moveWindow('Visualizer', 100, 100)
cv2.waitKey(0)
cv2.destroyWindow('Visualizer')