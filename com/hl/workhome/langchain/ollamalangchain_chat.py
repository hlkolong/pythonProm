from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, ToolMessage, AIMessage
import configparser

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

model = ChatOllama(model="qwen3:4b")
messages = [
    HumanMessage(content="帮我写一首田园诗"),
    AIMessage(content="""绿野延绵接远山，稻香四溢满人间。
                            溪流潺潺绕村过，牧童笛声伴日斜。
                            鸡鸣犬吠寻常事，炊烟袅袅映晚霞。
                            心随自然得宁静，此生愿作田舍家。"""),
    HumanMessage(content=f"翻译一下你描写的景色")
]
res = model.stream(messages)
for chunk in res:
    print(chunk.content, end="", flush=True);
