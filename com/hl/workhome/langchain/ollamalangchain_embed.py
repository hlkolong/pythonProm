from langchain_ollama import OllamaEmbeddings
import configparser

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");
embed = OllamaEmbeddings(model="qwen3-embedding")
print(embed.embed_query("我喜欢你"))
print(embed.embed_documents(["我喜欢你", "吾中意你", "我爱吃鱼", "我稀饭你"]))
