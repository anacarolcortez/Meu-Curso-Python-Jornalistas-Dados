########### IF, ELIF, ELSE #################

"""
If/elif/else é uma estrutura de desvio de fluxo. Como assim? 
O código deve “desviar” o caminho normal para executar uma ação diferente dada uma certa condição.

if => se
elif => else + if: senão.. se 
else => senão
"""

clima_do_dia = "quente"

if clima_do_dia == "quente":
    print("Use roupa leve")
else:
    print("Use agasalho")


dia_quente = False
previsao_chuva = True

if dia_quente and previsao_chuva:
    print("Use roupa leve, porém, leve guarda-chuva")
elif dia_quente and not previsao_chuva:
    print("Use roupa leve")
elif not dia_quente and previsao_chuva:
    print("Use agasalho e leve guarda-chuva")
# elif not dia_quente and not previsao_chuva:
#   print("Use agasalho")
else:
    print("Use agasalho")
