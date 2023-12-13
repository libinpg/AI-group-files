import argparse
from file_parser import read_file_content
from openai_classifier import classify_content
from organizer import move_file_to_category_folder
import os
def process_file(file_path):
    content = read_file_content(file_path)
    if content:
        classification = classify_content(content)
        if classification:
            move_file_to_category_folder(file_path, classification)

def process_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            process_file(file_path)

def main(target):
    if os.path.isdir(target):
        process_directory(target)
    elif os.path.isfile(target):
        process_file(target)
    else:
        print(f"指定的路径 {target} 既不是文件也不是目录。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="自动文件整理系统")
    parser.add_argument("target_path", type=str, help="要整理的文件或目录的路径")
    args = parser.parse_args()
    main(args.target_path)