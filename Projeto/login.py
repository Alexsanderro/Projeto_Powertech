import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox
import requests

class BackEnd():
    def __init__(self):
        self.conecta_db()
        self.desconecta_db()
        self.criar_tabela()
        self.cadastrar_usuario()

    def conecta_db(self):
        self.conn = sqlite3.connect('Sistema_cadastro.db')
        self.cursor = self.conn.cursor()
        print('Banco de dados conectado')

    def desconecta_db(self):
        self.conn.close()
        print('Banco de dados desconectado')

    def criar_tabela(self):
        self.conecta_db()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXIST Usuarios (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Usurname TEXT NOT NULL,
                Email TEXT NOT NULL,
                Password TEXT NOT NULL,
                ConfPassword TEXT NOT NULL
            );
        ''')
        self.conn.commit()
        print('Tabela criada com sucesso!')
        self.desconecta_db()

    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro.get('')
        self.email_cadastro = self.email_entry.get()
        self.password_cadastro = self.password_entry.get()
        self.cpassword_cadastro = self.cpassword_entry.get()
        msg = messagebox.showinfo(title='Estado do Cadastro', message='Usuario cadastrado com sucesso!')

        print(self.username_cadastro)


janela = ctk.CTk()

class Application(ctk.CTk, BackEnd):
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode('dark') #Setar a jenala preta
        ctk.set_default_color_theme('dark-blue') #Setar janela preta com botoes azuis

    def tela(self):
        janela.geometry('900x600') #criar tamanho da jenela
        janela.title('Login') #titulo da jenela
        janela.iconbitmap('Projeto\powertech.ico') #icone da janela
        janela.resizable(False, False) #fazer com que o usuario nao mexa na espessura da janela
    
    def tela_login(self):
        #Imagem da Tela
        img = PhotoImage(file='Projeto\powertech(fullsemfundo).png') #imagem que aparece ao lado do menu
        label_img = ctk.CTkLabel(master=janela, image=img, text=None) #coloque a imagem na janela
        label_img.place(x= -20, y= 50) #onde a imagem ira se localziar

        label_tt = ctk.CTkLabel(master=janela, text='Seja bem vindo(a) a\n POWER', font=('Roboto', 30), text_color='#FFD700').place(x=100, y=10)

        #frame
        login_frame= ctk.CTkFrame(master=janela, width=430, height=590) #fazer o fundo da direita do aplicativo
        login_frame.pack(side=RIGHT) #colocar do lado direito

        #frame widgets
        label = ctk.CTkLabel(master=login_frame, text='Sistema de Login', font = ('Roboto', 30, 'bold'), text_color= ('white')).place(x=100, y=100)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Nome de Usuario', width=300, font=('Roboto', 20)).place(x=75, y=205)
        username_label = ctk.CTkLabel(master=login_frame, text='^O campo de usuario e obrigatorio', text_color='#FFD700', font=('Roboto', 12)).place(x=75, y=235)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Senha do Usuario', width=300, font=('Roboto', 20), show='*').place(x=75, y=275)
        password_label = ctk.CTkLabel(master=login_frame, text='^O campo senha e obrigatorio', text_color='#FFD700', font=('Roboto', 12)).place(x=75, y=305)

        checkbox = ctk.CTkCheckBox(master=login_frame, text='Lembrar-se de mim').place(x=75, y=340)

        def login():
            msg = messagebox.showinfo(title='Estado de Login', message='Login feito com sucesso!')

        login_button = ctk.CTkButton(master=login_frame, text='LOGIN', width=300, fg_color='#FFD700', hover_color="yellow", text_color='black', command=login).place(x=75, y=390)

        def tela_register():
            #Remover o frame de login
            login_frame.pack_forget()

            #criando a tela de cadastro de usuarios
            rg_frame= ctk.CTkFrame(master=janela, width=430, height=590) #fazer o fundo da direita do aplicativo
            rg_frame.pack(side=RIGHT) #colocar do lado direito

            label = ctk.CTkLabel(master=rg_frame, text='Sistema de Registro', font = ('Roboto', 30, 'bold'), text_color= ('white')).place(x=80, y=100)

            spam = ctk.CTkLabel(master=rg_frame, text='Preencha todos os campos corretamente!', font=('Roboto', 17), text_color='gray').place(x=65, y=155)

            register_username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text='Nome de Usuario', width=300, font=('Roboto', 20)).place(x=75, y=205)
            register_email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text='Email de Usuario', width=300, font=('Roboto', 20)).place(x=75, y=255)
            register_password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text='Senha de Usuario', width=300, font=('Roboto', 20), show='*').place(x=75, y=305)
            register_cpassword_entry = ctk.CTkEntry(master=rg_frame, placeholder_text='Confirmar senha', width=300, font=('Roboto', 20), show='*').place(x=75, y=355)

            self.usuario_username = register_username_entry
            self.usuario_email = register_email_entry
            self.usuario_pass = register_password_entry
            self.usuario_cpass = register_cpassword_entry

            checkbox = ctk.CTkCheckBox(master=rg_frame, text='Aceito todos Termos e Politicas').place(x=75, y=405)


            def back():
                #Removendo o frame de cadastro
                rg_frame.pack_forget()

                #Deveolvendo o frame de login
                login_frame.pack(side=RIGHT)

            back_button = ctk.CTkButton(master=rg_frame, text='Voltar', width=140, fg_color='black', hover_color="#4F4F4F", text_color='white', command=back).place(x=75, y=450)

            def save_user():
                msg = messagebox.showinfo(title='Estado do Cadastro', message='Usuario cadastrado com sucesso!')

            save_button = ctk.CTkButton(master=rg_frame, text='Cadastrar', width=140, fg_color='#FFD700', hover_color="yellow", text_color='black', command=self.cadastrar_usuario).place(x=235, y=450)
        
        register_spam = ctk.CTkLabel(master=login_frame, text='Cadastre uma nova conta!').place(x=75, y=450)
        register_button = ctk.CTkButton(master=login_frame, text='Cadastre-se', width=130, fg_color='green', hover_color="#2D9334", command=tela_register).place(x=245, y=450)

        def limpa_entry_cadastro(self):
            self.username_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.cpassword_entry.delete(0, END)
        
        def limpa_entry_login(self):
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)

Application()