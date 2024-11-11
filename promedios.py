from math import ceil


def average_grades_in_file(input_file: str, output_file: str):
    "docstring"
    with open(input_file, 'r', encoding="utf8") as in_f:
        with open(output_file, 'w', encoding="utf8") as out_f:
            for line in in_f:
                line = line.strip().split()
                grades = [int(i) for i in line[2:]]
                average = ceil(sum(grades) / len(grades) * 10) / 10
                out_f.write(f'{line[1].upper()}, {line[0]}: {average:.1f}\n')


def main():
    average_grades_in_file("data/calificaciones.txt", "data/promedios.txt")


main()
