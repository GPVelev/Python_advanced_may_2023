from string import punctuation

with open("../file_handling/text.txt", "r") as file:
    text = file.readlines()

output = open("../file_handling/output.txt", "w")

for i in range(len(text)):
    row = text[i]

    letters, marks = 0, 0

    for char in text[i]:
        if char.isalpha():
            letters += 1
        elif char in punctuation:
            marks += 1

    output.write(f"Line {i+1}: {''.join(text[i][:-1])} ({letters})({marks})\n")

output.close()
