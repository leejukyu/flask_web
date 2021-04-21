from passlib.hash import sha256_crypt
password  = sha256_crypt.encrypt("password") # 패스워드 등록
print(password)

print(sha256_crypt.verify("password", password)) # 앞에꺼랑 맞는지 검증