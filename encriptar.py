from pathlib import Path
from string import ascii_lowercase as LETTERS


def encrypt(string: str, displacement: int) -> str:
    """
    Encrypt a string by applying the indicated offset. Only letters are
    encrypted, numbers and punctuation marks are left unaffected.
    """
    output = ""
    for letter in string.lower():
        position = LETTERS.find(letter)
        if position > -1:
            position = (position + displacement) % len(LETTERS)
            letter = LETTERS[position]
        output += letter
    return output


def encrypt_file(input: str, displacement: int) -> None:
    """
    Encrypts the input file by applying the specified offset. The output file
    has the same name as the input file plus the string: -CRYPTO.
    """
    file = Path(input)
    output = str(file.with_name(file.stem + "-CRYPTO" + file.suffix))
    with open(file, 'r', encoding="utf8") as f_in:
        with open(output, 'w', encoding="utf8") as f_out:
            for line in f_in:
                f_out.write(encrypt(line, displacement))
