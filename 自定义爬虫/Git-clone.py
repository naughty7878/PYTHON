import subprocess
import os
import json
import time
import random

# 从文件中读取 projects 数组
def load_projects_from_file(file_path):
    """
    从 JSON 文件中加载 projects 数组
    :param file_path: JSON 文件路径
    :return: projects 数组
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件 {file_path} 不存在")

    with open(file_path, "r", encoding="utf-8") as f:
        projects = json.load(f)
        return projects

# 创建目录结构
def create_namespace_directory(namespace):
    """
    根据 namespace 创建目录结构
    :param namespace: 命名空间路径（如 "zeus/global/moon/"）
    :return: 创建的目录路径
    """
    # 去除末尾的斜杠（如果存在）
    namespace = namespace.rstrip("/")
    # 创建目录
    os.makedirs(namespace, exist_ok=True)
    return namespace

# 克隆项目
def clone_project(project, initial_dir):
    """
    克隆单个项目
    :param project: 项目信息字典
    :param initial_dir: 脚本运行的初始目录
    """
    project_name = project["item_project_name"]
    git_url = project["item_http"]  # 使用 HTTP URL
    namespace = project["item_namespace_name"]

    # 创建命名空间目录
    base_dir = create_namespace_directory(namespace)

    # 切换到命名空间目录
    os.chdir(base_dir)

    # 执行 git clone 命令
    try:
        subprocess.run(["git", "clone", git_url], check=True)
        print(f"Successfully cloned {project_name} into {base_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {project_name}: {e}")
        print(f"Git URL: {git_url}")
        print(f"Please check if the repository exists and you have access.")
    finally:
        # 切换回初始目录
        os.chdir(initial_dir)

# 主函数
def main():
    # 保存脚本运行的初始目录
    initial_dir = os.getcwd()

    # 从文件中加载 projects 数组
    file_path = "projects.json"  # JSON 文件路径
    try:
        projects = load_projects_from_file(file_path)
    except Exception as e:
        print(f"加载文件失败: {e}")
        return

    # 遍历数组中的每个项目
    for project in projects:
        clone_project(project, initial_dir)

        # 随机休眠 10 秒到 120 秒
        sleep_time = random.randint(10, 120)
        print(f"休眠 {sleep_time} 秒...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()