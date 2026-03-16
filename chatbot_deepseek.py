# AI导论作业2 - DeepSeek聊天机器人
import requests

# 配置DeepSeek API信息
API_KEY = "your_deepseek_api_key"  # 替换为你的API Key
API_URL = "https://api.deepseek.com/v1/chat/completions"

def chat_with_deepseek(user_message):
    """调用DeepSeek API获取回答"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"请求失败，错误码：{response.status_code}"

if __name__ == "__main__":
    print("DeepSeek 聊天机器人已启动（输入 'exit' 退出）")
    while True:
        user_input = input("你：")
        if user_input.lower() == "exit":
            print("再见！")
            break
        reply = chat_with_deepseek(user_input)
        print(f"AI：{reply}")
