# Setup Embeddings
import os
OLLAMA_HOST = os.environ.get('OLLAMA_HOST')
if OLLAMA_HOST == None or OLLAMA_HOST == "":
    OLLAMA_HOST = "http://localhost"
from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings(base_url=f'{OLLAMA_HOST}:11434', model="llama3:8b")


# Setup Embeddings Database
from langchain_chroma import Chroma

# Load text document
from pprint import pprint
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
raw_documents = TextLoader('message.txt').load()


from langchain_text_splitters.spacy import SpacyTextSplitter
text_splitter = SpacyTextSplitter(chunk_size=10, chunk_overlap = 1)
# text_splitter = CharacterTextSplitter(
#     # separator = "\'",
#     chunk_size=100,
#     chunk_overlap=0,
#     length_function=len)
documents = text_splitter.split_documents(raw_documents)

pprint(documents)

# Raw Text

# from langchain.docstore.document import Document
# raw_documents =  Document(page_content="text", metadata={"source": "local"})


# Load Documents

# db = Chroma.from_documents(
#     documents,
#     embeddings,
#     persist_directory="./chroma_db"
#     )

# query = "I Like Cooking"
# docs = db.similarity_search(query)
# pprint(docs)
