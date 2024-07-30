import os
import pkgutil
import json
import random
import re
import subprocess

"""
AI:: 撰写文档
"""

def generate_title(module_name, lang):
    """

    :param module_name: The name of the module for which a title is being generated.
    :return: A randomly generated title for the given module.

    """
    zh = [
        "Python {module_name} 模块：入门指南",
        "Python {module_name} 模块：高级技巧",
        "Python {module_name} 模块：完整教程",
        "Python {module_name} 模块：使用实例",
        "Python {module_name} 模块：最佳实践",
        "Python {module_name} 模块：常见错误及解决方案",
        "Python {module_name} 模块：性能优化技巧",
        "Python {module_name} 模块：深度解析",
        "Python {module_name} 模块：从入门到精通",
        "Python {module_name} 模块：实用工具集",
        "Python {module_name} 模块：API详解",
        "Python {module_name} 模块：初学者必读",
        "Python {module_name} 模块：常见问题解答",
        "Python {module_name} 模块：开发者指南",
        "Python {module_name} 模块：基础知识",
        "Python {module_name} 模块：进阶使用",
        "Python {module_name} 模块：最佳资源",
        "Python {module_name} 模块：功能详解",
        "Python {module_name} 模块：高效使用技巧",
        "Python {module_name} 模块：十大实用功能",
        "Python {module_name} 模块：综合评测",
        "Python {module_name} 模块：快速入门",
        "Python {module_name} 模块：实战案例",
        "Python {module_name} 模块：你需要知道的一切",
        "Python {module_name} 模块：深入探索",
        "Python {module_name} 模块：与其他模块的比较",
        "Python {module_name} 模块：常见用法",
        "Python {module_name} 模块：常见错误解析",
        "Python {module_name} 模块：最佳配置",
        "Python {module_name} 模块：开发技巧",
        "Python {module_name} 模块：快速参考指南",
        "Python {module_name} 模块：高级特性",
        "Python {module_name} 模块：学习路径",
        "Python {module_name} 模块：开发心得",
        "Python {module_name} 模块：常见问题及解答",
        "Python {module_name} 模块：功能演示",
        "Python {module_name} 模块：进阶教程",
        "Python {module_name} 模块：最佳实践案例",
        "Python {module_name} 模块：详细指南",
        "Python {module_name} 模块：新手指南",
        "Python {module_name} 模块：使用技巧",
        "Python {module_name} 模块：全面分析",
        "Python {module_name} 模块：如何使用",
        "Python {module_name} 模块：详细介绍",
        "Python {module_name} 模块：必备技巧",
        "Python {module_name} 模块：全面入门",
        "Python {module_name} 模块：使用教程",
        "Python {module_name} 模块：常见问题",
        "Python {module_name} 模块：权威指南"
    ]

    en = [
        "Python {module_name} Module: Complete Guide to Installation and Advanced Usage",
        "Python {module_name} Module: Step-by-Step Installation and Use Case Examples",
        "Python {module_name} Module: Mastering Installation and Advanced Tutorials",
        "Python {module_name} Module: Installation Guide and Advanced Function Examples",
        "Python {module_name} Module: How to Install and Use with Advanced Examples",
        "Python {module_name} Module: Installation and Exploring Advanced Features",
        "Python {module_name} Module: Beginner to Advanced Guide with Practical Examples",
        "Python {module_name} Module: From Installation to Advanced Usage",
        "Python {module_name} Module: Comprehensive Installation and Use Case Guide",
        "Python {module_name} Module: Detailed Tutorial on Installation and Advanced Use",
        "Python {module_name} Module: Advanced Usage Examples and Installation Steps",
        "Python {module_name} Module: Installation Steps and Advanced Usage Guide",
        "Python {module_name} Module: Step-by-Step Guide to Installation and Advanced Use",
        "Python {module_name} Module: Mastering Installation and Advanced Use Cases",
        "Python {module_name} Module: Advanced Features and Installation Tutorial",
        "Python {module_name} Module: Installation Guide with Advanced Function Examples",
        "Python {module_name} Module: Advanced Tutorials and Installation Guide",
        "Python {module_name} Module: Installation and Practical Advanced Use Cases",
        "Python {module_name} Module: How to Install and Explore Advanced Features",
        "Python {module_name} Module: Advanced Usage and Installation Guide",
        "Python {module_name} Module: Detailed Guide on Installation and Advanced Usage",
        "Python {module_name} Module: Comprehensive Guide from Installation to Advanced Use",
        "Python {module_name} Module: Step-by-Step Installation and Advanced Functionality",
        "Python {module_name} Module: Advanced Use Case Examples and Installation Guide",
        "Python {module_name} Module: Installation and Advanced Use Case Tutorials",
        "Python {module_name} Module: Installation Guide with Advanced Tutorials",
        "Python {module_name} Module: How to Install and Use Advanced Features",
        "Python {module_name} Module: Advanced Examples and Installation Steps",
        "Python {module_name} Module: Installation Steps and Advanced Use Cases",
        "Python {module_name} Module: Advanced Features and Installation Guide",
        "Python {module_name} Module: Detailed Installation and Advanced Functionality",
        "Python {module_name} Module: Comprehensive Guide to Advanced Usage and Installation",
        "Python {module_name} Module: Step-by-Step Guide from Installation to Advanced Use",
        "Python {module_name} Module: Mastering Advanced Usage and Installation",
        "Python {module_name} Module: Advanced Function Examples and Installation Guide",
        "Python {module_name} Module: Installation and Exploring Advanced Functionality",
        "Python {module_name} Module: How to Master Installation and Advanced Use",
        "Python {module_name} Module: Installation and Advanced Examples Guide",
        "Python {module_name} Module: Advanced Usage and Installation Examples",
        "Python {module_name} Module: Detailed Guide to Advanced Features and Installation",
        "Python {module_name} Module: Comprehensive Installation and Advanced Use Guide",
        "Python {module_name} Module: Step-by-Step Installation and Advanced Examples",
        "Python {module_name} Module: Mastering Advanced Use and Installation",
        "Python {module_name} Module: Advanced Functionality and Installation Tutorial",
        "Python {module_name} Module: Installation Guide and Advanced Usage Tutorials",
        "Python {module_name} Module: Advanced Usage Examples and Installation Tutorial",
        "Python {module_name} Module: Installation Steps and Advanced Function Examples",
        "Python {module_name} Module: Advanced Features with Installation Guide",
        "Python {module_name} Module: Comprehensive Advanced Usage and Installation Guide",
        "Python {module_name} Module: How to Install and Use Advanced Functionality"
    ]

    if lang == "en":
        titles = en
    elif lang == "zh":
        titles = zh
    else:
        titles = lang

    chosen_title = random.choice(titles)
    return chosen_title.format(module_name=module_name)


def generate_valid_directory_name(title):
    """
    A method to generate a valid directory name based on the provided title.

    :param title: The title to generate the directory name from.
    :type title: str
    :return: The generated valid directory name.
    :rtype: str
    """
    # 定义允许的字符（字母、数字、下划线、连字符、空格），包括非英文的字母
    allowed_chars = re.compile(r'[^\w\s-]', re.UNICODE)

    # 替换不允许的字符为空字符串
    clean_title = allowed_chars.sub('', title)

    # 将空格替换为连字符
    valid_directory_name = clean_title.replace(' ', '-')

    # 返回处理后的合法文件夹名称
    return valid_directory_name

def save_standard_library_modules_to_file():
    """
    Save Standard Library Modules to File

    This method saves the names of standard library modules to a file in JSON format.

    :return: None

    """
    # 创建一个空列表来存储模块名称
    modules_list = []
    num = 0
    # 遍历所有模块
    with open("tools/datasets/program_az_guids_en.json", "r", encoding='utf-8') as content:
        dataset = json.load(content)

        for category in dataset:

            post_category = category

            for title in dataset[category]:
                post_title = title
                file_name = generate_valid_directory_name(post_title)
                num += 1
                modules_list.append({
                    'index': num,
                    'post_category': post_category,
                    'filename': f"{file_name}.md",
                    'post_title': post_title,
                    'post_file': f"source/_posts/{file_name}.md",
                    'created': False
                })  # 将模块名称添加到列表中

    # 将模块列表保存到文件
    with open('tools/titles/articles_dataset_01.json', 'w', encoding='utf-8') as file:
        json.dump(modules_list, file, indent=4)  # 以JSON格式写入文件

# 调用函数，保存模块名称到文件
save_standard_library_modules_to_file()