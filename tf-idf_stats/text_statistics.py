from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import stanza
import re

"""Calculation of the tf-idf"""

nlp = stanza.Pipeline(lang='uk', processors='tokenize,mwt,pos,lemma')

texts = ['kaidasheva_simya', 'khiba_revut_voly', 'natsionalism', 'tyhrolovy']


def tf_idf_calculator(x, y):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([x])
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    transpose_df = df.transpose()
    transpose_df.to_csv(f'/home/klychliievfx/projects/words_dictionary/texts/{y}.csv', encoding='utf-8')


for text in texts:
    f = open(f"/home/klychliievfx/projects/words_dictionary/texts/{text}.txt", "r")
    file = f.read(20000)
    matches = re.findall(r"[а-яА-ЯіІїЇґҐєЄ'`ʼ\s]", file, re.MULTILINE)
    doc1 = nlp("".join(matches))
    word_tokens = [token.text for sent in doc1.sentences for token in sent.tokens]
    word_string = " ".join(word_tokens[:3000])
    tf_idf_calculator(word_string, f'{text}')



