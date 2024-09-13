# Lista de Filmes

filmes = ["Filmes 1", "Filmes 2", "Filmes 3", "Filmes 4", "Filmes 5"]

# Mensagem de Boas Vindas

print ("Olá, Bem vindo a nossa classificação de filmes!")
print ("Há cinco filmes para serem classificados.")
print ("Digite '0' quando quiser parar a classificação.")

#Loop de Mensagens

for filme in filmes:
    #Solicita a classificação do Usuário
    classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? (ou 0 para parar):")
    
    #Verifica se o Usuário deseja Parar
    if classificacao == "0":
        print("Que pena que você não irá classificar mais os filmes.")
        break #Esse comando vai encerrar o loop

    #Converter a classificação para um numero inteiro
    classificacao = int(classificacao)

    #verifica se a classificação está dentro do intervalo válido
    if classificacao < 1 or classificacao > 5:
        print("Por favor, digite um número entre 1 e 5.")
    else:
        #Exibe a classificação e passa para o proximo filme
        print(f"Você classificou '{filme}' com {classificacao} estrelas. ")

#Mensagem de agradecimo ao finalizar
print("Muito Obrigado por classificar os filmes!")