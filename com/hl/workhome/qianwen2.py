from openai import OpenAI
import os
import configparser

print(os.getcwd())
config = configparser.ConfigParser()
config.read("labiconfig.ini", "utf-8");
# config.read('com/hl/workhome/labiconfig.ini');

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=config.get("settings", "api_key"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

messages=[
        {
            "role": "system",
            "content": "你是一个冷酷的杀手, 现在要去执行一项刺杀任务， 目标是王者峡谷的现眼包马可波罗"
        }, {
            "role": "user",
            "content": "你需要做哪些准备工作"
        }]
completion = client.chat.completions.create(
    model="qwen3.6-plus",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": True}
)
print(completion.choices[0].message.content);