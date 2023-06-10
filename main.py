import argparse
import utils

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch Image Metadata Removal Tool")
    parser.add_argument("--input_dir", type=str, default="./img/", help="Input directory containing image files")
    parser.add_argument("--output_dir", type=str, default="./img_delMD/", help="Output directory to save processed images")
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    utils.walk_dir(input_dir, output_dir)