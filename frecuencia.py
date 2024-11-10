def word_frequency_in_file(input_file: str, output_file: str) -> dict:
    "Analyzes the frequency with which different words occur in a text file."
    frequencies = {}

    with open(input_file, 'r', encoding="utf8") as f:
        for line in f:
            line = line.lower()
            letters = ""
            for character in line:
                if character.isalpha() or character == ' ':
                    letters += character
            words = letters.split()
            for word in words:
                if word in frequencies:
                    frequencies[word] += 1
                else:
                    frequencies[word] = 1

    items = frequencies.items()
    items = sorted(items, key=lambda item: item[1], reverse=True)
    frequencies = dict(items)

    with open(output_file, 'w', encoding="utf8") as f:
        for word in frequencies:
            line = f'{word}: {frequencies[word]}\n'
            f.write(line)

    return frequencies


def main():
    "Test the function"
    file = "data/Asimov, Isaac - Cómo ocurrió.txt"
    output = "data/Asimov-análisis.txt"
    test = word_frequency_in_file(file, output)
    i = 0
    for word in test:
        print(f'{word}: {test[word]}')
        i += 1
        if i >= 10:
            break


main()
