from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(
    file_path="./data/pythen基础语法.txt",
    encoding="utf-8"
)

docs = loader.load();

splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # 分段字符数
    chunk_overlap=50,  # 分段允许的重复字符数
    # 文本自然段落分隔的依据符号
    separators=["\n\n", "\n", ",", ".", "。", "，", " ", "", "!", "?"],
    length_function=len  # 统计字符的依据函数
)

# print(text, flush=True)

documents: list[Document] = splitter.split_documents(docs)

for document in documents:
    print("=" * 20)
    print(document)
