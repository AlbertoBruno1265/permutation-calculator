def fatorial(valor):
    result = 1
    for l in range(valor, 0, -1):
        result *= l

    return result

palavra = str(input("Digite a frase a ser permutada: ")).upper()

letras = {}

repeticao = []

for l in palavra:
    
    if l not in letras:
        letras[l] = 1

    else:
        letras[l] += 1


for k, v in letras.items():
    if v > 1:
        repeticao.append(v)
div = 1
for n in repeticao:
    div *= fatorial(n)

conta = fatorial(len(palavra))/div
print(conta)



