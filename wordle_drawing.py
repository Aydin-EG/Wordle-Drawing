key = input("enter 5 character word: ")
key = key.strip()
pattern = input("enter 6 groups of 5 characters seperated by a space. g=green, y=yellow, b=grey: ")
word_list = []

with open("valid-wordle-words.txt") as words:
    for line in words:
        word_list.append(line.rstrip("\n"))

def find_words():
    answer = ""

    if any(char not in " gyb" for char in pattern): #validates pattern characters
        return "input contains invalid character."

    groups = pattern.split()

    if len(groups) != 6 or any(len(group) != 5 for group in groups): #validates pattern length
        return "input must contain exactly 6 groups of 5 characters."

    for group in groups: #loops through each group in the pattern
        found = False

        for word in word_list: #loops through all of the valid words
            matches = True

            for i, letter in enumerate(group): #loops through each character of the word 
                if letter == "g" and word[i] != key[i]:
                    matches = False
                    break
                elif letter == "y" and (word[i] == key[i] or word[i] not in key):
                    matches = False
                    break
                elif letter == "b" and (word[i] in key):
                    matches = False
                    break

            if matches:
                answer += word + " "
                found = True
                break

        if not found: #if no valid word exits it returns DNE
            answer += "_DNE_ "

    return answer

print(find_words())
