from langchain_community.embeddings import DashScopeEmbeddings
import configparser

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");
embed = DashScopeEmbeddings(dashscope_api_key=config.get("settings", "api_key"))
print(embed.embed_query("我喜欢你"))
print(embed.embed_documents(["我喜欢你", "吾中意你", "我爱吃鱼", "我稀饭你"]))
