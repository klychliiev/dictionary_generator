import stanza
import re

nlp = stanza.Pipeline(lang='uk', processors='tokenize,mwt,pos,lemma')

f = open("/home/klychliievfx/Desktop/Kaidasheva_simya.txt", "r")
file = f.read(20000)

# regex to remove numbers and punctuation
matches = re.findall(r"[а-яА-ЯіІїЇґҐєЄ'`ʼ\s]", file, re.MULTILINE)
new_string = "".join(matches)
doc = nlp(new_string)

# word tokens
word_tokens = [token.text for sent in doc.sentences for token in sent.tokens]

# word pos
pos_tags = [word.upos for sent in doc.sentences for word in sent.words]
pos_tagger = [(i,) for i in set(pos_tags)]

# word lemmas
lemmas = [word.lemma for sent in doc.sentences for word in sent.words]

# database source: word_id, word, lemma, pos
