import configparser

from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate

config = configparser.ConfigParser()
config.read("../labiconfig.ini", "utf-8");

exampleData = [{"word": "大", "antonym": "小"},{"word": "长", "antonym": "短"}]

template = FewShotPromptTemplate(
    prefix="给出给定词的反义词，有如下示例",
    example_prompt=PromptTemplate.from_template("单词：{word}的反义词是：{antonym}"),
    examples=exampleData,
    suffix="基于示例，请告诉我{input_word}的反义词是什么，不知道就回答不知道",
    input_variables=["input_word"]
);

model = Tongyi(model="qwen-max", api_key=config.get("settings", "api_key"))

# chain = template | model;
# res = chain.invoke(input=[{"input_word":"污浊"}, {"input_word":"大陆"}])
# res = chain.invoke(input={"input_word":"污浊"})
text = template.invoke(input={"input_word":"污浊"}).to_string();
res = model.invoke(text);


print(res)
