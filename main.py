import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}
word = input("Please enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)
