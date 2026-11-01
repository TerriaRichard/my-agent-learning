from openai import OpenAI

# 1. 初始化客户端（相当于插上电话线）
# 这里以 DeepSeek 为例，如果是智谱等其他平台，把 base_url 换掉即可
client = OpenAI(
    api_key="sk-23747329318d4fe7a0f79902753df9d0", # ⚠️ 替换成你刚才申请的那串字符
    base_url="https://api.deepseek.com"
)

# # 2. 发起请求（拨打电话）
# print("正在呼叫大模型，请稍候...")
# response = client.chat.completions.create(
#     model="deepseek-chat", # 告诉它你想用哪个版本的模型
#     messages=[
#         {"role": "user", "content": "你好，请用一句简短的话介绍一下你自己，并告诉我 1+1 等于几。"}
#     ]
# )
#
# # 3. 打印结果（接听回复）
# print("\n--- 大模型回复 ---")
# print(response.choices[0].message.content)


# 用一个列表来充当机器人的“大脑记忆”
messages = [
    {"role": "system", "content": "你是一个乐于助人的 AI 助手。"}
]

print("输入 '退出' 即可结束聊天。")

while True:
    # 1. 获取用户输入
    user_input = input("\n你: ")
    if user_input == "退出":
        break

    # 2. 把用户的话加进记忆里
    messages.append({"role": "user", "content": user_input})

    # 3. 呼叫大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    # 4. 提取大模型的回答，并加进记忆里
    ai_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_reply})

    # 5. 打印回答
    print(f"AI: {ai_reply}")

# 打印 usage 对象，看看里面到底装了些什么
print(f"\n[系统数据] {response.usage}")

    # 提取具体的数字，更直观
prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

print(f"[计费统计] 你的输入消耗了: {prompt_tokens} 个 Token")
print(f"[计费统计] 模型的回答消耗了: {completion_tokens} 个 Token")
print(f"[计费统计] 本次对话总共消耗: {total_tokens} 个 Token")
print("-" * 40)