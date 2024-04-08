import bcrypt
password = b"A super complicated password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)