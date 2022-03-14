import json
# import os
# from natsort import natsorted
   
def Creating_Json(Landmarks_list, index):
    Points = {}
    if Landmarks_list:
        with open(f'Sec{index}.json', 'a') as outfile:
            outfile.write('[')

        for frame in range(len(Landmarks_list)):
            # if frame is empty
            if not any(Landmarks_list[frame]):
                if frame:
                    with open(f'Sec{index}.json', 'a') as outfile:
                        outfile.write(',\n')
                        outfile.write('[]')
                else:
                    with open(f'Sec{index}.json', 'a') as outfile:
                        outfile.write('[]')
                    
            # if frame not empty
            else:
                # Iterate 33 times to display all landmarks.    
                for i in range(33):
                    # Display the found landmarks after converting them into their original scale.
                    Points[i] = {
                            'x':Landmarks_list[frame][i][0],
                            'y':Landmarks_list[frame][i][1],
                            'z':Landmarks_list[frame][i][2],
                            }
                #if this frame is not first frame            
                if frame:  
                    with open(f'Sec{index}.json', 'a') as outfile:
                        outfile.write(',\n')
                        outfile.write(''.join(json.dumps(Points, separators=(',',':'))))
                #if this frame is first frame  
                else:
                    with open(f'Sec{index}.json', 'a') as outfile:
                        outfile.write(''.join(json.dumps(Points, separators=(',',':'))))      

        with open(f'Sec{index}.json', "a") as outfile:
            outfile.write(']') 
    
    with open(f'Sec{index}.json') as outfile: 
        if ValidateJsonFile(outfile):
            print(f'Sec{index}.json is valid')
        else:
            print(f'Sec{index}.json is invalid') 
#==================================================#        
def ValidateJsonFile(jsonFile):
    try:
        json.load(jsonFile)
    except ValueError as error:
        print(error)
        return False
    return True

# def Existed_JsonFiles():
#     path_to_json = '/home/beshbesh/Deep-Learning'
#     json_files = [pos_json for pos_json in os.listdir(
#         path_to_json) if pos_json.endswith('.json')]
#     Sorted_List = natsorted(json_files)
#     return (Sorted_List)
#==================================================#  

# json_files = Existed_JsonFiles()
# print(json_files)
# for jf in json_files:
#     with open(jf) as file:
#         if ValidateJsonFile(file):
#             print(f'{jf} is valid')
#         else:
#             print(f'{jf} is invalid')
