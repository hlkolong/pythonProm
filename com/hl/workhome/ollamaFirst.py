import configparser

from openai import OpenAI

config = configparser.ConfigParser()
config.read("labiconfig.ini", "utf-8");
client:OpenAI = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
    # api_key=config.get("settings", "api_key"),
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
);

completion = client.chat.completions.create(
    model="qwen3:4b",
    # model="qwen3.6-plus",
    messages=[
        {
            "role": "system",
            "content": "你是一个冷酷的杀手, 现在要去执行一项刺杀任务， 目标是王者峡谷的现眼包马可波罗"
        }, {
            "role": "user",
            "content": "你需要做哪些准备工作"
        }],
    stream=True
);

is_answering = False;  # 是否进入回复阶段
print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)


