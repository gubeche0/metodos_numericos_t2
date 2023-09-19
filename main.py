import argparse
from pathlib import Path

def resolve_linha(linha, variaveis):
    result = 0
    for i in range(len(linha)):
        result += linha[i] * variaveis[i]
    return result

def resolve_matriz(matriz, variaveis):
    results = []
    for linha in matriz:
        results.append(resolve_linha(linha, variaveis))
    return results

def calcula_erro(matriz, results, variaveis):
    results = resolve_matriz(matriz, variaveis)
    erro = 0
    for i in range(len(results)):
        erro += abs(results[i] - variaveis[i])
    return results

def gauss_seidel(matriz, results, precisao):
    x = 0
    chute = [0 for x in range(len(matriz))]

    # for n in chute:
    #     print(f"{n:.5f}", end=" ")
    # print("]")

    while x < 100:
        x += 1
        # new_results = []
        for i in range(len(matriz)):
            # matriz[i] = results[1]
            # value = results[i] + sum([(-1 * matriz[i][j]) * results[j] for j in range(len(matriz)) if j != i])
            value = results[i]
            
            for j in range(len(matriz)):
                if j != i:
                    value += -matriz[i][j] * chute[j]
                
            # value /= matriz[i][i]
            value = value / matriz[i][i]
            # new_results.append(value)
            chute[i] = value


        # print(f"iteração {x}: [", end=" ")
        # for n in chute:
        #     print(f"{n:.5f}", end=" ")
        # print("]")
    
    return chute


parser = argparse.ArgumentParser()
parser.add_argument("file", type=Path)
parser.add_argument("-p", "--precisao", type=float, default=0.0001)

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
            array[amiga] = 0.9/quantidadeAmigas

        fofocas.append(array)


print("\n\n###########\n\n")

matriz = []
results = []
for coluna in range(1, len(fofocas) + 1):
    results.append(-1)

    linha = []
    for l in range(len(fofocas)):
        if coluna in fofocas[l]:
            linha.append(fofocas[l][coluna])
        else:
            linha.append(0)

    matriz.append(linha)

for linha in range(len(matriz)):
    for elemento in matriz[linha]:
        print(f"{elemento:5.2f}", end=" ")
    print(f" = {results[linha]}")


res = gauss_seidel(matriz, results, args.precisao)

# print(f"\n\nResultado =  [", end=" ")
# for n in res:
#     print(f"{n:.3f}", end=" ")
# print("]")

maior = 0
for i in range(len(res)):
    if res[i] > res[maior]:
        maior = i

print(f"\n\nA velha com mais fofoca é a {maior + 1} com {res[maior]:.4f} fofocas")