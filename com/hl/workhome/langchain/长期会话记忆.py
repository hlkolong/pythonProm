import configparser
import os, json
from typing import Sequence
from warnings import catch_warnings

from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
        # 完整的文件路径
        self.file_path = os.path.join(self.storage_path, self.session_id)
        # 确保文件夹存在
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)

        # 将数据同步写入本地文件
        # 类对象写入是二进制的
        # 可以将BaseMessage消息转成字典（借助json模块以json格式写入）
        new_messages = []
        for message in all_messages:
            d = message_to_dict(message);
            new_messages.append(d)

        # new_messages = [message_to_dict(message) for message in all_messages]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property  # @property使该方法可以不带括号调用，被当成一个属性使用
    def messages(self) -> list:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

promTemplate = PromptTemplate.from_template(
    "你是一个话不多的问答器，你需要根据历史内容给出回应。对话历史：{history}，当用户数据{input}，给出回应"
)
chatModel = ChatTongyi(model="qwen3-max", api_key=config.get("settings", "api_key"));


# jsonOutputParser = JsonOutputParser();

def printPromotion(prom):
    print("=" * 20, prom, "=" * 20)
    return prom


def getSessionHistory(sessionId) -> FileChatMessageHistory:
    return FileChatMessageHistory(sessionId, "./chat_history");


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

    # print(conversation_chain.invoke({"input": "小明有一只狗"}, sessionConfig))
    # print(conversation_chain.invoke({"input": "小明有三只乌龟"}, sessionConfig))
    print(conversation_chain.invoke({"input": "小明有几个宠物"}, sessionConfig))
