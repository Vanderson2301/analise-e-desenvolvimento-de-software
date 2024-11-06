import sqlite3

conn = sqlite3.connect('sistema.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS sistema(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    estoque INTEGER NOT NULL,
    valor REAL NOT NULL,
    local TEXT NOT NULL)
''')
def consultar_produto():
    print(f"\nMuito Bem, vamos consultar os produtos.")
    cursor.execute('SELECT * FROM sistema')
    sistema = cursor.fetchall()
    if not sistema:
        print("\nEita, aparentemente não há produtos cadastrados.")
        print("Caso deseje cadastrar algum produto, digite 1.")
        print("Caso deseje voltar, digite 2.")

        opcao_voltar_menu = int(input("\nQual opção você escolhe? "))
        
        if opcao_voltar_menu == 1:
            cadastrar_produto()
        elif opcao_voltar_menu == 2:
            voltar_menu()
        else:
            print("Desculpe, o numero que você escolheu não é correspondente a nenhuma opção, tente novamente. ")
    else:
        print("Aqui estão todos os produtos cadastrados.")
        for produtos in sistema:
            print(produtos) 
def cadastrar_produto():
    tentativas = 0
    limite_de_tentativas = 3
    print(f"Certinho, vamos começar.")
    nome1 = input("\nQual o nome do produto? ")
    categoria1 = input("Qual a categoria do produto? ")
    estoque1 = int(input("Qual a quantidade? "))
    valor1 = float(input("Qual o valor? "))
    while tentativas < limite_de_tentativas:
        print(f"Em qual local vai ficar o produto?")
        print(f"1 - Ele está na Gaveta A")
        print(f"2 - Ele está na Gaveta B")
        print(f"3 - Ele está na Gaveta C")
        print(f"4 - Ele está na Gaveta D")
        escolha_local = int(input("Digite o numero do local que o produto irá ficar. "))            
        if escolha_local == 1:
            local1 = "Gaveta A"
        elif escolha_local == 2:
            local1 = "Gaveta B"
        elif escolha_local == 3:
            local1 = "Gaveta C"
        elif escolha_local == 4:
            local1 = "Gaveta D"
        else:
            tentativas += 1
            if tentativas < limite_de_tentativas:
                print("Desculpe, o numero que você escolheu não é correspondente a nenhum local.")
            else:
                print("Desculpa, você errou muitas vezes, o sistema retornará ao menu.")
        
        cursor.execute('INSERT INTO sistema (nome, categoria, estoque, valor, local) VALUES (?, ?, ?, ?, ?)', 
            (nome1, categoria1, estoque1, valor1, local1))
        conn.commit()
        print("Produto Cadastrado com Sucesso!")
        voltar_menu()
def alterar_produto():
    tentativas = 0
    limite_de_tentativas = 3
    while tentativas < limite_de_tentativas:
        consultar_produto()
        escolher_produto = input("Qual o número do produto que você deseja alterar? ")
        cursor.execute("SELECT 1 FROM sistema WHERE id = ?", (escolher_produto,))
        resultado = cursor.fetchone()
        if resultado:
            while True:
                print("1 - Nome.")
                print("2 - Categoria.")
                print("3 - Estoque.")
                print("4 - Valor.")
                print("5 - Local.")
                escolher_alteracao = int(input("Qual o número do que você deseja alterar no produto? "))
                if escolher_alteracao == 1:
                    nome2 = input("Qual o nome que você deseja colocar? ")
                    cursor.execute("UPDATE sistema SET nome = ? WHERE id = ?",(nome2, escolher_produto))
                    conn.commit()
                    print("Nome Alterado com Sucesso!")
                    voltar_menu()
                elif escolher_alteracao == 2:
                    categoria2 = input("Qual a categoria do produto? ")
                    cursor.execute("UPDATE sistema SET categoria = ? WHERE id = ?",(categoria2, escolher_produto))
                    conn.commit()
                    print("\nCategoria Alterada com Sucesso!")
                    voltar_menu()
                elif escolher_alteracao == 3:
                    estoque2 = int(input("Qual a quantidade? "))
                    cursor.execute("UPDATE sistema SET estoque = ? WHERE id = ?",(estoque2, escolher_produto))
                    conn.commit()
                    print("\nEstoque Alterado com Sucesso!")
                    voltar_menu()
                elif escolher_alteracao == 4:
                    valor2 = float(input("Qual o valor? "))
                    cursor.execute("UPDATE sistema SET valor = ? WHERE id = ?",(estoque2, escolher_produto))
                    conn.commit()
                    print("\nValor Alterado com Sucesso!")
                    voltar_menu()
                elif escolher_alteracao == 5:
                    while tentativas < limite_de_tentativas:
                        print(f"Em qual local vai ficar o produto?")
                        print(f"1 - Ele está na Gaveta A")
                        print(f"2 - Ele está na Gaveta B")
                        print(f"3 - Ele está na Gaveta C")
                        print(f"4 - Ele está na Gaveta D")
                        escolha_local = int(input("Digite o numero do local que o produto irá ficar. "))            
                        if escolha_local == 1:
                            local2 = "Gaveta A"
                        elif escolha_local == 2:
                            local2 = "Gaveta B"
                        elif escolha_local == 3:
                            local2 = "Gaveta C"
                        elif escolha_local == 4:
                            local2 = "Gaveta D"
                        else:
                            tentativas += 1
                            if tentativas < limite_de_tentativas:
                                print("Desculpe, o numero que você escolheu não é correspondente a nenhum local.")
                            else:
                                print("Desculpa, você errou muitas vezes, o sistema retornará ao menu.")
                    cursor.execute("UPDATE sistema SET local = ? WHERE id = ?",(local2, escolher_produto))
                    conn.commit()
                    print("\nLocal Alterado com Sucesso!")
                    voltar_menu()
                else:
                    print("\nDesculpe, o numero que você escolheu não é correspondente a nenhuma opção, tente novamente.")   

        else:
            tentativas +=1
            if tentativas < limite_de_tentativas:
                print("\nDesculpe, o numero que você escolheu não é correspondente a nenhum produto, tente novamente.")    
def relatorio():
    cursor.execute("SELECT * FROM sistema WHERE estoque < 3")
    estoque_baixo = cursor.fetchall()
    if estoque_baixo:
        print("Produtos com estoque abaixo de 3 unidades:")
        for produtos in estoque_baixo:
            print(produtos)
    else:
        print("Não há produtos com estoque abaixo de 3 unidades.")
def voltar_menu():
    while True:
        print(f"\n1 - Ver Todos os Produtos Cadastrados.")
        print(f"2 - Cadastrar Novo Produto.")
        print(f"3 - Alterar Produto Cadastrado.")
        print(f"4 - Excluir Produto Cadastrado.")
        print(f"5 - Relatório de Baixo Estoque.")
        print(f"6 - Sair.")
        menu = int(input("\nEscolha de 1 a 6 para prosseguir. "))
    
        if menu == 1:
            consultar_produto()
        elif menu == 2:
            cadastrar_produto()
        elif menu == 3:
            alterar_produto()
        elif menu == 4:
            consultar_produto()
            tentativas = 0
            limite_de_tentativas = 3
            while tentativas < limite_de_tentativas:
                excluir_produto = input("\n Qual o numero do produto que você deseja excluir? ")
                cursor.execute("SELECT 1 FROM sistema WHERE id = ?", (excluir_produto,))
                resultado = cursor.fetchone()
                if resultado:
                    cursor.execute("DELETE FROM sistema WHERE id = ?",(excluir_produto,))
                    conn.commit()
                    print(f"\nO produto {excluir_produto} excluído com sucesso.")
                    voltar_menu()
                else:
                    tentativas +=1
                    if tentativas < limite_de_tentativas:
                        print("\nDesculpe, o numero que você escolheu não é correspondente a nenhum produto, tente novamente.")
                    else:
                        print("\nDesculpe, você tentou muitas vezes, o sistema voltará ao menu.")
                        voltar_menu()
        elif menu == 5:
            relatorio()
        elif menu == 6:
            print(f"Até mais, te vejo outra hora!")
            break
        else:
            print(f"Hum... Acho que esse número não corresponde a nenhuma opção, poderia escolher novamente?")
voltar_menu()