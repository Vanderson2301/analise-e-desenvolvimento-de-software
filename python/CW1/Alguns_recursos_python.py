texto = "Explorando as diversidades de linguagens de programação com Python."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de 'e' no texto = {texto.count('e')}")
print(f"As 5 primeiras letras são = {texto[:5]}")

#Lista

cores = ['vermelho', 'preto', 'azul', 'rosa', 'branco']
for cor in cores:
    print(f'Posição = {cores.index(cor)}, cor = {cor}')

#listcomp (Deixar tudo em minusculo) (\n serve pra pular linha)

linguagens = ['JavaScript', 'Python', 'PHP', 'GO', 'C+', 'C++', 'Swift']
print('Antes do listcomp = ', linguagens)
linguagens = [item.lower() for item in linguagens]
print('\nDepois do listcomp = ', linguagens)

#Função Map
#Amplia a função em toda a sequência
#map(funcao, sequencia)
precos_em_dolares = [10, 20, 30 , 40]
taxa_do_dolar = 5.25
precos_em_reais = list(map(lambda x: x * taxa_do_dolar, precos_em_dolares))
print(precos_em_reais)

#Tupla
#A ordem importa
vogais = ('a', 'e', 'i' , 'o', 'u')
print(f"Tipos de objetos vogais = {type(vogais)}")
for p, x in enumerate(vogais):
  print(f"Posição = {p}, Valor = {x}")


        #Atividade  
#Tupla
#Lista de Convidados
convidados = ("Ana", "Beatriz", "Carol", "Daniel", "Henrique")
#Lista de Confirmados
confirmados = ["Ana", "Beatriz"]
#Identificar quem não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
#exibir quem não confirmou
for pessoa in nao_confirmados:
  print(pessoa)
#Enviar lembrete
print("\nEnviando Lembretes para os convidados que ainda não confirmaram!")