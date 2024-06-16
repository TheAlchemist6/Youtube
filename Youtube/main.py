from langchain_community.document_loaders import YoutubeLoader

video_urls =[
    "https://www.youtube.com/watch?v=s8z_lBr8Pqs",
    "https://www.youtube.com/watch?v=kPvOWlBqC8k",
    "https://www.youtube.com/watch?v=gO4mi-lKE-Q&t=152s",
    "https://www.youtube.com/watch?v=jZM90QqRJ5Y",
    "https://www.youtube.com/watch?v=YQsZRlo_Ir8",
    "https://www.youtube.com/watch?v=BSxtplMelbc&t=241s",
    "https://www.youtube.com/watch?v=7muTC8eHgTg&t=3s",
    "https://www.youtube.com/watch?v=g9euo693REI&t=1s",
    "https://www.youtube.com/watch?v=GDDpw6OvkV0&t=157s",
    "https://www.youtube.com/watch?v=LwWrpy1EMc0",   
]

transcripts = []

for url in video_urls:
    loader = YoutubeLoader.from_youtube_url(url,
                                         add_video_info=True)
    transcript = loader.load()
    transcripts.append(transcript)

for idx, transcript in enumerate(transcripts):
    print(f"Transcript for video {idx+1}:\n", transcript)

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_text_splitters import CharacterTextSplitter

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(transcripts, embedding_function)

query = "what is consciousness"
transcripts = db.similarity_search(query)
print(transcripts[0])



