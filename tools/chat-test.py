import os

from openai import OpenAI
from dotenv import load_dotenv

# 调用 load_dotenv 方法，这会加载位于同一目录下的 .env 文件中的环境变量
load_dotenv()

# 设置 API 密钥
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def chat_with_gpt4(prompt):
    response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "you are a helpful assistant"},
                {"role": "user", "content": "how it is today?"},
            ],
            stream=True  # 启用流式输出
        )

    article = ""
    print("生成的文章内容:\n")
    for chunk in response:
        if chunk.choices:

            chunk_message = chunk.choices[0].delta.content
            if chunk_message:
                print(chunk_message, end='', flush=True)  # 流式输出
                article += chunk_message

    print("\n")  # 确保输出完整内容后换行
    return article

print("开始与 GPT-4 对话 (输入 '退出' 来结束对话)")
while True:
    user_input = input("你: ")
    if user_input.lower() == "退出":
        break
    response = chat_with_gpt4(user_input)
    print("GPT-4:", response)
