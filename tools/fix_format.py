import base64
import os
import re


def clean_code_files(directory):
    # 遍历目录下的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                print(f"Checking {file_path}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                # 如果文件以 ```markdown 开头且以 ``` 结尾，修改内容
                if lines[0].strip() == '```markdown' and lines[-1].strip() == '```':
                    print(f" YES GOT\n")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(lines[1:-1])

                # 检查并修改第二行的 title 格式
                if len(lines) > 1 and lines[1].startswith('title: '):
                    title_content = lines[1][7:].strip()
                    if not (title_content.startswith('"') and title_content.endswith('"')):
                        lines[1] = f'title: "{title_content}"\n'

                # 修改 description 标签
                for i, line in enumerate(lines):
                    if line.startswith('description: '):
                        description_content = line[13:].strip()
                        if '"' in description_content:
                            description_content = description_content.replace('"', '&quot;')
                            lines[i] = f'description: "{description_content}"\n'

                # 修改 markdown 格式图片链接
                for i, line in enumerate(lines):
                    lines[i] = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',
                                      r'![\1](/images/python-standard-libs.png)', line)

                # 将修改后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)

                    print(f'Processed file: {file_path}')
            except Exception as e:
                print(f'Error processing file {file_path}: {e}')


# 使用示例
directory_path = 'check/'  # 将此替换为你的文件夹路径
clean_code_files(directory_path)
