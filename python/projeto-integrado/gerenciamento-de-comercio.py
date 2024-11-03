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
novo_produto = [
    ("Camisa", "Vestuário", 0, 25, "Gaveta A"),
    ("Calça", "Vestuário", 0, 50, "Gaveta B"),
    ("Vestido", "Vestuário", 0, 10, "Gaveta C"),
]
cursor.executemany('INSERT INTO sistema (nome, categoria, estoque, valor, local) VALUES (?, ?, ?, ?, ?)', novo_produto)
conn.commit()

while True:
    print(f"1 - Ver Todos os Produtos Cadastrados.")
    print(f"2 - Cadastrar Novo Produto.")
    print(f"3 - Alterar Produto Cadastrado.")
    print(f"4 - Excluir Produto Cadastrado.")
    print(f"5 - Sair.")

    menu = int(input("Escolha de 1 a 5 para prosseguir."))

    if menu == 1:
        print(f"Muito Bem, aqui estão todos os produtos cadastrados até o momento.")
        
        cursor.execute('SELECT * FROM sistema')
       
        sistema = cursor.fetchall()
        print("Produtos")
        
        for produtos in sistema:
            print(produtos)
        
        break
    elif menu == 2:
        print(f"Certinho, vamos começar.")
        break
    elif menu == 3:
        print(f"Claro, qual produto você deseja alterar?")
        break
    elif menu == 4:
        print(f"Tudo certo, qual produto você deseja excluir?")
        break
    elif menu == 5:
        print(f"Até mais, te vejo outra hora!")
        break
    
    else:
        print(f"Hum... Acho que esse número não corresponde a nenhuma opção, poderia escolher novamente?")