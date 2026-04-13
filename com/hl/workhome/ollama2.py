import configparser

from openai import OpenAI
from openai.types.chat import ChatCompletion

config = configparser.ConfigParser()
config.read("labiconfig.ini", "utf-8");
client:OpenAI = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
    # api_key=config.get("settings", "api_key"),
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
);

response:ChatCompletion = client.chat.completions.create(
    model="qwen3:4b",
    # model="qwen3.6-plus",
    messages=[
        {
            "role": "system",
            "content": "你是一个冷酷的杀手, 现在要去执行一项刺杀任务， 目标是王者峡谷的现眼包马可波罗"
        }, {
            "role": "user",
            "content": "你需要做哪些准备工作"
        }]
);

print(response.choices[0].message.content);


