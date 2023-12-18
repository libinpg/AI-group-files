import os
import shutil

def create_directory_if_not_exists(directory_path):
    """
    如果指定的目录不存在，则创建它。
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def move_file_to_category_folder(file_path, category, save_path):
    """
    将文件移动到其分类标签对应的文件夹。
    """
    if not category or not file_path:
        print("分类标签或文件路径为空，无法整理文件。")
        return

    # directory_path = os.path.join("sorted_files", category)
    directory_path = os.path.join(save_path, category)
    create_directory_if_not_exists(directory_path)

    # 构建目标文件路径
    file_name = os.path.basename(file_path)
    target_path = os.path.join(directory_path, file_name)

    try:
        # shutil.move(file_path, target_path)
        shutil.copy(file_path, target_path)
        # print(f"文件 '{file_name}' 已移动到 '{directory_path}'")
        print(f"文件 '{file_name}' 已复制到 '{directory_path}'")
    except Exception as e:
        # print(f"移动文件时出错: {e}")
        print(f"复制文件时出错: {e}")