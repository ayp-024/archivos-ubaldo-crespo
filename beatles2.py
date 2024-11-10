f = open("beatles.txt", 'r', encoding="utf8")
for line in f:
    for character in line:
        print(repr(character), end=' ')
    print()
f.close()
