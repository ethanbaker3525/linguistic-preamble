"""

open word_surprisal_tuples_list
nco, co = open stimuli_grouped_by_region


"""

import json
import io
import pandas as pd

def fix_separators_in_csv(path:str) -> str: # replaces tabs with spaces
    with open(path) as file:
        text = file.read()
        return text.replace("\t", " ")

def csv_text_to_co_and_nco_dataframes(csv_text:str) -> tuple[pd.DataFrame, pd.DataFrame]:
    csv_texts = csv_text.split(",,,,,,,,,,,,,,,") # split on empty row
    co_df = pd.read_csv(io.StringIO(csv_texts[0]))
    nco_df = pd.read_csv(io.StringIO(csv_texts[1]))
    return co_df, nco_df

def get_grouped_surprisals(groups, word_surprisal_tuples):
    grouped_surprisals = []
    while len(groups) > 0:
        current_group_surprisal = 0
        if isinstance(groups[0], str):
            words = groups[0].strip(".").split(" ") # remove period if there is one and split into list of words
            for word in words:
                assert word == word_surprisal_tuples[0][0] # sanity check
                word_surprisal = word_surprisal_tuples[0][1] # get surprisal of current word
                current_group_surprisal += word_surprisal # add surprisal to the group's surprisal
                word_surprisal_tuples = word_surprisal_tuples[1:] # go to the next word surprisal tuple
        else:
            current_group_surprisal = None

        grouped_surprisals.append(current_group_surprisal) 
        groups = groups[1:] # go to the next group
    return grouped_surprisals


if __name__ == "__main__":

    final_stimuli_df = pd.read_csv("final_stimuli.csv") # read csv (taken directly from "Baker Ling Spreadsheet") to a pandas dataframe
    word_surprisal_tuples_list = json.load(open("word_surprisal_tuples_list.json")) # read previously generated word_surprisal_tuples_list
    csv_text = fix_separators_in_csv("stimuli_grouped_by_region.csv") # read csv (taken directly from "Baker Ling Spreadsheet") to a string
    co_df, nco_df = csv_text_to_co_and_nco_dataframes(csv_text) # create a co dataframe and nco dataframe (useful because of the different column headers for each df)

    all_grouped_surprisals = []

    for df in [co_df, nco_df]:
        for row_idx, row in df.iterrows(): # for each row in the spreadsheet

            # format the identifiers from stimuli_grouped_by_region to match those of final_stimuli
            item_num = row["Item"]
            sco_or_nco = "NCO" if row["co/nco"] == "nco" else "SCO"
            gendermatch = "Match" if row["match/mismatch"] == "match" else "Mismatch"

            matching_row_in_final_stimuli_df = final_stimuli_df[ # find the matching row
                (final_stimuli_df['item'] == item_num) & 
                (final_stimuli_df['SCO/NCO'] == sco_or_nco) & 
                (final_stimuli_df['gendermatch?'] == gendermatch) 
            ]
            assert len(matching_row_in_final_stimuli_df) == 1 # sanity check, there should only be one matching row
            matching_word_surprisal_tuples = word_surprisal_tuples_list[matching_row_in_final_stimuli_df.index[0]] # get the corresponding word surprisal tuples from the word_surprisal_tuples_list

            groups = row[3:-1]
            grouped_surprisals = get_grouped_surprisals(groups, matching_word_surprisal_tuples)

            all_grouped_surprisals.append(grouped_surprisals)

    json.dump(all_grouped_surprisals, open("all_grouped_surprisals.json", "w"), indent=4)
    # printing as csv
    for row in all_grouped_surprisals:
        row = [str(f) for f in row]
        print(",".join(row))

            
            



    #print(co_df)
    #print(nco_df)


