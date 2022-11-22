import stanza
import re

nlp = stanza.Pipeline(lang='uk', processors='tokenize,mwt,pos,lemma')

f = open("/home/klychliievfx/projects/words_dictionary/texts/tyhrolovy.txt", "r")
file = f.read(20000)

# regex to remove numbers and punctuation
matches = re.findall(r"[а-яА-ЯіІїЇґҐєЄ'`ʼ\s]", file, re.MULTILINE)
doc1 = nlp("".join(matches))

# word tokens
word_tokens = [token.text for sent in doc1.sentences for token in sent.tokens]
word_string = " ".join(word_tokens[:3000])

doc2 = nlp(word_string)

# word pos
pos_tags = [word.upos for sent in doc2.sentences for word in sent.words]
pos_tagger = [(i,) for i in set(pos_tags)]

# word lemmas
lemmas = [word.lemma for sent in doc2.sentences for word in sent.words]
unique_lemmas = [(i,) for i in set(lemmas)]
