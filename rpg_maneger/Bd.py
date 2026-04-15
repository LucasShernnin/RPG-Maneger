import sqlite3

conexão = sqlite3.connect("Banco de dados.db")
cursor = conexão.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS criacão_de_personagens(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            jogador TEXT NOT NULL,
            personagem TEXT NOT NULL,
            nex INTEGER NOT NULL,
            classe TEXT NOT NULL,
            p_culto INTEGER NOT NULL,
            p_rebeldes INTEGER NOT NULL
            )""")


cursor.execute(""" INSERT INTO criacão_de_personagens
                              (jogador, personagem, classe, nex, p_culto, p_rebeldes) VALUES
                              (?, ?, ?, ?, ?, ?)""",
                              (
                            personagem['user'],
                            personagem['nome'],
                            personagem['classe'],
                            personagem['nex'],
                            personagem['prestigio_culto'],
                            personagem['prestigio_rebeldes']
                              ))