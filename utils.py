import os
from PIL import Image

def clear_exif(img_dir, number_name):
    with Image.open(f'{img_dir}', mode='r', formats=['PNG']) as im:
        fields_to_keep = ('transparency', )
        exif_fields = list(im.info.keys())
        for k in exif_fields:
            if k not in fields_to_keep:
                del im.info[k]
        try:
            im.save(f'{number_name}_del.png', format='PNG')
        except Exception as e:
            print(f"Error to save {number_name}_del.png")
            raise e
            
def walk_dir(img_dir, new_img_dir):
    i = 0
    for files_dir in os.listdir(img_dir):
        tempTuple = os.path.splitext(files_dir)
        if tempTuple[1].endswith(".png"):
            file_path = os.path.join(img_dir, files_dir)
            number_name = os.path.join(new_img_dir, "{:06d}".format(i))
            clear_exif(file_path, number_name)
            i+=1
