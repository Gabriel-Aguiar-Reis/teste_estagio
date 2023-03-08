# Exercício 1

Indice = 13
Soma = 0
K = 0
while K < Indice:
    K += 1
    Soma += K
print(Soma) # Resultado final = 91

# Exercício 2

def funcao_fibonacci(entrada):
    valor_inicial = 0
    n = 1
    acumulador = 0
    while acumulador < entrada:
        acumulador += n
        n = valor_inicial
        valor_inicial = acumulador
    if acumulador == entrada:
        print(f'{entrada} faz parte da sequência de Fibonacci.')
    else:
        print(f'{entrada} não faz parte da sequência de Fibonacci.')
funcao_fibonacci(int(input("""Digite o número que deseja descobrir
se faz parte da sequência de fibonacci: """)))

# Exercício 3

# a) 1, 3, 5, 7, 9
# b) 2, 4, 8, 16, 32, 64, 128
# c) 0, 1, 4, 9, 16, 25, 36, 49
# d) 4, 16, 36, 64, 100
# e) 1, 1, 2, 3, 5, 8, 13
# f) 2, 10, 12, 16, 17, 18, 19, 200

# Exercício 4

# Para carro(A) -> S = So + V*t
# S = x
# So = 0
# V = 110 km/h
# t = 1h

# Para caminhão(B) -> S = So + V*t
# S = x
# So = 100 km
# V = 80 km/h
# t = 1 + (1/6) h

# X(A) = 0 + 110 * t
# X(B) = 100 - 80 * (1.166 * t)

# X(A) = X(B)
# 0 + 110 * t = 100 - 80 * (1.166 * t)
# t = 0.491

# X(A) = 110 * 0.491 = 54,01
# Ou seja, os veículos se encontram a 54 Km de Ribeirão Preto

# Embora saibamos a posição do encontro, 
# essa informação é irrelevante para a questão original,
# pois ao se encontrarem, ambos estarão igualmente distantes
# de Ribeirão Preto.

# Exercício 5

def inverte_string(string):
    print (string[::-1])
inverte_string(str(input('Escreva a string que deseja reverter: ')))