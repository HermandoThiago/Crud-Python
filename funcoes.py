from tkinter import *
import sqlite3
import gui as g
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from reportlab.pdfgen import canvas
import webbrowser

def limparDados():
    g.entryNome.delete(0, END)
    g.entryDepartamento.delete(0, END)
    g.entryEmail.delete(0, END)
    g.entrySalario.delete(0, END)
    g.entryTelefone.delete(0, END)
    g.entryId.delete(0, END)

def concectaDB():
    global db
    global cursor
    db = sqlite3.connect("funcionarios.db")
    cursor = db.cursor()

def desconectaDB():
    db.close()

def montarTabela():
    concectaDB()
    print('Conectando ao banco de dados...')
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS cadastro (
                        id integer not null primary key,
                        nome varchar(30) not null,
                        departamento varchar(20) not null,
                        salario decimal(7,2),
                        email varchar(30),
                        telefone varchar(12)
                    );
                    """)
    db.commit()
    desconectaDB()

def verLista(data):
    data.delete(*data.get_children())
    concectaDB()
    lista = cursor.execute("""SELECT id, nome, departamento, salario, email, telefone FROM cadastro ORDER BY id ASC;""")
    for i in lista:
        data.insert("", END,values=i)
    desconectaDB()
 
def addFuncionario():
    nome = g.entryNome.get()
    departamento = g.entryDepartamento.get()
    salario = g.entrySalario.get()
    email = g.entryEmail.get()
    telefone = g.entryTelefone.get()

    concectaDB()

    cursor.execute("""INSERT INTO cadastro (nome, departamento, salario, email, telefone)
                        VALUES (?, ?, ?, ?, ?)
                        """, (nome, departamento, salario, email, telefone) )
    
    db.commit()
    desconectaDB()
    verLista(g.bancoDados)
    limparDados()

def deletarFuncionario():
    nome = g.entryNome.get()
    departamento = g.entryDepartamento.get()
    salario = g.entrySalario.get()
    email = g.entryEmail.get()
    telefone = g.entryTelefone.get()
    idfunc = g.entryId.get()

    concectaDB()

    cursor.execute("""DELETE FROM cadastro WHERE id = ?""", [idfunc])
    db.commit()

    desconectaDB()
    limparDados()
    verLista(g.bancoDados)

def editarFuncionario():
    nome = g.entryNome.get()
    departamento = g.entryDepartamento.get()
    salario = g.entrySalario.get()
    email = g.entryEmail.get()
    telefone = g.entryTelefone.get()
    idfunc = g.entryId.get()

    concectaDB()

    cursor.execute("""UPDATE cadastro SET nome = ?, departamento = ?, salario = ?, email = ?, telefone = ? WHERE id = ?""",
                    (nome, departamento, salario, email, telefone, idfunc))
    db.commit()
    
    desconectaDB()
    limparDados()
    verLista(g.bancoDados)

def gerarRelatorioPDF():
    c = canvas.Canvas("funcionarios.pdf")

    concectaDB()
    lista = cursor.execute("""SELECT * FROM cadastro ORDER BY id ASC;""")

    c.setFont("Helvetica-Bold", 20)
    c.drawString(200,790,'FICHA DE FUNCIONÁRIOS')
    
    espaco = 0
    linha = 0
    
    for i in lista:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, 720 - espaco, 'ID: ' + str(i[0]))
        c.drawString(50, 700 - espaco, 'NOME: ' + str(i[1]))
        c.drawString(50, 680 - espaco, 'DEPARTAMENTO: ' + str(i[2]))
        c.drawString(50, 660 - espaco, 'SALÁRIO: ' + str(i[3]))
        c.drawString(50, 640 - espaco, 'EMAIL: ' + str(i[4]))
        c.drawString(50, 620 - espaco, 'TELEFONE: ' + str(i[5]))
        c.rect(20, 620 - (espaco + 20), 550, 2, fill=True, stroke=False)
        espaco = espaco + 150
        linha = linha + 1

        if (linha >= 6):
            espaco = 0
            c.showPage()
            c.setFont("Helvetica-Bold", 10)
            c.drawString(50, 720 - espaco, 'ID: ' + str(i[0]))
            c.drawString(50, 700 - espaco, 'NOME: ' + str(i[1]))
            c.drawString(50, 680 - espaco, 'DEPARTAMENTO: ' + str(i[2]))
            c.drawString(50, 660 - espaco, 'SALÁRIO: ' + str(i[3]))
            c.drawString(50, 640 - espaco, 'EMAIL: ' + str(i[4]))
            c.drawString(50, 620 - espaco, 'TELEFONE: ' + str(i[5]))
            c.rect(20, 620 - (espaco + 20), 550, 2, fill=True, stroke=False)
            espaco = espaco + 150
            linha = 1

    c.showPage()
    c.save()
    webbrowser.open("funcionarios.pdf")
    desconectaDB()