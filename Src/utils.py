import json

     
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
#==================================================#   