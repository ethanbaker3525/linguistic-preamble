import os

os.environ["TRANSFORMERS_NO_DEEPSPEED"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import json
import random
from tqdm import tqdm

from minicons import scorer

import data

models = {
    "gpt-2": scorer.IncrementalLMScorer('gpt2', 'cpu'),
    #"gpt-j": scorer.IncrementalLMScorer('EleutherAI/gpt-j-6B', 'cpu')
    }

def sentence_surprisals(sentence, model):
    """
    get surprisal at all tokens in a string
    """
    assert isinstance(sentence, str)
    token_surprisals = model.token_score(sentence, surprisal=True, base_two=True)[0]
    return align_surprisal(token_surprisals, sentence)

# modified from https://github.com/umd-psycholing/lm-syntactic-generalization
def align_surprisal(token_surprisals, sentence):
    words = sentence.split(" ")
    token_index = 0
    word_index = 0
    word_level_surprisal = []  # list of word, surprisal tuples
    while token_index < len(token_surprisals):
        current_word = words[word_index]
        current_token, current_surprisal = token_surprisals[token_index]
        current_token = current_token.replace("Ġ", "")
        # token does not match, alignment must be adjusted
        mismatch = (current_word != current_token)
        while mismatch:
            token_index += 1
            current_token += token_surprisals[token_index][0]
            current_surprisal += token_surprisals[token_index][1]
            mismatch = current_token != current_word
        word_level_surprisal.append((current_word, current_surprisal))
        token_index += 1
        word_index += 1
    return word_level_surprisal
     

#print(sentence_surprisals("Hello there! How's it going today? I'm fine, how's the milk-man?", models["gpt-2"]))

if __name__ == "__main__":

    model_name = "gpt-2"
    n = 512
    random.seed("LING449K")

    ### Experiment 1; Kush et al. ###

    ### strong crossover without preamble ###

    surprisals = {"_".join(condition):[] for condition in data.strong_crossover_conditional_stimuli.keys()}

    for condition, sentence in tqdm(data.strong_crossover_conditional_stimuli.items()):
            stimulus = sentence
            surprisals["_".join(condition)].append(sentence_surprisals(stimulus, models[model_name]))

    json.dump(surprisals, open(f"results/{model_name}_surprisals_strong_crossover_without_preamble.json", "w"), indent=4)

    ### strong crossover with preamble ###

    surprisals = {"_".join(condition):[] for condition in data.strong_crossover_conditional_stimuli.keys()}

    for preamble in tqdm(data.sample_n_preambles(n, data.strong_crossover_sentences)):
        for condition, sentence in data.strong_crossover_conditional_stimuli.items():
            stimulus = preamble + sentence
            surprisals["_".join(condition)].append(sentence_surprisals(stimulus, models[model_name]))

    json.dump(surprisals, open(f"results/{model_name}_surprisals_strong_crossover_with_preamble.json", "w"), indent=4)

    ### weak crossover without preamble ###

    surprisals = {"_".join(condition):[] for condition in data.weak_crossover_conditional_stimuli.keys()}

    for condition, sentence in tqdm(data.weak_crossover_conditional_stimuli.items()):
            stimulus = sentence
            surprisals["_".join(condition)].append(sentence_surprisals(stimulus, models[model_name]))

    json.dump(surprisals, open(f"results/{model_name}_surprisals_weak_crossover_without_preamble.json", "w"), indent=4)
    
    ### weak crossover with preamble ###

    surprisals = {"_".join(condition):[] for condition in data.weak_crossover_conditional_stimuli.keys()}

    for preamble in tqdm(data.sample_n_preambles(n, data.weak_crossover_sentences)):
        for condition, sentence in data.weak_crossover_conditional_stimuli.items():
            stimulus = preamble + sentence
            surprisals["_".join(condition)].append(sentence_surprisals(stimulus, models[model_name]))

    json.dump(surprisals, open(f"results/{model_name}_surprisals_weak_crossover_with_preamble.json", "w"), indent=4)


    ### Experiment 2; Lan et al. ###

    ### ATB without preamble ###

    surprisals = {"_".join(condition):[] for condition in data.atb_conditional_stimuli.keys()}

    for condition, sentence in tqdm(data.atb_conditional_stimuli.items()):
            stimulus = sentence
            surprisals["_".join(condition)].append(sentence_surprisals(stimulus, models[model_name]))

    json.dump(surprisals, open(f"results/{model_name}_surprisals_atb_without_preamble.json", "w"), indent=4)

    ### ATB with preamble ###

    surprisals = {"_".join(condition):[] for condition in data.atb_conditional_stimuli.keys()}

    for preamble in tqdm(data.sample_n_preambles(n, data.atb_sentences)):
        for condition, sentence in data.atb_conditional_stimuli.items():
            stimulus = preamble + sentence
            surprisals["_".join(condition)].append(sentence_surprisals(stimulus, models[model_name]))

    json.dump(surprisals, open(f"results/{model_name}_surprisals_atb_with_preamble.json", "w"), indent=4)

    ### PG without preamble ###

    surprisals = {"_".join(condition):[] for condition in data.pg_conditional_stimuli.keys()}

    for condition, sentence in tqdm(data.pg_conditional_stimuli.items()):
            stimulus = sentence
            surprisals["_".join(condition)].append(sentence_surprisals(stimulus, models[model_name]))

    json.dump(surprisals, open(f"results/{model_name}_surprisals_pg_without_preamble.json", "w"), indent=4)

    ### PG with preamble ###

    surprisals = {"_".join(condition):[] for condition in data.pg_conditional_stimuli.keys()}

    for preamble in tqdm(data.sample_n_preambles(n, data.pg_sentences)):
        for condition, sentence in data.pg_conditional_stimuli.items():
            stimulus = preamble + sentence
            surprisals["_".join(condition)].append(sentence_surprisals(stimulus, models[model_name]))

    json.dump(surprisals, open(f"results/{model_name}_surprisals_pg_with_preamble.json", "w"), indent=4)



