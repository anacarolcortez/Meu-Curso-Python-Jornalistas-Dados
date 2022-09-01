"""
Dicionários são coleções de dados que possuem pares de 'chave' e 'valor'. Imagine uma tabela: as chaves são os nomes das colunas e os valores são... os valores correspondentes na cédula de um registro (de uma linha).
É um tipo mutável, permite reatribuição de valor
Dicionários são delimitados por colchetes {}
Para acessar um valor, utiliza-se sua chave.
"""
dic = {}

# Dicionários aceitam qualquer tipo como valor. Porém, as chaves só podem ser strings ou inteiras
dicionario_simples = {'chave': 'valor'}
dicionario_simples = {1: 'valor1', 2: 'valor2', 3: 'valor3'}
print(dicionario_simples)

dicionario = {
    "nome": "Ana",
    "idade": 37,
    "altura": 1.6,
    "series": [
        'The God Place', 'The Office',
        'Unbreakable Kimmy Schmidt',
        'Fleabag', 'I may destroy you'
    ],
    2: {}
}

# Para acessar o valor, utiliza-se esta sintaxe:
print(dicionario['nome'])

# É possível alterar valores
dicionario['nome'] = 'Anna'
novo_nome = dicionario.get("nome")
print(novo_nome)

# É possível criar chaves (de mais de uma forma)
dicionario['sobrenome'] = 'Kendrick'

# Dicionário alterado:
print(dicionario)

################################################
# Principais métodos

# Adcionar valor
dicionario.update({'atriz': True})
print(dicionario)

# Remove um valor
dicionario.pop('atriz')
print(dicionario)

# Retorna as chaves do dicionário (lista)
chaves = dicionario.keys()
print(chaves)

# Retorna os valores do dicionário (lista)
valores = dicionario.values()
print(valores)

# Retorna chaves e valores (tupla):
pares_chave_valor = dicionario.items()
print(pares_chave_valor)
