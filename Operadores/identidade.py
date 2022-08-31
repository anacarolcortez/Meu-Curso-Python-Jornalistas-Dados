print("*** Operadores Identidade ***")

"""
Este operador verifica se duas variáveis apontam para o mesmo espaço na memória, ou seja, se representam o mesmo objeto. 
"""

linguagem_amada = "Python"
linguagem_alternativa = "R"
linguagem_data_science = linguagem_amada
linguagem_data_science2 = "Python"

resultado1 = linguagem_amada is linguagem_alternativa
print(resultado1)

resultado2 = linguagem_amada is not linguagem_alternativa
print(resultado2)

resultado3 = linguagem_amada is linguagem_data_science
print(resultado3)

resultado4 = linguagem_amada is linguagem_data_science2
print(resultado4)

# Obs: para comparar valores de strings, inteiros, floats etc, deve usar == ou !=

resultado5 = linguagem_amada == "Python"
print(resultado5)
