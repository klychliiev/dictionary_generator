import pandas as pd
import text_processing as tp

df = pd.read_csv('/home/klychliievfx/Desktop/wlist.csv', index_col=0, header=None, squeeze=True).to_dict()

definitions = []
for i in tp.lemmas:
    if i in df.keys():
        definitions.append(df[i])
    else:
        definitions.append('nun')


data = list(zip(list(range(1, len(tp.word_tokens) + 1)), tp.word_tokens, tp.lemmas, definitions, tp.pos_tags))
