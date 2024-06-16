## Requirements

``` bash
pip install langchain_community
pip install youtube_transcript_api
pip install pytube
from langchain_community.embeddings import OllamaEmbeddings
pip install langchain-chroma
pip install nltk
pip install spacy

pip install llama-index
pip install llama-index-vector-stores-chroma
pip install llama-index-embeddings-huggingface
pip install llama-index chromadb --quiet
pip install chromadb
pip install sentence-transformers
pip install pydantic==1.10.11
pip install IPython
pip install llama-index-embeddings-ollama
pip install llama-index-llms-openai
```

``` bash

pip install sqlite_vss
pip install numpy


pip install datasets
pip install chunkipy
pip install semantic-chunkers
pip install -qU semantic-router
pip uninstall tiktoken
pip install tiktoken==0.7.0
pip install -qU "semantic_router[local]"

```

#### Installing Ollama and `llama:8b` model

Install Ollama from here


``` bash

curl http://localhost:11434/api/pull -d '{"name": "llama3:8b"}'

```


#### yt-dlp

``` bash

yt-dlp --skip-download --write-info-json https://www.youtube.com/watch?v=CN_BDrVjWvU -o youtube-scraiping.json

yt-dlp --skip-download --write-subs --write-auto-subs --sub-lang en --sub-format ttml --convert-subs srt --output "transcript.%(ext)s" https://www.youtube.com/watch?v=CN_BDrVjWvU && sed -i '' -e '/^[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]$/d' -e '/^[[:digit:]]\{1,4\}$/d' -e 's/<[^>]*>//g' ./transcript.en.srt && sed -e 's/<[^>]*>//g' -e '/^[[:space:]]*$/d' transcript.en.srt > output.txt && rm transcript.en.srt



```


#### Bash

``` bash
wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp
chmod +x yt-dlp
sudo mv ty-dlp /bin/local
```