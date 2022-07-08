import cv2
import argparse
import os

from utils.utils_for_one_json import *
from model.detect_pose import *

# Initialize a variable to store the duration.
frame_counter = 0
second_index = 0
time1 = 0
time2 = 0
list_of_frames = []

#==================================================#
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--video', help='Path to video file')
args = parser.parse_args() 

video_path = args.video
# video_path = "push-up3.mp4"
#==================================================#

video_name = os.path.basename(video_path).split('.')[0]

#function for video
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1) 
 
# Initialize the VideoCapture object to read from a video stored in the disk.
video = cv2.VideoCapture(video_path)
print(video)
 
# Iterate until the video is accessed successfully.
while video.isOpened():
    
    # Read a frame.
    ok, frame = video.read()
    
    # Check if frame is not read properly.
    if not ok:

        # Break the loop.
        break
    
    # Flip the frame horizontally for natural (selfie-view) visualization.
    frame = cv2.flip(frame, 1)
    
    # Get the width and height of the frame
    frame_height, frame_width, _ =  frame.shape
    
    # Resize the frame while keeping the aspect ratio.
    frame = cv2.resize(frame, (int(frame_width * (640 / frame_height)), 640))
    
    # Perform Pose landmark detection.
    frame, Landmarks = detectPose(frame, pose_video, display=False)
      
    list_of_frames.append(Landmarks)
    frame_counter = frame_counter + 1


create_one_json_file(list_of_frames, video_name)
print(frame_counter)
