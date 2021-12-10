from tkinter import *
from tkinter import ttk
import funcoes as f

f.montarTabela()

# ------------ GUI --------------
root = Tk()
root.title('Crud de funcionários')
root.geometry('800x600')
root.resizable(FALSE,FALSE)

# ---------- WIDGETS -----------

# FRAME
frameCadastro = Frame(root).place(relx=0,rely=0,relwidth=1,relheight=0.4)
frameData = Frame(root).place(relx=0,rely=0.4,relwidth=1,relheight=0.6)

# TREEVIEW
bancoDados = ttk.Treeview(frameData,height=4,column=("col1","col2","col3","col4","col5","col6"))
# => Heading
bancoDados.heading("#0",text='')
bancoDados.heading("#1",text='ID')
bancoDados.heading("#2",text='Nome')
bancoDados.heading("#3",text='Departamento')
bancoDados.heading("#4",text='Salario')
bancoDados.heading("#5",text='Email')
bancoDados.heading("#6",text='Telefone')
# => Columns
bancoDados.column("#0",width=0)
bancoDados.column("#1",width=20)
bancoDados.column("#2",width=100)
bancoDados.column("#3",width=70)
bancoDados.column("#4",width=30)
bancoDados.column("#5",width=100)
bancoDados.column("#6",width=70)
# => Place
bancoDados.place(relx=0.01,rely=0.42,relwidth=0.95,relheight=0.56)

f.verLista(bancoDados)

# LABEL
labelNome = Label(frameCadastro, text='NOME: ',anchor=W,fg='#245af0',font='verdana 9 bold').place(relx=0.05,rely=0.04,relwidth=0.2,relheight=0.04)
labelDepartamento = Label(frameCadastro, text='DEPARTAMENTO: ',anchor=W,fg='#245af0',font='verdana 9 bold').place(relx=0.05,rely=0.09,relwidth=0.2,relheight=0.04)
labelSalario = Label(frameCadastro, text='SALARIO: ',anchor=W,fg='#245af0',font='verdana 9 bold').place(relx=0.05,rely=0.14,relwidth=0.2,relheight=0.04)
labelNascimento = Label(frameCadastro, text='EMAIL: ',anchor=W,fg='#245af0',font='verdana 9 bold').place(relx=0.05,rely=0.19,relwidth=0.2,relheight=0.04)
labelTelefone = Label(frameCadastro, text='TELEFONE: ',anchor=W,fg='#245af0',font='verdana 9 bold').place(relx=0.05,rely=0.24,relwidth=0.2,relheight=0.04)
labelId = Label(frameCadastro, text='ID: ',anchor=W,fg='#245af0',font='verdana 9 bold').place(relx=0.75,rely=0.04,relwidth=0.2,relheight=0.04)

# ENTRY
entryNome = Entry(frameCadastro)
entryDepartamento = Entry(frameCadastro)
entrySalario = Entry(frameCadastro)
entryEmail = Entry(frameCadastro)
entryTelefone = Entry(frameCadastro)
entryId = Entry(frameCadastro)

entryNome.place(relx=0.27,rely=0.04,relwidth=0.35,relheight=0.04)
entryDepartamento.place(relx=0.27,rely=0.09,relwidth=0.35,relheight=0.04)
entrySalario.place(relx=0.27,rely=0.14,relwidth=0.35,relheight=0.04)
entryEmail.place(relx=0.27,rely=0.19,relwidth=0.35,relheight=0.04)
entryTelefone.place(relx=0.27,rely=0.24,relwidth=0.35,relheight=0.04)
entryId.place(relx=0.80,rely=0.04,relwidth=0.1,relheight=0.04)

def clickDuplo(event):
    f.limparDados()
    bancoDados.selection()

    for n in bancoDados.selection():
        col1, col2, col3, col4, col5, col6 = bancoDados.item(n, 'values')
        entryId.insert(END,col1)
        entryNome.insert(END,col2)
        entryDepartamento.insert(END,col3)
        entrySalario.insert(END,col4)
        entryEmail.insert(END,col5)
        entryTelefone.insert(END,col6)

# BUTTON
buttonCadastrar = Button(frameCadastro, text='CADASTRAR',bg='#245af0',fg='white',font='Verdana 8 bold',command=f.addFuncionario).place(relx=0.05,rely=0.32,relwidth=0.2,relheight=0.06)
buttonExcluir = Button(frameCadastro, text='EXCLUIR',bg='#245af0',fg='white',font='Verdana 8 bold',command=f.deletarFuncionario).place(relx=0.27,rely=0.32,relwidth=0.2,relheight=0.06)
buttonEditar = Button(frameCadastro, text='EDITAR',bg='#245af0',fg='white',font='Verdana 8 bold',command=f.editarFuncionario).place(relx=0.49,rely=0.32,relwidth=0.2,relheight=0.06)
buttonCSV = Button(frameCadastro, text='EXPORTAR CSV',bg='#245af0',fg='white',font='Verdana 8 bold').place(relx=0.71,rely=0.32,relwidth=0.2,relheight=0.06)

# SCROLLBAR
scrollbar = Scrollbar(frameData,orient=VERTICAL)
scrollbar.place(relx=0.96,rely=0.42,relwidth=0.04,relheight=0.55)
bancoDados.configure(yscroll=scrollbar.set)

bancoDados.bind("<Double-1>", clickDuplo)

root.mainloop()