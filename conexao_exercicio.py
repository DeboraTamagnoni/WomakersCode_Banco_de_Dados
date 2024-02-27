#Exercicios referentes a "Semana 5: Banco de dados SQL" do bootcamp Data Analytics da WomakersCode

 #Exercícios Banco de dados

import sqlite3

conexao = sqlite3.connect('C:/Users/debor/OneDrive/Área de Trabalho/SQL_Desafio/dados_desafio')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(200), idade INT, curso VARCHAR(50));')


#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(01, "Felipe de Moraes", 18, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(02, "Liliane Tamagnoni", 32, "Estética")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(03, "Fernando Fernandez", 24, "Medicina")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(04, "Amanda Morais", 25, "Ciências Econômicas")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(05, "Mary Goulart", 42, "Medicina")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(06, "Rosangela Borges", 21, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(07, "Arthur Camargo", 22, "Educação Física")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(08, "Andreia Valle", 27, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(09, "Arnaldo Ferreira", 24, "Estética")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(10, "Ademir Lopes", 37, "Ciências Econômicas")')


#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

#registros = cursor.execute('SELECT * FROM alunos')
#for alunos in registros:
#    print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#registros_filtro1 = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
#for alunos in registros_filtro1:
#    print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
#registros_engenharia = cursor.execute('SELECT * FROM alunos WHERE curso == "Engenharia" ORDER BY nome')
#for alunos in registros_engenharia:
#    print(alunos)

#d) Contar o número total de alunos na tabela.
#cursor.execute('SELECT COUNT (*) FROM alunos') #realizando a consulta
#resultado_consulta = cursor.fetchone() #recuperando o resultado da consulta
#total_alunos = resultado_consulta[0] #para devolver o resultado como um único elemento
#print(total_alunos) #imprimindo resultado


#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela. (Vou atualizar a idade da aluna Rosangêla)
#cursor.execute('UPDATE alunos SET idade="24" WHERE nome="Rosangela Borges"')

#b) Remova um aluno pelo seu ID. (Vou remover o aluno de id 8)
#cursor.execute('DELETE FROM alunos WHERE id=08')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
#Insira alguns registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(200), idade INT, saldo FLOAT);')

#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(01, "Salvelina Neves", 55, 5678.32)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(02, "Vanessa Carvalho", 32, 252.10)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(03, "Izaias Silva", 72, 4415.23)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(04, "Adriano Pereira", 22, 78963.65)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(05, "Evan Flávio Borges", 37, 4523.89)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(06, "Ana Amélia Rodriges", 34, 45238.66)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(07, "André Henrique Reis", 48, 2365.87)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(08, "Giovanna Ribas", 27, 48.50)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(09, "Laura Martins", 59, 55448.32)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(10, "Miguel Ferreira", 47, 548521.32)')

#5. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#clientes_mais30 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
#for clientes in clientes_mais30:
#    print(clientes)

#b) Calcule o saldo médio dos clientes.

#cursor.execute('SELECT AVG(saldo) FROM clientes')
#resultado_saldo = cursor.fetchone()
#saldo_medio = resultado_saldo[0]
#print("O saldo médio dos clientes é de:", saldo_medio)

#c) Encontre o cliente com o saldo máximo.

#cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
#resultado_maior_saldo = cursor.fetchone()
#saldo_maximo = resultado_maior_saldo[0]
#print("O cliente como maior saldo é", saldo_maximo)

#d) Conte quantos clientes têm saldo acima de 1000.
#cursor.execute('SELECT COUNT (*) FROM clientes where saldo>1000') #realizando a consulta
#resultado_consulta_saldo = cursor.fetchone() #recuperando o resultado da consulta
#total_clientes_saldo_1000 = resultado_consulta_saldo[0] #para devolver o resultado como um único elemento
#print("O total de clientes com saldo maior que 1000 é", total_clientes_saldo_1000)


#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.

#cursor.execute('UPDATE clientes SET saldo="1256.37" WHERE nome="Ana Amélia Rodriges"')

#b) Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes WHERE nome="Laura Martins"')


#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra

#criando a tabela
#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, id_cliente INT, produto VARCHAR(50), valor FLOAT, FOREIGN KEY (id_cliente) REFERENCES clientes(id));')

#inserindo alguns valores
#cursor.execute('INSERT INTO compras(id, id_cliente, produto, valor) VALUES(01, 03, "Carrinho de bebe cinza", 854.97)')
#cursor.execute('INSERT INTO compras(id, id_cliente, produto, valor) VALUES(02, 06, "Kit Shampoo e Condicionador", 58.95)')
#cursor.execute('INSERT INTO compras(id, id_cliente, produto, valor) VALUES(03, 04, "Aparador de pelos elétrico", 224.87)')
#cursor.execute('INSERT INTO compras(id, id_cliente, produto, valor) VALUES(04, 09, "Máquina de fazer sorvete", 4595.67)')
#cursor.execute('INSERT INTO compras(id, id_cliente, produto, valor) VALUES(05, 10, "Mouse sem fio", 129.65)')

#compras_clientes = cursor.execute('SELECT c.nome, co.produto, co.valor FROM clientes c JOIN compras co ON c.id = co.id_cliente;')
#for cliente in compras_clientes:
#    print(cliente)


conexao.commit()
conexao.close