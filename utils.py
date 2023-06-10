import os
from PIL import Image
from tqdm import tqdm
import concurrent.futures

def clear_exif(img_path, output_path):
    # Function to remove unwanted EXIF metadata from an image
    with Image.open(img_path) as im:
        # Define the fields to keep in the image metadata
        fields_to_keep = ('transparency',)
        # Get the list of all EXIF fields in the image
        exif_fields = list(im.info.keys())
        # Iterate through the EXIF fields
        for k in exif_fields:
            # If the field is not in the fields_to_keep, delete it from the image metadata
            if k not in fields_to_keep:
                del im.info[k]
        try:
            # Save the image with the updated metadata
            im.save(output_path, format='PNG')
        except Exception as e:
            # If there's an error while saving the image, print an error message
            print(f"Error al guardar {output_path}")
            raise e

def process_image(args):
    # Function to process an individual image by removing its metadata
    file_path, new_img_dir, i = args
    # Generate the new file name for the processed image
    number_name = os.path.join(new_img_dir, "{:06d}".format(i))
    # Call the clear_exif function to remove metadata from the image
    clear_exif(file_path, f"{number_name}_del.png")

def walk_dir(img_dir, new_img_dir):
    # Function to walk through a directory and process all the image files
    # Get the list of image files in the directory
    file_list = [entry for entry in os.scandir(img_dir) if entry.is_file() and entry.name.endswith('.png')]
    # Get the total number of image files
    total_files = len(file_list)

    # Initialize a progress bar using tqdm
    with tqdm(total=total_files, desc="Processing") as pbar, concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        # Iterate through the image files
        for i, entry in enumerate(file_list):
            # Get the file path of the image
            file_path = entry.path
            # Prepare the arguments for the process_image function
            args = (file_path, new_img_dir, i)
            # Submit the process_image function to the ThreadPoolExecutor
            future = executor.submit(process_image, args)
            # Append the future object to the list of futures
            futures.append(future)

        # Wait for all the futures to complete
        for future in concurrent.futures.as_completed(futures):
            # Get the result of the future
            future.result()
            # Update the progress bar
            pbar.update(1)
