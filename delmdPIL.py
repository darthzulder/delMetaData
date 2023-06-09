# Uses the Python Imaging Library
# `pip install Pillow` works too
from PIL import Image

def clear_exif(img_dir):
    with Image.open(f'{img_dir}', mode='r', formats=['PNG']) as im:
        fields_to_keep = ('transparency', )
        exif_fields = list(im.info.keys())
        for k in exif_fields:
            if k not in fields_to_keep:
                del im.info[k]

        im.save(f'{img_dir}_del', format='PNG')