#!/usr/bin/env python3
"""
This program uses OpenCV 3 to get the amount of time passed between given
video frames using the framerate of the video and the number of frames in the
middle.
"""

import cv2

__author__ = "Parth Oza"
__status__ = "Development"

LEFT_KEY = ord("h")
RIGHT_KEY = ord("l")
SPACE_BAR = ord(" ")


def select_frame(frame_list, index=0):
    modifier = 1
    selected_frame = False
    while not selected_frame:
        frame = frame_list[index]
        cv2.imshow('frame', frame)
        k = cv2.waitKey(33)
        if k == LEFT_KEY:
            index -= 1 * modifier
        elif k == RIGHT_KEY:
            index += 1 * modifier
        elif k == SPACE_BAR:
            selected_frame = True
        elif k > -1 and chr(k).isdigit():
            modifier = int(chr(k))
        index = index % len(frames)
    return index


file_name = input("Enter file path: ").strip()

frames = []

video = cv2.VideoCapture(file_name)

first_frame = False
last_frame = False
frames_passed = 0

fps = video.get(cv2.CAP_PROP_FPS)

print("fps:", fps)
input_str = input("Enter real fps if this was wrong: ")
if len(input_str) > 0:
    fps = int(input_str)

print("total number of frames:", video.get(cv2.CAP_PROP_FRAME_COUNT))

print("Going through video, please wait.")

for i in range(int(video.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = video.read()
    if ret:
        frames.append(frame)

print("Enter a digit to set it to the multiplier for number of frames.")
print("Select the first frame, using the arrow keys to navigate and the")
print("spacebar to select.")

first_frame_index = select_frame(frames)

print("Select the second frame, using the arrow keys to navigate and the")
print("spacebar to select.")

last_frame_index = select_frame(frames, index=first_frame_index)

print("The amount of time that passed was " + str(fps / (
    first_frame_index - first_frame_index)) + " seconds.")
