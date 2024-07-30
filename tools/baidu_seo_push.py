import os

import requests


def batch_push_urls(site, token, file_path, batch_size=10):
    url = f"http://data.zz.baidu.com/urls?site={site}&token={token}"
    headers = {'Content-Type': 'text/plain'}

    # 从文件读取URLs
    with open(file_path, 'r') as file:
        urls = file.readlines()

    # 处理每批次的URLs
    start_index = 0
    while start_index < len(urls):
        # 取当前批次的URLs
        end_index = min(start_index + batch_size, len(urls))
        batch_urls = urls[start_index:end_index]
        data = ''.join(batch_urls)

        # 发送POST请求
        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()

        if response.status_code == 200:
            print(f"Batch successful: {response_data.get('success', 0)} URLs pushed.")
            print(f"Remaining quota: {response_data.get('remain', 0)}")

            # 更新开始索引到下一批次
            start_index += batch_size

            # 成功推送后，从列表中移除已推送的URLs
            urls = urls[end_index:]

            # 检查是否还有剩余的配额，如果没有则提前退出
            if response_data.get('remain', 0) <= 0:
                print("No remaining quota. Stopping.")
                break
        else:
            print(f"Error pushing batch: {response_data.get('message', 'No error message')}")
            break

    # 推送完成后，更新文件内容
    with open(file_path, 'w') as file:
        file.writelines(urls)


# 使用函数
batch_push_urls(os.getenv('BAIDU_SEO_SITE'), os.getenv('BAIDU_SEO_KEY'), 'public/baidu_urls.txt')
