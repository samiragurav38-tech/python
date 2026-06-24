import bcrypt
password =input("Enter your password:")
ADMIN_PASS="admin@123"

def encrypt_password(_pass):
    a = bcrypt.hashpw(_pass.encode(),bcrypt.gensalt())
    return a.decode()

def check_password(_pass,_bcrypt_password):
    return bcrypt.checkpw(_pass.encode(),_bcrypt_password.encode())

login = check_password(ADMIN_PASS,encrypt_password(password))
if login:
   print(f"login")
else:
    print("not")

