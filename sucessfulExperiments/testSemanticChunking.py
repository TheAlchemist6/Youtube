from pprint import pprint
from semantic_router.encoders import HuggingFaceEncoder
encoder = HuggingFaceEncoder()

from datasets import load_dataset
data = load_dataset("jamescalam/ai-arxiv2", split="train")
content = data[3]["content"]


from semantic_chunkers import StatisticalChunker
chunker = StatisticalChunker(encoder=encoder)
chunks = chunker(docs=[content])

pprint(chunks)
