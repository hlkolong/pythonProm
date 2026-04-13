from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
import configparser

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

firstProm = PromptTemplate.from_template(
    "我的邻居姓：{lastname}，生了一个{gender}，请帮忙起两个名字，并封装成json返回给我，"
    "key是name，value就是起的名字"
)

secondProm = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义"
)

chatModel = ChatTongyi(model="qwen-max", api_key=config.get("settings", "api_key"));
jsonOutputParser = JsonOutputParser();
strOutputParser = StrOutputParser();

chain = firstProm|chatModel|jsonOutputParser|secondProm|chatModel|strOutputParser

res = chain.invoke({"lastname":"张","gender":"女儿"})
print(res, end="", flush=True);


