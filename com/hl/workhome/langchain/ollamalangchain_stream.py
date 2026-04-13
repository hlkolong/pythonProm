from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b");

res = model.stream(input="你是谁啊， 能做什么")

for chunk in res:
    print(chunk, end="", flush=True)