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
    weirdTemplates = []
    for i in range(1, 7):
        templates.append({"fileName": "./ims/a" + str(i) + ".png", "shift": True})
    for i in range(1, 4):
        templates.append({"fileName": "./ims/weird" + str(i) + ".png", "shift": False})

    coords = []
    for template in templates:
        templateImg = cv2.imread(template["fileName"], 0)
        h, w = templateImg.shape
        result = cv2.matchTemplate(cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY), templateImg, cv2.TM_CCOEFF)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        location = maxLoc
        if template["shift"]:
            botRight = (int(location[1] + w), int(location[0]))
        else:
            botRight = (int(location[1]), int(location[0]))
        coords.append({'coordinate': botRight, 'move_type': move_type})

    return coords

