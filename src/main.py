import argparse
from file_parser import read_file_content
from openai_classifier import classify_content as openai_classify
from ChatGLM2_6B_32K_classifier import classify_content as glm_classify
from organizer import move_file_to_category_folder
import os

def process_file(file_path, classifier_func):
    content = read_file_content(file_path)
    if content:
        classification = classifier_func(content)
        if classification:
            move_file_to_category_folder(file_path, classification)

def process_directory(directory, classifier_func):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            process_file(file_path, classifier_func)

def main(target, classifier):
    classifier_func = openai_classify if classifier == 'openai' else glm_classify
    if os.path.isdir(target):
        process_directory(target, classifier_func)
    elif os.path.isfile(target):
        process_file(target, classifier_func)
    else:
        print(f"指定的路径 {target} 既不是文件也不是目录。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="自动文件整理系统")
    parser.add_argument("target_path", type=str, help="要整理的文件或目录的路径")
    parser.add_argument("--classifier", type=str, choices=['openai', 'glm'], default='openai', 
                        help="选择使用的分类器：'openai' 或 'glm'")
    
    args = parser.parse_args()
    main(args.target_path, args.classifier)
