email=input("insira o gmail: ").lower()
senha= (input("insira a senha: "))

email_lib= ["admin"]
email_lib="".join(email_lib)

senha_lib= ["1234"]
senha_lib="".join(senha_lib)

if email == email_lib and senha == senha_lib:
  print("voce entrou")
elif email != email_lib and senha != senha_lib:
 print("Seu Email ou Senha Estao incorretos")
else:
  print("nao encontramos seu login por favor cadastresse")
