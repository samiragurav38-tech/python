import hashlib

password = input("enter your password:")
def password_encryption(password):
    return hashlib.sha256(password.encode()).hexdigest()

print(f"data type:{type(password)}")
print(f"Encrypted password:{password_encryption(password)}")
print(f"Encrypted password length:{len(password_encryption(password))}")
