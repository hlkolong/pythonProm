from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
import configparser

from langchain_core.runnables import RunnableLambda, RunnableWithMessageHistory

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

promTemplate = PromptTemplate.from_template(
    "你是一个话不多的问答器，你需要根据历史内容给出回应。对话历史：{history}，当用户数据{input}，给出回应"
)
chatModel = ChatTongyi(model="qwen-max", api_key=config.get("settings", "api_key"));


# jsonOutputParser = JsonOutputParser();

def printPromotion(prom):
    print("=" * 20, prom, "=" * 20)
    return prom


chat_history_store = {};


def getSessionHistory(sessionId):
    if sessionId not in chat_history_store:
        chat_history_store[sessionId] = InMemoryChatMessageHistory();
    return chat_history_store[sessionId];


strOutputParser = StrOutputParser();

chain = promTemplate | printPromotion | chatModel | strOutputParser

conversation_chain = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=getSessionHistory,
    input_messages_key="input",
    history_messages_key="history"
)

if __name__ == '__main__':
    sessionConfig = {"configurable": {"session_id": "user_001"}};

    print(conversation_chain.invoke({"input": "小明有一只狗"}, sessionConfig))
    print(conversation_chain.invoke({"input": "小明有三只乌龟"}, sessionConfig))
    print(conversation_chain.invoke({"input": "小明有几个宠物"}, sessionConfig))
