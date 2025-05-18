import json
import random

strong_crossover_sentences = json.load(open("data/kush_2013_experiment_4_strong_crossover.json", "r"))[1:] # remove the first sentence as it involves Jane
weak_crossover_sentences = json.load(open("data/kush_2013_experiment_5_weak_crossover.json", "r"))[1:]

strong_crossover_conditional_stimuli = {
    ("NoCrossover", "Match"):       "Jane asked which maintenance man had said that he already spoke with Donna regarding the food-fight in the cafeteria.",
    ("NoCrossover", "Mismatch"):    "Jane asked which lunch lady had said that he already spoke with Donna regarding the food-fight in the cafeteria.",
    ("Crossover",   "Match"):       "Jane asked which maintenance man it appeared that he already spoke with regarding the food-fight in the cafeteria.",
    ("Crossover",   "Mismatch"):    "Jane asked which lunch lady it appeared that he already spoke with regarding the food-fight in the cafeteria.",
    ("NoCrossover", "Control"):     "Jane asked which maintenance man had said that Dana already spoke with Jim regarding the food-fight in the cafeteria.",
    ("Crossover",   "Control"):     "Jane asked which maintenance man it appeared that Dana already spoke with regarding the food-fight in the cafeteria."
}

weak_crossover_conditional_stimuli = {
    ("NoCrossover", "Match"):       "Jane asked which janitor had said that his supervisor might have already spoken with Donna regarding the food-fight in the cafeteria.",
    ("NoCrossover", "Mismatch"):    "Jane asked which lunch-lady had said that his supervisor might have already spoken with Donna regarding the food-fight in the cafeteria.",
    ("Crossover",   "Match"):       "Jane asked which janitor it seemed that his supervisor might have already spoken with regarding the food-fight in the cafeteria.",
    ("Crossover",   "Mismatch"):    "Jane asked which lunch-lady it seemed that his supervisor might have already spoken with regarding the food-fight in the cafeteria.",
    ("NoCrossover", "Control"):     "Jane asked which janitor had said that the supervisor might have already spoken with Donna regarding the food-fight in the cafeteria.",
    ("Crossover",   "Control"):     "Jane asked which janitor it seemed that the supervisor might have already spoken with regarding the food-fight in the cafeteria."
    }

pg_sentences = json.load(open("data/lan_pg.json", "r")) # no need to remove the first item, as John has been filtered out
atb_sentences = json.load(open("data/lan_atb.json", "r"))

pg_conditional_stimuli = {
    ("+Filler", "-Gap"):    "I know who John's talking to is going to annoy you soon.",
    ("+Filler", "+Gap"):    "I know who John's talking to is going to annoy soon."
    }

atb_conditional_stimuli = {
    ("+Filler", "-Gap"):    "I know who John met recently and is going to annoy you soon.",
    ("+Filler", "+Gap"):    "I know who John met recently and is going to annoy soon."
    }

def sample_preamble(sentences):
    i = random.randint(0, len(sentences))
    if i == len(sentences):
        return ""
    else:
        return random.choice(sentences[i]) + " " + sample_preamble(sentences[0:i] + sentences[i+1:])

def sample_n_preambles(n, sentences):
    preambles = []
    while n > 0:
        preamble = sample_preamble(sentences)
        if not preamble in preambles and preamble.count(".") > 1:
            preambles.append(preamble)
            n -= 1
    return preambles
