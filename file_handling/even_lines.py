chars_to_replace = ["-", ",", ".", "!", "?"]

with open("../file_handling/text.txt", "r") as file:
    text = file.readlines()

    for row in range(0, len(text), 2):
        for char in chars_to_replace:
            text[row] = text[row].replace(char, "@")

        print(*text[row].split()[::-1], sep=" ")
