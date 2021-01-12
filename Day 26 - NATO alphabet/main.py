import pandas as pd
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")


# create a dictionary in from dataframe
new_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()


def generate_phonetic():
    try:
        output = [new_dict[i] for i in user_input]
    except KeyError:
        print("Sorry! Only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(f"Your coded word is: {output}")


generate_phonetic()
