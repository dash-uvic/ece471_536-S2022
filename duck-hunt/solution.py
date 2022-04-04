import time
import os
import cv2
import numpy as np
import pygame

"""
Replace following with your own algorithm logic

Two random coordinate generator has been provided for testing purposes.
Manual mode where you can use your mouse as also been added for testing purposes.
"""
def GetLocation(move_type, env, current_frame):
    templates = []
    for i in range(1, 9):
        templates.append("./ims/a" + str(i) + ".png")

    coords = []
    for templatePath in templates:
        template = cv2.imread(templatePath, 0)
        h, w = template.shape
        result = cv2.matchTemplate(cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        location = maxLoc

        botRight = (int(location[1] + w), int(location[0]))
        coords.append({'coordinate': botRight, 'move_type': move_type})

    return coords

