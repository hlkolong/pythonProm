from langchain_community.llms.tongyi import Tongyi
import configparser

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

model = Tongyi(model="qwen-max", api_key=config.get("settings", "api_key"))
res = model.invoke(input="你是谁呀， 会做什么")
print(res)