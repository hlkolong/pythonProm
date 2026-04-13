from langchain_community.llms.tongyi import Tongyi
import configparser

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

model = Tongyi(model="qwen-max", api_key=config.get("settings", "api_key"))
chunks = model.stream(input="你是谁呀， 会做什么")
for chunk in chunks:
    print(chunk, end="", flush=True);