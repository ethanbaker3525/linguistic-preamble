import matplotlib.pyplot as plt
import json
import os
import numpy as np

def get_test_sentence_surprisal(sentence):
    test_sentence = [sentence[-1]]
    for word_surprisal_tuple in reversed(sentence[:-1]):
        if word_surprisal_tuple[0][-1] == ".":
            return  test_sentence
        test_sentence = [word_surprisal_tuple] + test_sentence
    return test_sentence

def plot_surprisal_simple(x_labels, y_mean, title, condition):

    x_idxs = list(range(len(x_labels)))

    plt.figure(figsize=(10, 4))
    plt.title(f"{title} ({condition})")
    # Plot lines
    plt.plot(x_idxs, y_mean, label=condition, linestyle='-', marker='o')
    # Labels and title
    plt.xlabel('Token', fontsize=12)
    plt.ylabel('Surprisal', fontsize=12)
    # Grid and legend
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=10)
    # Ticks
    plt.xticks(fontsize=10)
    plt.xticks(x_idxs, x_labels, rotation=-45)
    plt.yticks(fontsize=10)
    # Tight layout
    plt.tight_layout()
    # Show or save the plot
    plt.savefig(f"plots/{title} {condition}.png".replace(" ", "_"))
    plt.close()

def plot_surprisal(data, key):

    for condition, sentences in data[key].items():

        title = key.replace("_", " ")
        condition = condition.replace("_", " ")
        x_labels = [token for token, surprisal in get_test_sentence_surprisal(sentences[0])]
        y_sum = np.zeros([len(x_labels)], dtype=np.float64)

        for sentence in sentences:
            sentence = get_test_sentence_surprisal(sentence) # get only the final (test) sentence
            y_sum += np.array([surprisal for token, surprisal in sentence])

        y_mean = y_sum / len(sentences)
        
        plot_surprisal_simple(x_labels, y_mean, title, condition)

if __name__ == "__main__":

    results = {}
    for fname in os.listdir("results"):
        results[fname.strip(".json")] = json.load(open(f"results/{fname}", "r"))

    for key in results:
        print(key)
        plot_surprisal(results, key)
    