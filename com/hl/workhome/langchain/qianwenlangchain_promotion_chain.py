from langchain_classic.chains.base import Chain
from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate
import configparser

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

template = PromptTemplate.from_template(template="我有一个邻居姓{lastname}，生了一个{gender}，帮忙起个名字");

inputText = template.format(lastname="黄", gender="男孩")

model = Tongyi(model="qwen-max", api_key=config.get("settings", "api_key"))
# res = model.invoke(input=inputText)

chain = template | model;
res = chain.invoke(input={"lastname":"张", "gender":"女儿"})
print(res)
