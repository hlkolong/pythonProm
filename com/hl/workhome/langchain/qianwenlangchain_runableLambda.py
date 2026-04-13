from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
import configparser

from langchain_core.runnables import RunnableLambda

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

firstProm = PromptTemplate.from_template(
    "我的邻居姓：{lastname}，生了一个{gender}，请帮忙起一个名字，不要返回多余的文字"
    "key是name，value就是起的名字"
)

secondProm = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义"
)

chatModel = ChatTongyi(model="qwen-max", api_key=config.get("settings", "api_key"));
# jsonOutputParser = JsonOutputParser();

myParser = RunnableLambda(lambda aiMsg:{"name":aiMsg.content})

strOutputParser = StrOutputParser();

chain = firstProm|chatModel|myParser|secondProm|chatModel|strOutputParser

chunks = chain.stream({"lastname":"张","gender":"女儿"})
for chunk in chunks:
    print(chunk, end="", flush=True);


