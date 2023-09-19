import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("file", type=Path)

args = parser.parse_args()

if not args.file.exists():
    print("Arquivo não existe!")
    exit(1)

fofocas = []

print("Entrada:\n")
with open(args.file, "r") as file:
    # print(file.read())
    for line in file:
        line = line.strip()
        if line.startswith("#"):
            continue

        parts = line.split(":")
        if len(parts) != 2:
            continue

        velha = int(parts[0].strip())
        amigas = parts[1].strip().split()
        # print(velha, amigas, len(amigas), (1/len(amigas)), (1/len(amigas) - (0.1 / len(amigas))))
        # print(velha, end=": ")

        # for amiga in amigas:
        #     print(amiga, end=" ")
        # print()
        print(f"{velha}: {amigas}")
        
        array = {}
        quantidadeAmigas = len(amigas)
        array[velha] = -1

        for amiga in amigas:
            amiga = int(amiga)
            array[amiga] = 1/quantidadeAmigas - (0.1 / quantidadeAmigas)

        fofocas.append(array)


print("\n\n###########\n\n")


matriz = []
results = []
for line in fofocas:
    linha = []
    for x in range(1, len(fofocas) + 1):
        if x in line:
            linha.append(line[x])
        else:
            linha.append(0)

    matriz.append(linha)
    results.append(-1)

for linha in range(len(matriz)):
    for elemento in matriz[linha]:
        print(f"{elemento:5.2f}", end=" ")
    print(f" = {results[linha]}")