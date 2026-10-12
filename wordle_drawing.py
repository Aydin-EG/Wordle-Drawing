key = input("enter 5 character word:")
pattern = input("enter 6 groups of 5 characters seperated by a space. g=green, y=yellow, b=grey:")
word_list = []
answer = ""

with open("valid-wordle-words.txt") as words:
    for line in words:
        word_list.append(line.rstrip("\n"))

def find_word(pattern):
    if pattern.strip(["g", "y", "b"]):
        return "input contains invalid character."
    
    if len(pattern.strip()) > 30:
        return "input is too long."

    for group in pattern.split(" "):
        for word in word_list:

            matches = True
            for i, letter in enumerate(group):
                if letter == "g" and word[i] != key[i]:
                    matches = False
                    break
                elif letter == "y" and (word[i] == key[i] or key[i] not in word):
                    matches = False
                    break
                elif letter == "b" and key[i] in word:
                    matches = False
                    break

            if matches:
                answer += word
        
    answer += "DNE"

print(find_word())
