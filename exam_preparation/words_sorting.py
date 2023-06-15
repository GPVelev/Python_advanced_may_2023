def words_sorting(*words):
    words_dict = {word: sum(map(ord, word)) for word in words}

    if sum(words_dict.values()) % 2 ==0:
        return "\n".join([f"{word} - {sum}" for word, sum in sorted(words_dict.items(), key=lambda x: x[0])])

    return "\n".join([f"{word} - {sum}" for word, sum in sorted(words_dict.items(), key=lambda x: -x[1])])




print(
    words_sorting(
        'cacophony',
        'bccolade'
    )
)