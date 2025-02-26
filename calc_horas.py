"""
Programa: calc_horas
Descrição: Este programa calcula salario bruto, salario liquido e total de descontos para um prof. horista
Autor: Filipe Eich
Data: 25/02/2025
Versao: 0.0.1
"""



#Alocaçao de memoria

horas=""
bruto=""
desc=""
liq=""


#preencher as demais variáveis que eu for usando




#Entrada de dados

horas = float(input("\nOlá! Vamos calcular o salário para algum Professor de sua escolha? Digite as horas trabalhadas:"))




# Processamento de dados

bruto = 40*horas
desc=0.3*bruto

liq = bruto - desc



#Saida de dados



print(f"\nOk! Seguem os valores correspondentes à remuneração deste Professor,\n\nSalário Bruto: R${bruto}\n\nDescontos: R${desc}\n\nSalário Líquido: R${liq}")




