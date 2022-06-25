print('Questionário para a preparação dos dois dias de IF')

#Variaveis

numero_de_placas = float(input('Quantas placas serão utilizadas?\n'))

numero_de_poços = float(input('Quantos poços serão usados nessa IF?\n'))

minimo_por_poço = float(input('Qual a quantidade miníma de liquido que o poço suporta?\n'))

fator_de_diluição_primario = float(input('Qual a diluição do anticorpo primário?\n'))

fator_de_diluição_secundário = float(input('Qual a diluição do anticorpo secundário\n'))

#Cálculos:

print('Fixação')

def fixação():
    print('Você vai precisar dessa quantidade em microlitros de PFA.')
    print(float((numero_de_poços * minimo_por_poço) * 1.1))
fixação()

def pbs():
    print('Você vai precisar dessa quantidade em microlitros de PBS')
    print(float((numero_de_poços * minimo_por_poço) * 1.1))
pbs()

print('Materiais necessários para a permeabilização e para o restante da IF')

def pbst():
    print('Você vai precisar dessa quantidade em microlitros de PBS-T 0,3%.')
    print(float(((numero_de_poços * minimo_por_poço) * 1.1) * 7) * numero_de_placas)
pbst()

def pré_bloqueio0():
    print('Você vai precisar dessa quantidade em microlitros de pré-bloqueio par o processo inteiro de IF')
    print(float(((numero_de_poços * minimo_por_poço) * 1.1) * 3) * numero_de_placas)
pré_bloqueio0()

print('Pimeiro dia de IF')

def anticorpo_primário():
    print('Você vai precisar dessa quantidade em microlitros de anticorpo primário:')
    print(float(((minimo_por_poço / fator_de_diluição_primario) * numero_de_poços) * 1.1) * numero_de_placas)
anticorpo_primário()

print('Segundo dia de IF')

def anticorpo_secundário():
    print('Você vai precisar dessa quantidade em microlitros de anticorpo secundário')
    print(float(((minimo_por_poço / fator_de_diluição_primario) * numero_de_poços) * 1.1) * numero_de_placas)
anticorpo_secundário()

credito = input('Feito por Lucas Vicente')
