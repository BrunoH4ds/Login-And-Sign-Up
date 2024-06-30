user_data = [("admin", "1234")]

email_cad = input("digite o gmail:").lower()
senha_cad = input("digite a senha:").lower()
  
if any(email == email_cad for email, _ in user_data):
  print("gmail ja cadastrado")

else:
  user_data.append((email_cad, senha_cad))
  print("gmail e senha cadastrados")
