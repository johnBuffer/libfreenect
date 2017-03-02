#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import numpy as np

cv2.namedWindow('Depth')
#cv2.namedWindow('RGB')
keep_running = True


def display_depth(dev, data, timestamp):
    global keep_running
    data2 = frame_convert2.pretty_depth_cv(cv2.resize(data, (0, 0), fx=0.25, fy=0.25))
    cv2.imshow('Depth', cv2.resize(data2, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST))
    if cv2.waitKey(10) == 27:
        keep_running = False


def display_rgb(dev, data, timestamp):
    global keep_running
    cv2.imshow('RGB', frame_convert2.video_cv(data))
    if cv2.waitKey(10) == 27:
        keep_running = False


def body(*args):
    if not keep_running:
        raise freenect.Kill


print('Press ESC in window to stop')
freenect.runloop(depth=display_depth,
                 video=None,
                 body=body)
