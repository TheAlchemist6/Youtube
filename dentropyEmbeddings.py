import os
OLLAMA_HOST = os.environ.get('OLLAMA_HOST')
if OLLAMA_HOST == None or OLLAMA_HOST == "":
    OLLAMA_HOST = "http://localhost"


from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings(base_url=f'{OLLAMA_HOST}:11434', model="llama3:8b")
text = "This is a test document. and Dentropy was here"
# text = "a"
query_result = embeddings.embed_query(text)

print(text)
print(query_result)
