# Tipos de Variáveis

# String = texto / str
variavel = "Hello, world!"
print(variavel)
print(type(variavel))

variavel = "Olá, Mundo!"
print(variavel)
print(type(variavel))

# Inteiro / int
inteiro = 10
print(inteiro)
print(type(inteiro))

# Float = decimal
decimal = 4.6
print(decimal)
print(type(decimal))

# Boolean / bool
boleana = True
boleana2 = False
print(boleana)
print(boleana2)
print(type(boleana))

resultado = type(boleana) == type(boleana2)
print(resultado)

resultado2 = boleana == boleana2
print(resultado2)

# String
inteiro2 = "10"
print(inteiro2)
print(type(inteiro2))

resultado3 = inteiro == inteiro2
print(resultado3)

inteiro3 = int(inteiro2)
print(inteiro3)
print(type(inteiro3))

decimal2 = float(inteiro3)
print(decimal2)
print(type(decimal2))

# Conversão de Tipos
# para string => str(variavel)
# para int => int(variavel)
# para float => float(variavel)
# para bool => bool(variavel) - Obs: só será False se valor da variável for vazio ("") ou zero (0). Em todos os outros casos, será True.

boleana4 = bool(decimal2)
print(boleana4)

boleana5 = bool("")
print(boleana5)

boleana6 = bool(0)
print(boleana6)

# Nome de variáveis
# Não começar com número, não possuir caracter especial, não misturar maiúsculas e minúsculas, usar sempre snake_case
variavel_texto = "snake_case"
