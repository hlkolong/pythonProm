from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(template="我有一个邻居姓{lastname}，生了一个{gender}，帮忙起个名字");

model = OllamaLLM(model="qwen3:4b");

chain = template | model;

res = chain.invoke(input={"lastname":"张","gender":"女孩"})
print(res)