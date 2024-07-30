import os
import json
import subprocess
from openai import OpenAI
import argparse
from dotenv import load_dotenv

# 调用 load_dotenv 方法，这会加载位于同一目录下的 .env 文件中的环境变量
load_dotenv()

# 配置OpenAI API密钥
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),  # this is also the default, it can be omitted
)

def read_standard_library_modules_from_file():
    """从JSON文件中读取Python标准库模块名称列表"""
    with open('python_top_modules_en.json', 'r', encoding='utf-8') as file:
        modules_list = json.load(file)  # 使用json.load()读取文件内容

    return modules_list  # 返回读取的模块名称列表

def read_system_prompt_from_file(prompt_file_path):
    """从文本文件中读取系统提示词"""
    with open(prompt_file_path, 'r', encoding='utf-8') as file:
        system_prompt = file.read()  # 读取整个文件内容

    return system_prompt  # 返回系统提示词

def generate_article(system_prompt, user_prompt):
    """
    根据系统提示词和用户提示词生成文章内容
    :param system_prompt: 系统提示词，用于设定生成内容的背景和风格
    :param user_prompt: 用户提示词，用于指定文章主题
    :return: 生成的文章内容
    """
    try:
        # 调用OpenAI API生成文本
        models = ["gpt-4o-mini-2024-07-18", "gpt-4o-2024-05-13"]

        response = client.chat.completions.create(
            model=models[0],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=True  # 启用流式输出
        )

        article = ""
        print(f"{user_prompt}:\n")
        for chunk in response:
            if chunk.choices:
                chunk_message = chunk.choices[0].delta.content
                if chunk_message:
                    print(chunk_message, end='', flush=True)  # 流式输出
                    article += chunk_message

        print("\n")  # 确保输出完整内容后换行
        return article.strip()
    except Exception as e:
        print(f"生成文章时出错: {e}")
        return None

def save_article_to_file(article, full_path):
    """
    将生成的文章保存到指定文件夹
    :param article: 生成的文章内容
    :param full_path: 完整文件路径（包括目录和文件名）
    """
    try:
        # 提取目录路径
        folder_path = os.path.dirname(full_path)

        # 确保文件夹存在
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # 保存文件（覆盖）
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(article)
        print(f"文章已保存至: {full_path}")

    except OSError as e:
        print(f"创建文件夹或保存文件时出错: {e}")


# 从JSON文件中加载数据
def load_posts_datasets(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# 将数据保存回JSON文件
def save_posts_datasets(file_path, posts):
    with open(file_path, 'w') as f:
        json.dump(posts, f, indent=4)


# 处理每个post
def process_posts(system_prompt, data_sets, auto_save=False, language="zh"):
    posts = load_posts_datasets(dataset_file)
    for post in posts:
        if not post['created']:
            folder_path = post['post_file']
            post_file_name = post['filename']
            post_name = post['post_title']
            catrgory = post['post_category']
            # 生成文章
            generated_article = generate_article(f"设定文章中的默认分类为{catrgory} ， {system_prompt}", f"\n\n撰写文章：{post_name}")
            # 为本地Hexo创建新文章
            command = f"hexo new post --path \"{post_file_name}\" \"{post_name}\" "
            subprocess.run(command, shell=True)
            # 生产内容
            if generated_article:
                if auto_save:
                    save_article_to_file(generated_article, folder_path)  # 自动保存到文件
                    post['created'] = True
                    save_posts_datasets(data_sets, posts)
                else:
                    # 询问用户是否确认保存
                    confirmation = input("\n\n是否确认保存该内容 (save)，重新生成 (regenerate)，或者跳过 (skip)? (s/r/k): ").strip().lower()
                    if confirmation == 's':
                        save_article_to_file(generated_article, folder_path)  # 保存到文件
                        post['created'] = True
                        save_posts_datasets(data_sets, posts)
                    elif confirmation == 'k':
                        break


if __name__ == '__main__':
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="Process some command line arguments.")

    # 添加 --prompt-file 参数
    parser.add_argument('--prompt-file', type=str, required=True, help='The path to the prompt file.')

    # 解析命令行参数
    parser.add_argument('--auto-save', action='store_true', help="自动保存生成的文章")

    parser.add_argument('--dataset-file', type=str, required=True, help='保存文章的JSON文件路径.')

    # 解析命令行参数
    args = parser.parse_args()

    # 获取参数值
    prompt_file = args.prompt_file
    auto_save = args.auto_save
    dataset_file = args.dataset_file

    system_prompt = read_system_prompt_from_file(prompt_file)  # 替换为你的系统提示

    process_posts(system_prompt, dataset_file, auto_save)
    # main()