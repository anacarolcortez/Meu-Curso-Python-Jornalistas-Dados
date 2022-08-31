# Listas são coleções de dados
# Elas são delimitadas por colchetes
lista = []

# Listas em Python aceitam absolutamente qualquer tipo de dado
lista = ['ana', 'rita', 'catarina', 'soraia']
lista = [1, 2, 3, 4, 5, 6]
lista = [True, False]
lista = [1.2, 1.3, 1.4]

# Inclusive na mesma coleção podemos ter tipos de dados diferentes
nome = 'ana'
listinha = []
lista = ['Python', 3.9, False, 2022, ['Olá, mundo', 'Hello, world',
                                      3, 2, 1, 1, 2], nome, '13', True, listinha, 'Python', 2022]

# Podemos acessar um valor dentro de uma lista pelo seu índice:
print(lista[0])
print(lista[4])
print(lista[4][-1])

# Podemos alterar os valores de dentro de uma lista e seus tipos:
lista[1] = '3.10'
print(lista[1])

# PRINCIPAIS MÉTODOS DE LISTAS, já nativos do Python:

# Adicionar elemento
lista.append('feliz')
print(lista)

# Contar elementos dentro dela
qtd_1 = lista.count(2022)
print(qtd_1)

qtd_e = lista.count('e')
print(qtd_e)

# Mexer na ordem de seus valores
letras = sorted(['g', 'i', 'a', 't', 'm'])
print(letras)

letras_2 = reversed(['e', 't', 'n', 'e', 'r', 'f'])
print(list(letras_2))

# Remover elementos
lista_2 = ['pêra', 'uva', 'maçã', 'salada mista']
lista_2.remove('salada mista')
print(lista_2)

lista_2.pop(0)
print(lista_2)

lista_2.pop()
print(lista_2)

# Descobrir a quantidade de elementos dentro de uma lista: o tamanho da lista
lista_3 = ['rosana', 2, 7, 3.2, False]
print(len(lista_3))

# Descobrir os valores mínimos e máximos
valores = [22, 43, 87, 45, 60, 11]
print(max(valores))
print(min(valores))

# Slice/ fatia (obs: o intervalo é fechado no início e aberto no fim,)
numeros = lista_3[1:4]
# Não inclui o elemento de índice 4
print(numeros)

slice_2 = lista_3[1:]
# se não informar o índice, depois dos ":", ele pega todos os elementos a partir do índice fornecido
print(slice_2)

slice_3 = lista_3[:-1]
# o mesmo vale para o primeiro item do interevalo
print(slice_3)

# Note que é possível contar os índices de uma lista de frente para trás e de trás para frente:

#  0,  1,  2,  3,  4
# -5, -4, -3, -2, -1

# Copiar uma lista
lista_original = [1, 2, 3]
lista_copia = lista_original.copy()
print(lista_copia)
