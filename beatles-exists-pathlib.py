from pathlib import Path

files = ["beatles.txt", "data", "data/ejemplo.txt"]
for file in files:
    file = Path(file)
    if file.exists():
        if file.is_dir():
            print(f'{file.name} es una carpeta')
        elif file.is_file():
            print(f'{file.name} es un archivo.')
    else:
        print(f'{file.name} no existe.')
