key = input("enter 5 character word:")
pattern = input("enter 6 groups of 5 characters seperated by a space. g=green, y=yellow, b=grey:")
word_list = []
answer = ""

with open("valid-wordle-words.txt") as words:
    for line in words:
        word_list.append(line.rstrip("\n"))

def find_word(group):
    if len(group) > 5:
        return "_____"
    for word in word_list:
        matches = True
        for i, mark in enumerate(group):
            if mark == "g" and word[i] != key[i]:
                matches = False
                break
            elif mark == "y" and (word[i] == key[i] or key[i] not in word):
                matches = False
                break
            elif mark == "b" and key[i] in word:
                matches = False
                break

        if matches:
            return word
    return "_____"


for group in pattern.split(" "):
    answer += find_word(group) + " "

print(answer)