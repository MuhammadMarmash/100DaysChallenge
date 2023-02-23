with open(file="Input/Names/invited_names.txt") as file:
    # names = file.read().split("\n")
    names = file.readlines()
    str().

with open(file="Input/Letters/starting_letter.txt") as file:
    text = file.read()

for name in names:
    new_text = text.replace("[name]", name)
    with open(file=f"Output/ReadyToSend/letter_for_{name}", mode="w") as file:
        file.write(new_text)
