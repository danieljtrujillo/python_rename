import os

def rename_images(folder_path):
    files = os.listdir(folder_path)
    img_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    num_images = len(img_files)
    step = 499 / num_images

    for i, file in enumerate(sorted(img_files), start=1):
        new_name = str(round(i * step)).zfill(5) + os.path.splitext(file)[-1]
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

# specify the path to your folder
folder_path = "/path/to/folder"
rename_images(folder_path)
