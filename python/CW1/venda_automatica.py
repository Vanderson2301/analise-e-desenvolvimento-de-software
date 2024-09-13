# Ainda não há banco de dados aqui.

# Perguntar qual a idade do cliente

idade = int(input("Qual sua idade? "))

#Aqui vai se verificar a idade e gerar uma sugestão.

if idade <= 18:
    print ("Recomendo o filme Meu Malvado Favorito 3, é um ótimo filme!")

elif idade <= 35:
    print ("Recomendo o filme DeadPool 2, é um filme épico!")

else:
    print ("Recomendo os filmes do Mazaropi!")

# Agora é a disponibilidade

quantidade_ingressos = 1 # Aqui seria a quantiadde de ingressos disponiveis

if quantidade_ingressos > 0:
    print("Ingressos disponíveis!")

else:
    print("Ingressos esgotados!")