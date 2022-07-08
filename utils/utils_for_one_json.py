import json
import cv2
   
def create_json(list_of_frames, video_name):

    Points = {}

    if list_of_frames:
        start_file(video_name)

        for frame in range(len(list_of_frames)):

            # if frame is empty
            if not any(list_of_frames[frame]):
                handle_empty_frame(frame, video_name)

            # if frame not empty
            else:
                # Iterate 33 times to display all landmarks.    
                for i in range(33):
                    Points[i] = [
                        list_of_frames[frame][i][0],
                        list_of_frames[frame][i][1],
                        list_of_frames[frame][i][2]]

                #if this frame is not first frame            
                if frame:  
                    handle_not_empty_not_first_frame(video_name, Points)

                #if this frame is first frame  
                else:
                    handle_not_empty_first_frame(video_name, Points)
                      
        end_file(video_name)              
    
    handle_validation(video_name) 
#==================================================#  
# Dividing video into chunks 
#==================================================#        
def calculate_duration(video):
    duration_MSEC = video.get(cv2.CAP_PROP_POS_MSEC)
    time2  = duration_MSEC/1000
    return time2
#==================================================#  
def create_one_json_file(list_of_frames, video_name):
    # create file for every second
    create_json(list_of_frames, video_name)
    list_of_frames.clear()
#==================================================#
# Handling json file                               
#==================================================#   
def start_file(video_name):
    with open(f'{video_name}.json', 'a') as outfile:
        outfile.write('[')  
#==================================================#  
def end_file(video_name):              
    with open(f'{video_name}.json', "a") as outfile:
        outfile.write(']') 
#==================================================# 
def handle_empty_frame(frame, video_name):
        if frame:
            with open(f'{video_name}.json', 'a') as outfile:
                outfile.write(',\n')
                outfile.write('[]')
        else:
            with open(f'{video_name}.json', 'a') as outfile:
                outfile.write('[]')
#==================================================#  
def handle_not_empty_first_frame(video_name, Points):
    with open(f'{video_name}.json', 'a') as outfile:
        outfile.write(''.join(json.dumps(Points, separators=(',',':')))) 
#==================================================#  
def handle_not_empty_not_first_frame(video_name, Points):
    with open(f'{video_name}.json', 'a') as outfile:
        outfile.write(',\n')
        outfile.write(''.join(json.dumps(Points, separators=(',',':'))))
#==================================================# 
# Validation
#==================================================#    
def handle_validation(video_name):
    # Validate files
    with open(f'{video_name}.json') as outfile: 
        if ValidateJsonFile(outfile):
            print(f'{video_name}.json is valid')
        else:
            print(f'{video_name}.json is invalid') 
#==================================================#  
def ValidateJsonFile(jsonFile):
    try:
        json.load(jsonFile)
    except ValueError as error:
        print(error)
        return False
    return True
#==================================================#  