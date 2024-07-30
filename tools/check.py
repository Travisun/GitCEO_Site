import os

def check_hexo_front_matter(directory):
    problematic_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    di = 0
                    for line in lines:
                        if line == "---\n":
                            di += 1
                    if di < 2:
                        problematic_files.append(file_path)

    return problematic_files


def main():
    directory = "source/_posts"  # 请替换为你的 Hexo 文件目录
    problematic_files = check_hexo_front_matter(directory)

    if problematic_files:
        print("以下文件的文件头缺少 --- 作为结尾：")
        for file in problematic_files:
            print(file)
    else:
        print("所有文件的文件头都正确地包含 --- 作为结尾。")


if __name__ == "__main__":
    main()
