from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="./data/stu_json_lines.json",
    jq_schema=".name",
    text_content=False,  # 表示抽取的不是字符串
    json_lines=True  #抽取多行json
)
# loader = JSONLoader(
#     file_path="./data/stus.json",
#     jq_schema=".[].name",  #抽取数组
#     text_content=False  # 表示抽取的不是字符串
# )
# loader = JSONLoader(
#     file_path="./data/stu.json",
#     jq_schema=".name"
# )

document = loader.load()
print(document);
