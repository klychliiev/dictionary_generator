import pymorphy2
from text_processing import lemmas

morph = pymorphy2.MorphAnalyzer(lang='uk')

new = []
for i in lemmas:
    d = morph.parse(i)[0]
    new.append(d.lexeme)

new1 = []
for i in new:
    x = [y.word for y in i]
    new1.append(x)

