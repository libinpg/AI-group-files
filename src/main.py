import argparse
from .utils.file_parser import read_file_content
from .utils.util import write_ai_reply_to_file
from .classifiers.openai_classifier import classify_content as openai_classify
from .classifiers.ChatGLM2_6B_32K_classifier import classify_content as glm_classify
from .classifiers.baichuan2_13b_classifier import classify_content as baichuan2_classify
from .os_operations.organizer import move_file_to_category_folder
import os
from .prompts.stage1_prompt import CONCLUDE_DIRECTORY_PROMPT
from .model_apis.baichuan2_13b_api import testApi

def process_file(file_path, classifier_func, save_path):
    content = read_file_content(file_path)
    if content:
        classification = classifier_func(content)
        if classification:
            move_file_to_category_folder(file_path, classification, save_path)

def process_directory(directory, classifier_func, save_path):
    
    
    while True:
        fist_reply = testApi(CONCLUDE_DIRECTORY_PROMPT.format(os.listdir(directory)))
        print('CONCLUDE_DIRECTORY_PROMPT.format(os.listdir(directory))',CONCLUDE_DIRECTORY_PROMPT.format(os.listdir(directory)))
        print("fist_reply: ", fist_reply)
        write_ai_reply_to_file(fist_reply, 'src/data/directoryconclusion.txt')

        user_input = input("确定分类结果是否符合需求...,输入yes继续")
        if user_input == "yes":
            break
        
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            process_file(file_path, classifier_func, save_path)

def main(target, classifier, save_path):
    if classifier == 'openai':
        classifier_func = openai_classify
    elif classifier == 'glm':
        classifier_func = glm_classify
    elif classifier == 'baichuan2':
        classifier_func = baichuan2_classify
    
    else:
        print(f"未知的分类器: {classifier}")
        return
    if os.path.isdir(target):
        process_directory(target, classifier_func, save_path)
    elif os.path.isfile(target):
        process_file(target, classifier_func, save_path)
    else:
        print(f"指定的路径 {target} 既不是文件也不是目录。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="自动文件整理系统")
    parser.add_argument("target_path", type=str, help="要整理的文件或目录的路径")
    parser.add_argument("--classifier", type=str, choices=['openai', 'glm', 'baichuan2'], default='openai',
                        help="选择使用的分类器：'openai', 'glm', 'baichuan2'")
    parser.add_argument("--save_path", type=str, default="./sorted_files", 
                    help="指定分类结果的保存路径")
    args = parser.parse_args()
    main(args.target_path, args.classifier, args.save_path)

