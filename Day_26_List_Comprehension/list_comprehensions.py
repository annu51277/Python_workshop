import pandas as pd

alphabet = pd.read_csv('NATO Phonetic Alphabet.csv')

new_dict = {row.Symbol:row.Code_Word for (index,row) in alphabet.iterrows()}
print(new_dict)

user_word = input('Enter a word:').upper()
nato = [new_dict[letter] for letter in user_word]
print(nato)
