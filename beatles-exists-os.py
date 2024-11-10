import os.path

file = "beatles.txt"
if os.path.isfile(file):
    print(f"El archivo '{file}' existe.")
else:
    print(f"El archivo '{file}' no exite.")
