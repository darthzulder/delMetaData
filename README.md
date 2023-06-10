# Batch Image Metadata Removal Tool. ONLY WORKS WITH PNG (For now)

The Batch Image Metadata Removal Tool is a Python script that allows you to remove metadata from multiple image files in a directory in a batch process. It utilizes the Python Imaging Library (PIL) for image processing and provides a progress bar to track the processing status. 

## Features

- Removes unwanted EXIF metadata from image files
- Supports batch processing of multiple image files in a directory
- Utilizes ThreadPoolExecutor for improved processing speed
- Includes a progress bar to track the processing status
- Provides detailed code comments for better understanding and customization

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)
- tqdm (for progress bar)
- concurrent.futures (for ThreadPoolExecutor)

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

```sh
pip install -r requirements.txt
```


## Usage

1. Place your image files (in PNG format) that you want to process in the directory ./img/.
2. Open the terminal and navigate to the project directory.
3. Execute the Execute.bat file if you are in windows:
3. Or Execute the following command (by default):

```sh
python main.py
```
3. Or Execute the following command if you want to chage the path:

```sh
python main.py --input_dir ./img/ --output_dir ./img_delMD/
```


Replace `./img/` with the path to the directory containing your input images and `./img_delMD/` with the path to the directory where you want to save the processed images.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


