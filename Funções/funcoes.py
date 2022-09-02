################### FUNÇÕES #######################

"""
As funções são ótimos recursos para tornar o nosso código mais legível e modular
Elas ajudam a reduzir repetições de instruções e facilitam também a manutenção do código,
pois concentram, em um só lugar, "tudo" relacionado a um assunto.
"""


def soma(x, y):
    return x+y


def subtracao(x, y):
    return x-y


def multiplicacao(x, y):
    return x*y


def divisao(y, x=2):
    return x/y


def so_li_verdades():
    return "Python é legal!"


# INVOCANDO FUNÇÕES

def programa():
    num1 = 10
    num2 = 3

    print(soma(num1, num2))
    print(multiplicacao(soma(num1, num2), num2))


programa()
