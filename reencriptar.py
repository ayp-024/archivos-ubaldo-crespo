from pathlib import Path
from string import ascii_lowercase as LETTERS


def reencrypt(string: str, displacement: int) -> str:
    """
    Reencrypt a string by applying the indicated offset. Only letters are
    reencrypted, numbers and punctuation marks are left unaffected. Uppercase
    letters are lost.
    """
    output = ""
    for letter in string.lower():
        position = LETTERS.find(letter)
        if position > -1:
            position = (position - displacement) % len(LETTERS)
            letter = LETTERS[position]
        output += letter
    return output


def reencrypt_file(in_file: str, displacement: int) -> None:
    """
    Reencrypts the input file by applying the specified offset. The output file
    has the same name as the input file plus the string: -UNCRYPTO.
    """
    file = Path(in_file)
    out_file = str(file.with_name(file.stem[:-7] + "-UNCRYPTO" + file.suffix))
    with open(file, 'r', encoding="utf8") as f_in:
        with open(out_file, 'w', encoding="utf8") as f_out:
            for line in f_in:
                f_out.write(reencrypt(line, displacement))


def main():
    reencrypt_file("data/Asimov, Isaac - Cómo ocurrió-CRYPTO.txt", 2)


main()
