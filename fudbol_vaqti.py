from random import randint as ri

salt = ri(1, 1)
f = open("baza.txt", "w")
username = "maktab"
password = "maktab4"
f.write(username + '\n' + str(hash(password) + salt))
f.close()

print("Ismingizni kiriting: ")
username = input("Login: ")
password = input("password: ")

f = open("baza.txt", 'r')
Login = username in f.readline()
parol = str(hash(password)) in f.readline()

if Login and password:
    print("tizimga kirdingiz")
else:
    print("login yoki parol xato")
