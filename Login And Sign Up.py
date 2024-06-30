from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

user_data = [("admin", "1234")]

def janela_login_signUp():
    Painel_Login.pack_forget()
    Painel_SingUp.pack(fill="both", expand=True)

def janela_signUp_login():
    Painel_SingUp.pack_forget()
    Painel_Login.pack(fill="both", expand=True)

def Login():
    email = Email_Entry.get().lower()
    senha = Senha_Entry.get().lower()

    if (email, senha) in user_data:
        Resultado_label.config(text="voce entrou")
    else:
        Resultado_label.config(text="Seu Email ou Senha Estao incorretos")

def Sign_Up():
    email_cad = Email_Entry2.get().lower()
    senha_cad = Senha_Entry2.get().lower()

    if any(email == email_cad for email, _ in user_data):
        Resultado_label2.config(text="Gmail ja cadastrado")
    else:
        user_data.append((email_cad, senha_cad))
        Resultado_label2.config(text="Gmail e Senha cadastrados")

Janela = ttk.Window("Login/Signup")
Janela.geometry('500x500+800+250')
Janela.title("Login/Signup")
style = Style(theme="superhero")

main_frame = ttk.Frame(Janela)
main_frame.pack(pady=10, padx=10, fill="both", expand=True)  

Painel_Login = ttk.Frame(main_frame)
Painel_Login.pack(pady=10, fill="both", expand=True)
ttk.Label(Painel_Login, text="Login", font=("arial", 18)).pack(padx=10, pady=10, fill="y")

Email = ttk.Frame(Painel_Login)
Email.pack(padx=10, pady=10, fill='x')
Email_label = ttk.Label(Email, text='Email:', font=("arial", 18)).pack(side=LEFT, padx=5)
Email_Entry = ttk.Entry(Email, font=("arial", 12))
Email_Entry.pack(side=LEFT, fill="x", expand=True, padx=5) 

Senha = ttk.Frame(Painel_Login)
Senha.pack(padx=10, pady=10, fill='x')
Senha_label = ttk.Label(Senha, text='Senha:', font=("arial", 18)).pack(side=LEFT, padx=5)
Senha_Entry = ttk.Entry(Senha, font=("arial", 12), show="*")
Senha_Entry.pack(side=LEFT, fill="x", expand=True, padx=5)

checkbt = ttk.Frame(Painel_Login)
checkbt.pack(pady=10, padx=10, fill="x")
ttk.Checkbutton(checkbt, text="Deseja Salvar Os Dados De Login ?", bootstyle="round-toggle").pack(side=LEFT, padx=10)

botao = ttk.Frame(Painel_Login)
botao.pack(padx=30, pady=10)
ttk.Button(botao, text="Entrar", bootstyle=SUCCESS, command=Login).pack(side=LEFT, padx=10)
ttk.Button(botao, text="Sign Up", bootstyle=PRIMARY, command=janela_login_signUp).pack(side=RIGHT, padx=10)

Resultado = ttk.Frame(Painel_Login)
Resultado.pack(pady=10, fill="x")
Resultado_label = ttk.Label(Resultado, text="aguardando resultados...", font=("Danger", 12))
Resultado_label.pack()

Painel_SingUp = ttk.Frame(main_frame)
Painel_SingUp.pack(pady=10, fill="both", expand=True)
ttk.Label(Painel_SingUp, text="Sign Up", font=("arial", 18)).pack(padx=10, pady=10, fill="y")

Email2 = ttk.Frame(Painel_SingUp)
Email2.pack(padx=10, pady=10, fill='x')
Email_label2 = ttk.Label(Email2, text='Email:', font=("arial", 18)).pack(side=LEFT, padx=5)
Email_Entry2 = ttk.Entry(Email2, font=("arial", 12))
Email_Entry2.pack(side=LEFT, fill="x", expand=True, padx=5)

Senha2 = ttk.Frame(Painel_SingUp)
Senha2.pack(padx=10, pady=10, fill='x')
Senha_label2 = ttk.Label(Senha2, text='Senha:', font=("arial", 18)).pack(side=LEFT, padx=5)
Senha_Entry2 = ttk.Entry(Senha2, font=("arial", 12), show="*")
Senha_Entry2.pack(side=LEFT, fill="x", expand=True, padx=5)

botao2 = ttk.Frame(Painel_SingUp)
botao2.pack(padx=30, pady=10)
ttk.Button(botao2, text="Cadastrar", bootstyle=SUCCESS, command=Sign_Up).pack(side=LEFT, padx=10)
ttk.Button(botao2, text="Login", bootstyle=PRIMARY, command=janela_signUp_login).pack(side=RIGHT, padx=10)

Resultado2 = ttk.Frame(Painel_SingUp)
Resultado2.pack(pady=10, fill="x")
Resultado_label2 = ttk.Label(Resultado2, text="aguardando resultados...", font=("Danger", 12))
Resultado_label2.pack()

Painel_SingUp.pack_forget()

Janela.mainloop()
