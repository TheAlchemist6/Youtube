import semchunk
from transformers import AutoTokenizer # Neither `transformers` nor `tiktoken` are required,
import tiktoken                        # they are here for demonstration purposes.

chunk_size = 2 # A low chunk size is used here for demonstration purposes.
text = 'The quick brown fox jumps over the lazy dog.'

# As you can see below, `semchunk.chunkerify` will accept the names of all OpenAI models, OpenAI
# `tiktoken` encodings and Hugging Face models (in that order of precedence), along with custom
# tokenizers that have an `encode()` method (such as `tiktoken`, `transformers` and `tokenizers`
# tokenizers) and finally any function that can take a text and return the number of tokens in it.
chunker = semchunk.chunkerify('umarbutler/emubert', chunk_size) or \
          semchunk.chunkerify('gpt-4', chunk_size) or \
          semchunk.chunkerify('cl100k_base', chunk_size) or \
          semchunk.chunkerify(AutoTokenizer.from_pretrained('umarbutler/emubert'), chunk_size) or \
          semchunk.chunkerify(tiktoken.encoding_for_model('gpt-4'), chunk_size) or \
          semchunk.chunkerify(lambda text: len(text.split()), chunk_size)

# The resulting `chunker` can take and chunk a single text or a list of texts, returning a list of
# chunks or a list of lists of chunks, respectively.
assert chunker(text) == ['The quick', 'brown', 'fox', 'jumps', 'over the', 'lazy', 'dog.']
assert chunker([text], progress = True) == [['The quick', 'brown', 'fox', 'jumps', 'over the', 'lazy', 'dog.']]