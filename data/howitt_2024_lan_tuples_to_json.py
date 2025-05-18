import json
import os
import random

path = "lm-syntactic-generalization/grammar_outputs/lan_tuples"

atb_tuple_data = []
pg_tuple_data = []

for i in range(3):
    atb_tuple_data += json.load(open(f"{path}/ATB/ATB_{i}_tuple_data.json"))

for i in range(4):
    pg_tuple_data += json.load(open(f"{path}/PG/PG_{i}_tuple_data.json"))

atb_sentences = []
pg_sentences = []

def get_names(strings):
    """
    Roughly returns the subject of the sentence.
    Not perfect, but works well enough to make sure that filler sentences are unrelated.
    """
    names = set([s for s in strings[1:] if s[0].isupper()])
    if len(names) <= 0:
        return set([strings[strings.index("the") + 1]])
    return set([s for s in strings[1:] if s[0].isupper()])

random.seed("lanetal")
random.shuffle(atb_tuple_data)
used_names = set(["John"]) # John must be excluded
for sentence_group in atb_tuple_data:
    sentences = []
    new_names = get_names(list(sentence_group.values())[0]["processed_tokens"])
    if used_names - new_names == used_names:
        used_names = used_names | new_names
        for sentence_data in sentence_group.values():
            sentence = " ".join(sentence_data["processed_tokens"]) + "."
            sentences.append(sentence)
    if len(sentences) > 0:
        atb_sentences.append(sentences)

random.seed("lanetal")
random.shuffle(pg_tuple_data)
used_names = set(["John"]) # John must be excluded
for sentence_group in pg_tuple_data:
    sentences = []
    new_names = get_names(list(sentence_group.values())[0]["processed_tokens"])
    if used_names - new_names == used_names:
        used_names = used_names | new_names
        for sentence_data in sentence_group.values():
            sentence = " ".join(sentence_data["processed_tokens"]) + "."
            sentences.append(sentence)
    if len(sentences) > 0:
        pg_sentences.append(sentences)

json.dump(atb_sentences, open("data/lan_atb.json", "w"), indent=4)
json.dump(pg_sentences, open("data/lan_pg.json", "w"), indent=4)