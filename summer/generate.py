import os

os.environ["TRANSFORMERS_NO_DEEPSPEED"] = "1" # setting these env variables to force CPU infrencing
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import pandas as pd
import random
from tqdm import tqdm

from minicons import scorer

# modified from https://github.com/umd-psycholing/lm-syntactic-generalization
def align_surprisal(token_surprisal_tuples, sentence):
    words = sentence.split(" ")
    token_index = 0
    word_index = 0
    word_level_surprisal = []  # list of word, surprisal tuples
    while token_index < len(token_surprisal_tuples):
        current_word = words[word_index]
        current_token, current_surprisal = token_surprisal_tuples[token_index]
        current_token = current_token.replace("Ġ", "")
        # token does not match, alignment must be adjusted
        mismatch = (current_word != current_token)
        while mismatch:
            token_index += 1
            current_token += token_surprisal_tuples[token_index][0]
            current_surprisal += token_surprisal_tuples[token_index][1]
            mismatch = current_token != current_word
        word_level_surprisal.append((current_word, current_surprisal))
        token_index += 1
        word_index += 1
    return word_level_surprisal

if __name__ == "__main__":
    
    df = pd.read_csv("final_stimuli.csv") # read csv (taken directly from "Baker Ling Spreadsheet") to a pandas dataframe
    sentences = df["sentence"]

    model = scorer.IncrementalLMScorer('gpt2', 'cpu') # initialize LM

    for sentence in sentences:
        token_surprisal_tuples = model.token_score(sentence, surprisal=True, base_two=True)[0] # outputs a length 1 list with a list of tuples, each containing the token and the surprisal at that token
        word_surprisal_tuples = align_surprisal(token_surprisal_tuples, sentence)

