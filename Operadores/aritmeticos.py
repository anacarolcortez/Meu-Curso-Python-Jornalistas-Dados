print("*** Operadores Aritméticos ***")

numero1 = 10
numero2 = 3

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
modulo = numero1 % numero2
exponenciacao = numero1 ** numero2

print(soma)  # 13
print(subtracao)  # 7
print(multiplicacao)  # 30
print(divisao)  # 3.333333
print(divisao_inteira)  # 3
print(modulo)  # 1
print(exponenciacao)  # 1000

# A ordem das operações será sempre:
# 1º Divisão ou Multiplicação
# 2º Soma ou Subtração
# A ordem do cálculo é da esquerda para a direita

print((2 + 5) * 3)  # 21
print(1 + 5**2)  # 26
print(5 * 3 + 8)  # 23
print(8 + 5 - 10)  # 3
