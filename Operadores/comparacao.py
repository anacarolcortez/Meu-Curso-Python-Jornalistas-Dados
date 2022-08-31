print("*** Operadores de Comparação ***")

numero1 = 10
numero2 = 20

resultado = 10 >= 20
print(resultado)

resultado = 10 <= 20
print(resultado)

resultado = 10 != 20
print(resultado)

resultado = 10 == 20
print(resultado)

print("************************")
rendimentos = float(input("Informe seu rendimento tributável em 2021, em R$:"))

base = 28559.70

if rendimentos < base:
    print("Você está isento do Imposto de Renda 2022")
else:
    print("Você deve pagar imposto em 2022")
