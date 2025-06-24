import os

os.environ["TRANSFORMERS_NO_DEEPSPEED"] = "1" # setting these env variables to force CPU infrencing
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import pandas as pd
import json
import random
from tqdm import tqdm
import numpy as np

from minicons import scorer

def clean_token_surprisal_tuples(token_surprisal_tuples): # removes meta characters (â,Ģ,Ļ,Ġ) from token_surprisal_tuples 
    clean_token_surprisal_tuples = [] 
    for token, surprisal in token_surprisal_tuples:
        token = token.replace("Ġ", "")
        token = token.replace("âĢ", "")
        token = token.replace("Ļ", "’") # this token corresponds to ' in words like couldn't
        clean_token_surprisal_tuples.append((token, surprisal))
    return clean_token_surprisal_tuples

# modified from https://github.com/umd-psycholing/lm-syntactic-generalization
def align_surprisal(token_surprisal_tuples, sentence):
    token_surprisal_tuples = clean_token_surprisal_tuples(token_surprisal_tuples) # remove meta characters from tokens
    words = sentence.split(" ")
    token_index = 0
    word_index = 0
    word_level_surprisal = []  # list of word, surprisal tuples
    while token_index < len(token_surprisal_tuples):
        current_word = words[word_index]
        current_token, current_surprisal = token_surprisal_tuples[token_index]
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

def get_surprisal_at_critical_pronoun(word_surprisal_tuples:list) -> float: 
    for word, surprisal in word_surprisal_tuples: # for each word in the list
        if word in ["he", "she"]: # does the word match he or she
            return surprisal # if so, return the surprisal at that region
    assert False # if no pronoun is found, throw an error

if __name__ == "__main__":
    
    df = pd.read_csv("final_stimuli.csv") # read csv (taken directly from "Baker Ling Spreadsheet") to a pandas dataframe
    sentences = df["sentence"]
    
    model = scorer.IncrementalLMScorer('gpt2', 'cpu') # initialize LM

    # getting the surprisal for each word in each sentence

    word_surprisal_tuples_list = [] # list of all the token_surprisal_tuples generated

    for sentence in sentences:
        token_surprisal_tuples = model.token_score(sentence, surprisal=True, base_two=True)[0] # token_score() outputs a length 1 list with a list of tuples, each containing the token and the surprisal at that token
        # -> [(tok0, 0.0), (tok1, 1.0), ...]
        word_surprisal_tuples = align_surprisal(token_surprisal_tuples, sentence) # groups multiple tokens comprising a single word by summing their surprisals
        # -> [(word0, 0.0), (word1, 1.0), ...]
        word_surprisal_tuples_list.append(word_surprisal_tuples)

    json.dump(word_surprisal_tuples_list, open("word_surprisal_tuples_list.json", "w"), indent=4) # save the outputs

    # finding the surprisals for the critical pronouns

    surprisals_at_critical_pronouns = [] # list that will contain the surprisal values of only the critical pronoun of each sentnce 

    for word_surprisal_tuples in word_surprisal_tuples_list:
        surprisal_at_critical_pronoun = get_surprisal_at_critical_pronoun(word_surprisal_tuples)
        surprisals_at_critical_pronouns.append(surprisal_at_critical_pronoun)

    json.dump(surprisals_at_critical_pronouns, open("surprisals_at_critical_pronouns.json", "w"), indent=4) # save the outputs

    # finding the average surprisal for the critical pronoun for each condition

    surprisals_at_critical_pronouns_by_conditions = ([], [], [], []) # 4-tuple of lists, one for each of SCO-Match, SCO-Mismatch, NCO-Match, NCO-Mismatch

    for i, surprisal_at_critical_pronoun in enumerate(surprisals_at_critical_pronouns):
        surprisals_at_critical_pronouns_by_conditions[i%4].append(surprisal_at_critical_pronoun) # appends item with index n % 4 == x to surprisals_at_critical_pronouns_by_conditions[x]

    average_surprisals_at_critical_pronouns_by_conditions = [] # list that will contain the 4 averages (by condition) of the surprisals at the critical prnoun

    for surprisals_at_critical_pronouns_by_condition in surprisals_at_critical_pronouns_by_conditions:
        average_surprisals_at_critical_pronouns_by_condition = np.mean(surprisals_at_critical_pronouns_by_condition)
        average_surprisals_at_critical_pronouns_by_conditions.append(average_surprisals_at_critical_pronouns_by_condition)

    json.dump(average_surprisals_at_critical_pronouns_by_conditions, open("average_surprisals_at_critical_pronouns_by_conditions.json", "w"), indent=4) # save the outputs

    


    


    


