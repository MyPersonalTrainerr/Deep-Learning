import cv2
import requests
import json
import mediapipe as mp
# from google.colab.patches import cv2_imshow
# import math
# import argparse
import numpy as np
from time import time
import matplotlib.pyplot as plt

counter =0
Flag = False
# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose
#connection bet points(Initializing mediapipe drawing class, useful for annotation.)
mp_drawing = mp.solutions.drawing_utils 

# Setting up the Pose function.
#pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)

#==================================================#
# parser = argparse.ArgumentParser()

# parser.add_argument(
#     '-v',
#     '--video',
#     help='Path to video file')

# args = parser.parse_args()
#==================================================#
# api-endpoint
# URL = ""
  
# # sending get request and saving the response as response object
# r = requests.get(url = URL)
  
# # extracting data in json format
# video_path = r.json()
video_path = "push-up3.mp4"
#==================================================#
def detectPose(image, pose, display=True):
    '''
    This function performs pose detection on an image.
    Args:
        image: The input image with a prominent person whose pose landmarks needs to be detected.
        pose: The pose setup function required to perform the pose detection.
        display: A boolean value that is if set to true the function displays the original input image, the resultant image, 
                 and the pose landmarks in 3D plot and returns nothing.
    Returns:
        output_image: The input image with the detected pose landmarks drawn.
        landmarks: A list of detected landmarks converted into their original scale.
    '''
    
    # Create a copy of the input image.
    output_image = image.copy()
    
    # Convert the image from BGR into RGB format.
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Perform the Pose Detection.
    results = pose.process(imageRGB)
    
    # Retrieve the height and width of the input image.
    height, width, _ = image.shape
    
    # Initialize a list to store the detected landmarks.
    landmarks = []
    
    # Check if any landmarks are detected.
    if results.pose_landmarks:
    
        # Draw Pose landmarks on the output image.
        mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks, connections=mp_pose.POSE_CONNECTIONS)
        
        # Iterate over the detected landmarks.
        for landmark in results.pose_landmarks.landmark:
            
            # Append the landmark into the list.
            landmarks.append((int(landmark.x * width), int(landmark.y * height), (landmark.z * width)))
    
    # Check if the original input image and the resultant image are specified to be displayed.
    if display:
    
        # Display the original input image and the resultant image.
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis('off');
        plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off');
        
        # Also Plot the Pose landmarks in 3D.
        mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
        
    # Otherwise
    else:
        
        # Return the output image and the found landmarks.
        return output_image, landmarks

#==================================================#        
def Creating_Json(Landmarks, counter):
    Points = {}
    if counter == 0:
        Flag = False
    else: 
        Flag = True
    if Landmarks:
        # Iterate two times as we only want to display first two landmark.    
        for i in range(33):
            # Display the found landmarks after converting them into their original scale.
            Points[i] = {
                    'x':Landmarks[i][0],
                    'y':Landmarks[i][1],
                    'z':Landmarks[i][2],
                    }
        if Flag:
            with open('Points.json', 'a') as outfile:
                outfile.write(',\n')
                outfile.write(''.join(json.dumps(Points, separators=(',',':'))))
        else:
            with open('Points.json', 'a') as outfile:
                outfile.write('[')
                outfile.write(''.join(json.dumps(Points, separators=(',',':'))))
#==================================================#        
#function for video

pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)
 
# Initialize the VideoCapture object to read from the webcam.
#video = cv2.VideoCapture(0)
 
# Initialize the VideoCapture object to read from a video stored in the disk.
video = cv2.VideoCapture(video_path)
 
 
# Initialize a variable to store the time of the previous frame.
# time1 = 0
 
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
    
    # json file
    Creating_Json(Landmarks,counter)
    counter = counter +1  
 
print(counter) 
with open("Points.json", "a") as outfile:
    outfile.write(']') 
      
    # Set the time for this frame to the current time.
    # time2 = time()
    
    # Check if the difference between the previous and this frame time &gt; 0 to avoid division by zero.
    # if (time2 - time1) > 0:
    # #if (time2 - time1) &gt; 0:
    #     # Calculate the number of frames per second.
    #     frames_per_second = 1.0 / (time2 - time1)
        
    #     # Write the calculated number of frames per second on the frame. 
    #     cv2.putText(frame, 'FPS: {}'.format(int(frames_per_second)), (10, 30),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    
    # # Update the previous frame time to this frame time.
    # # As this frame will become previous frame in next iteration.
    # time1 = time2  

    # Display the frame.
    #cv2_imshow(frame)
    
    
    # Wait until a key is pressed.
    # Retreive the ASCII code of the key pressed
    # k = cv2.waitKey(1) & 0xFF
    #k= cv2.waitkey(1)==ord('q')
    #k = cv2.waitKey(1) &amp; 0xFF  

    # Check if 'ESC' is pressed.
    # if(k == 27):
        
    #     # Break the loop.
    #     break
 
# Release the VideoCapture object.
# video.release()
 
# Close the windows.
# cv2.destroyAllWindows()   
