import pandas as pd
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")


# create a dictionary in from dataframe
new_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output = [new_dict[i] for i in user_input]
print(f"Your coded word is: {output}")