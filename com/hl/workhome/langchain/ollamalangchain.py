from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b");

res = model.invoke(input="你是谁啊， 能做什么")
print(res)