from pprint import pprint

# Read File into context variable
f = open('./data/message.txt', 'r')
content = f.read()
print(content)
f.close()

def split_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


split_document = split_text(content, 1000)
pprint(split_document)
