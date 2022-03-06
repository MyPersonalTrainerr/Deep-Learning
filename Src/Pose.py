import cv2
import mediapipe as mp
import argparse
import matplotlib.pyplot as plt
from utils import *

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose
#connection bet points(Initializing mediapipe drawing class, useful for annotation.)
mp_drawing = mp.solutions.drawing_utils 

# Setting up the Pose function.
#pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)

#==================================================#
parser = argparse.ArgumentParser()

parser.add_argument(
    '-v',
    '--video',
    help='Path to video file')

args = parser.parse_args() 

video_path=args.video
# video_path = "push-up3.mp4"
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
#function for video
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1) 
 
# Initialize the VideoCapture object to read from a video stored in the disk.
video = cv2.VideoCapture(video_path)
 
# Initialize a variable to store the duration.
SEC_Index = 0
counter = 0
duration_SEC1 = 0
Landmarks_list = []
 
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
    
    counter = counter +1  
    Landmarks_list.append(Landmarks)

    duration_MSEC = video.get(cv2.CAP_PROP_POS_MSEC)
    duration_SEC2  = duration_MSEC/1000
    print("in while loop")
    # Check the difference 
    if (int(duration_SEC2)  - int(duration_SEC1)) == 1:
      SEC_Index = int(duration_SEC2)
      print(duration_SEC2)
      # json file
      Creating_Json(Landmarks_list, SEC_Index)
      Landmarks_list.clear()

    duration_SEC1 = duration_SEC2   

if Landmarks_list:
    SEC_Index += 1
    print(SEC_Index)
    Creating_Json(Landmarks_list, SEC_Index) 

print(counter)
