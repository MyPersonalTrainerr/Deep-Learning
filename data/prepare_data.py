import shutil
import splitfolders
import os


def collect_data_files_together():

    source_dir = 'data/sample_video'
    target_dir = 'data/all_data/new'
    
    folders_list = os.listdir(source_dir)

    n_files_before = os.listdir(target_dir)
    print(len(n_files_before)) 
    
    for folder_list in folders_list:

        path_to_folder = os.path.join(source_dir, folder_list)
        folders_in_folder = os.listdir(path_to_folder)

        for folder_in_folder in folders_in_folder:

            path_3djoints = os.path.join(path_to_folder, folder_in_folder)
            file_names = os.listdir(path_3djoints)

            for file_name in file_names:
                path_to_json = os.path.join(path_3djoints, file_name)
                shutil.copy2(path_to_json, target_dir)
                # shutil.move(path_to_json, target_dir)
    
    n_files_after = os.listdir(target_dir)
    print(len(n_files_after)) 

# call this fun just for the first time.
# collect_data_files_together()

# split data into train/val/test
splitfolders.ratio(input = 'data/all_data', output = "data/output", seed=1337, ratio=(.8, 0.1, 0.1)) 
