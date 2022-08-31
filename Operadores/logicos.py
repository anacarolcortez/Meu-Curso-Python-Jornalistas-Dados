print("*** Operadores Lógicos ***")

idade_joao = 19
possui_cnh = True

resultado1 = idade_joao > 18 and possui_cnh
print(resultado1)

resultado2 = idade_joao > 18 and not possui_cnh
print(resultado2)

resultado3 = idade_joao > 18 or possui_cnh
print(resultado3)

resultado4 = idade_joao < 18 or possui_cnh
print(resultado4)

resultado5 = idade_joao < 18 or not possui_cnh
print(resultado5)


