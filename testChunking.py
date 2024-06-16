from chunkipy import TextChunker, TokenEstimator
from transformers import AutoTokenizer

text = """Napoleon Bonaparte (born Napoleone Buonaparte; 15 August 1769 â€“ 5 May 1821), later known by his regnal name Napoleon I, was a French military commander and political leader who rose to prominence during the French Revolution and led successful campaigns during the Revolutionary Wars. He was the de facto leader of the French Republic as First Consul from 1799 to 1804, then Emperor of the French from 1804 until 1814 and again in 1815. Napoleon's political and cultural legacy endures to this day, as a highly celebrated and controversial leader. He initiated many liberal reforms that have persisted in society, and is considered one of the greatest military commanders in history. His wars and campaigns are studied by militaries all over the world. Between three and six million civilians and soldiers perished in what became known as the Napoleonic Wars.
Napoleon was born on the island of Corsica, not long after its annexation by France, to a native family descending from minor Italian nobility. He supported the French Revolution in 1789 while serving in the French army, and tried to spread its ideals to his native Corsica. He rose rapidly in the Army after he saved the governing French Directory by firing on royalist insurgents. In 1796, he began a military campaign against the Austrians and their Italian allies, scoring decisive victories and becoming a national hero. Two years later, he led a military expedition to Egypt that served as a springboard to political power. He engineered a coup in November 1799 and became First Consul of the Republic.
Differences with the United Kingdom meant France faced the War of the Third Coalition by 1805. Napoleon shattered this coalition with victories in the Ulm campaign, and at the Battle of Austerlitz, which led to the dissolution of the Holy Roman Empire. In 1806, the Fourth Coalition took up arms against him. Napoleon defeated Prussia at the battles of Jena and Auerstedt, marched the Grande ArmÃ©e into Eastern Europe, and defeated the Russians in June 1807 at Friedland, forcing the defeated nations of the Fourth Coalition to accept the Treaties of Tilsit. Two years later, the Austrians challenged the French again during the War of the Fifth Coalition, but Napoleon solidified his grip over Europe after triumphing at the Battle of Wagram.
Hoping to extend the Continental System, his embargo against Britain, Napoleon invaded the Iberian Peninsula and declared his brother Joseph the King of Spain in 1808. The Spanish and the Portuguese revolted in the Peninsular War aided by a British army, culminating in defeat for Napoleon's marshals. Napoleon launched an invasion of Russia in the summer of 1812. The resulting campaign witnessed the catastrophic retreat of Napoleon's Grande ArmÃ©e. In 1813, Prussia and Austria joined Russian forces in a Sixth Coalition against France, resulting in a large coalition army defeating Napoleon at the Battle of Leipzig. The coalition invaded France and captured Paris, forcing Napoleon to abdicate in April 1814. He was exiled to the island of Elba, between Corsica and Italy. In France, the Bourbons were restored to power."""

f = open('./data/message.txt', 'r')
content = f.read()
print(content)
f.close()

text = content

class BertTokenEstimator(TokenEstimator):
    def __init__(self):
        self.bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    def estimate_tokens(self, text):
        return len(self.bert_tokenizer.encode(text))


bert_token_estimator = BertTokenEstimator()

print(f"Num of chars: {len(text)}")
print(f"Num of tokens (using BertTokenEstimator): {bert_token_estimator.estimate_tokens(text)}")
# --> Num of tokens (using BertTokenEstimator): 603

# This creates an instance of the TextChunker class with a chunk size of 512, 
# using token-based segmentation and a custom tokenizer function bert_tokenizer.encode to count tokens.


text_chunker = TextChunker(500, tokens=True, token_estimator=BertTokenEstimator(), overlap_percent=0.3)
chunks = text_chunker.chunk(text)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}, num of tokens: {bert_token_estimator.estimate_tokens(chunk)} -> {chunk}")
    print("\n\n")
