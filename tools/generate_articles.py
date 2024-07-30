import os
import json
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
    with open('standard_library_modules.json', 'r', encoding='utf-8') as file:
        modules_list = json.load(file)  # 使用json.load()读取文件内容

    return modules_list  # 返回读取的模块名称列表

def read_system_prompt_from_file():
    """从文本文件中读取系统提示词"""
    with open('tools/system_prompt.txt', 'r', encoding='utf-8') as file:
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

def save_article_to_file(article, folder_path, file_name):
    """
    将生成的文章保存到指定文件夹
    :param article: 生成的文章内容
    :param folder_path: 文件夹路径
    :param file_name: 文件名称
    """
    # 确保文件夹存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 保存文件（覆盖）
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(article)
    print(f"文章已保存至: {file_path}")

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="生成并保存文章")
    parser.add_argument('--auto-save', action='store_true', help="自动保存生成的文章")
    args = parser.parse_args()

    # 从文件中读取系统提示词
    system_prompt = read_system_prompt_from_file()

    # 调用函数，读取模块名称
    modules = read_standard_library_modules_from_file()

    user_prompts = modules  # 用户提示词列表

    folder_path = 'generated_articles'  # 指定保存文章的文件夹

    for user_prompt in user_prompts:
        while True:
            file_name = f"{user_prompt}.md"  # 指定文件名称
            # 生成文章
            generated_article = generate_article(system_prompt, f"撰写文章：{user_prompt}")
            if generated_article:
                if args.auto_save:
                    save_article_to_file(generated_article, folder_path, file_name)  # 自动保存到文件
                    break
                else:
                    # 询问用户是否确认保存
                    confirmation = input(
                        "是否确认保存该内容 (save)，重新生成 (regenerate)，或者跳过 (skip)? (s/r/k): ").strip().lower()
                    if confirmation == 's':
                        save_article_to_file(generated_article, folder_path, file_name)  # 保存到文件
                        break
                    elif confirmation == 'k':
                        break

if __name__ == '__main__':
    main()