import json

     
def Creating_Json(Landmarks_list, index):
    print("in utils file")
    Points = {}
    if Landmarks_list:
        with open(f'Sec{index}.json', 'a') as outfile:
            outfile.write('[')

        for frame in range(len(Landmarks_list)):
            # Iterate 33 times to display all landmarks.    
            for i in range(33):
                # Display the found landmarks after converting them into their original scale.
                Points[i] = {
                        'x':Landmarks_list[frame][i][0],
                        'y':Landmarks_list[frame][i][1],
                        'z':Landmarks_list[frame][i][2],
                        }
            if frame:
                with open(f'Sec{index}.json', 'a') as outfile:
                    outfile.write(',\n')
                    outfile.write(''.join(json.dumps(Points, separators=(',',':'))))
            else:
                 with open(f'Sec{index}.json', 'a') as outfile:
                    outfile.write(''.join(json.dumps(Points, separators=(',',':'))))

        with open(f'Sec{index}.json', "a") as outfile:
            outfile.write(']') 
#==================================================#   