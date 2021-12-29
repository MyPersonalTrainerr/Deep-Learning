# import requests
# # import json

# URL = "https://awatef.pythonanywhere.com/fileUploadApi"

# # data to be sent to api
# # data = {'file_uploaded': "Points.json"}
# # files = {'file_uploaded':open('Points.json', 'rb')}

# # sending post request and saving response as response object
# # r = requests.post(url = URL, data=open('Points.json', 'rb'))
# # r = requests.post(url = URL, files=files)
# r = requests.get(url = URL)

# print(r.json())


# import json
# import gzip

# data ={'feed': {'title': 'W3Schools Home Page', 'title_detail': {'type': 'text/plain', 'language': None, 'base': '', 'value': 'W3Schools Home Page'}, 'links': [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://www.w3schools.com'}], 'link': 'https://www.w3schools.com', 'subtitle': 'Free web building tutorials', 'subtitle_detail': {'type': 'text/html', 'language': None, 'base': '', 'value': 'Free web building tutorials'}}, 'entries': [], 'bozo': 0, 'encoding': 'utf-8', 'version': 'rss20', 'namespaces': {}}
# def compress_data(data):
#     # Convert to JSON
#     json_data = json.dumps(data, indent=2)
#     # Convert to bytes
#     encoded = json_data.encode('utf-8')
#     # Compress
#     compressed = gzip.compress(encoded)

# compress_data(data)
# with open("data.json", "a") as outfile:
#     json.dump(data, outfile, indent=2, separators=(',',': '))
#     # outfile.write(',')
#     outfile.write('\n')

# import json
# import os
# from zipfile import ZipFile

# data = [
#     {"key01":"value","key02":"value"},
#     {"key11":"value","key12":"value"},
#     {"key21":"value","key22":"value"}
# ]

# with open('file.json', 'w') as fp:
#     fp.write(
#         '[' +
#         ',\n'.join(json.dumps(i) for i in data) +
#         ']\n')

# def create_zip(path,zipf):
#     for root, dirs, files in os.walk(path):
#         print(root)
#         print(dirs)
#         print(files)
#         for file in files:
#             if file.endswith(".json"):
#                 # chdir(root)
#                 # zipf.write(file)
#                 print(file)
#                 print(os.path.join(root, file))
#                 # filename = os.path.join(root, file)
#                 # print(filename)
#                 zipf.write(os.path.join(root, file))
#                 # os.remove(file)

import os
import zipfile

def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])
                
path ="/home/beshbesh/GP/connection"
zip_directory(path, "p.zip")
# create_zip(path,path)