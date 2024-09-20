import sqlite3

#1. Fazer uma coneção com o banco de dados (ou criar um novo)
conn = sqlite3.connect('exemplo.db')

#2. Agora deve criar um cursos para executar as coisas dentro do banco de dados
cursor = conn.cursor()

#3. Definir um comando para criar uma tabela
create_table = """
CREATE TABLE IF NOT EXISTS Produtos(
    id INTERGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTERGER
);

"""
#Usa o método execute do objeto para criar executar o comando em SQL e criar uma tabela
cursor.execute(create_table)

#confirmar as alterações
conn.commit()

#fechar coneção
conn.close()
#----------------------------------------------------


#adicionar produto
novo_produto = ('Camisa', 19.99, 50)

#commando sql para inserir na tabela
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

#executar comando no SQL para execução
cursor.execute(inserir_produto, novo_produto)

#confirmar as alterações
conn.commit()

#fechar coneção
conn.close()
#----------------------------------------------------

# visualizar produtos
#connectar ao banco de dados
conn = sqlite3.connet ('exemplo.db')
cursor = conn.cursor()

#comando no SQL para selecionar todos os produtos
selecionar_produtos = "SELECT * FROM Produtos"

#executar comando no SQL
cursor.execute(selecionar_produtos)

#Executar todos os regritos e exibilos
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)

#fechar coneção
conn.close()
#----------------------------------------------------

#Atualizar produto
import sqlite3
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#Novo preço e o Id do produto
novo_preco = 29.99
produto_id = 1 #Escolhi o produto 1 pra trocar de preço
#comando no SQL para atualizar o produto
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco, produto_id))

#confirmar as alterações
conn.commit()

#fechar coneção
conn.close()
#----------------------------------------------------

import sqlite3
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#comando no SQL para deletar o produto
produto_id = 2
deletar_produto = "DELETE FROM Produtos WHERE id = ?"
cursor.execute(deletar_produto, (produto_id,))
#confirmar as alterações
conn.commit()
#fechar coneção
conn.close()