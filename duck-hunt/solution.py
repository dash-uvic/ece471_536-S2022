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
    # Using template matching, some images require diff shifting
    templates = []
    for i in range(1, 8):
        templates.append({"fileName": "./ims/a" + str(i) + ".png", "shift": True})
    for i in range(1, 4):
        templates.append({"fileName": "./ims/weird" + str(i) + ".png", "shift": False})

    coords = []
    for template in templates:
        templateImg = cv2.imread(template["fileName"], 0)
        h, w = templateImg.shape
        # This is a very innacurate, but fast method, so I'm trusting that in the sea of false positives, at some point it'll see each duck. Also TM_CCOEFF is just the one I found most accurate
        # I'm using an RCNN in another branch, which is amazing at finding the ducks, but it's wayyyy too slow to predict which makes it effectively useless in this case
        #   It's probaly due to my potato of a laptop, but this is a much surer bet
        # Don't get me started on the blue ducks on light backgrounds though, 4 of my 10 templates are specifically for that case, but I still can't detect them
        result = cv2.matchTemplate(cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY), templateImg, cv2.TM_CCOEFF)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        location = maxLoc

        # The weird shifting diff, mostly due to where the hit box is
        if template["shift"]:
            botRight = (int(location[1] + w), int(location[0]))
        else:
            botRight = (int(location[1]), int(location[0]))
        coords.append({'coordinate': botRight, 'move_type': move_type})

    return coords

