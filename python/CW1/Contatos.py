import sqlite3
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Agenda(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    numero TEXT,
    email TEXT )
'''
)
novo_contato = [
    ("Vanderson", "(82) 9 9957-3521", "Vanderson2301@gmail.com"),
    ("Aleatório", "555-555-555", "Testando123@gmail.com"),
    ("Aleatório2", "333-333-333", "Ola123@gmail.com"),
]
cursor.executemany('INSERT INTO Agenda (nome, numero, email) VALUES (?, ?, ?)', novo_contato)
conn.commit()

#Para Ler a agenda
cursor.execute('SELECT * FROM Agenda')

agenda = cursor.fetchall()

print("Contatos")

for contato in agenda:

    print(contato)

# UPDATE (Atualização do número de telefone do contato com ID 2)

novo_telefone = '999-999-9999'

contato_id = 2

cursor.execute('UPDATE Agenda SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))

conn.commit()

# DELETE (Exclusão do contato com ID 1)
contato_id_para_excluir = 1
cursor.execute('DELETE FROM Agenda WHERE id = ?', (contato_id_para_excluir,))
conn.commit()

# Fechando a conexão
conn.close()