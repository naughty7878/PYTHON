import os

def remove_dot_underscore_files(folder_path):
    """
    递归删除文件夹中以 ._ 开头的文件
    :param folder_path: 要处理的文件夹路径
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith('._'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"已删除: {file_path}")
                except Exception as e:
                    print(f"删除失败 {file_path}: {e}")

def main():
    target_folder = "F:\\相册"
    print(target_folder)
    if os.path.isdir(target_folder):
        remove_dot_underscore_files(target_folder)
        print("清理完成！")
    else:
        print("错误: 指定的路径不是文件夹或不存在")

main()




