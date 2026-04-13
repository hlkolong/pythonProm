import configparser

from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts import PromptTemplate

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

history = [
    ("user", "写一首绝句"),
    ("ai", "秦时明月汉时关，万里长征人未还。但使龙城飞将在，不教胡马度阴山。"),
    # {"system", "你是一名诗人，边塞诗人"},
]

template = ChatPromptTemplate.from_messages(
    [("system", "你是一名诗人，边塞诗人"),
     MessagesPlaceholder("history"),
     ("user", "再写一首绝句, 不要明着提到大漠，要创作，不要直接照搬古人的诗句")]
);

model = Tongyi(model="qwen-max", api_key=config.get("settings", "api_key"))

# text = template.invoke(input={"history": history}).to_string();
# res = model.invoke(text);
chain = template|model;
res = chain.invoke({"history":history})

print(res)
