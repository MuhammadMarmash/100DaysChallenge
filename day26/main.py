import pandas

# new_list = [new_item(code) for item in list if test]
# new_dict = {new_key(code):new_value(code) for (key, value) in dict.items() if test}
# panda dataframe:
# for (index, row) in name_of_the_var.iterrows():
#   do something

dict = {value.letter: value.code for (index, value) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
name = input("Enter a word:").upper()
answer = [dict[letter] for letter in name]
print(answer)
