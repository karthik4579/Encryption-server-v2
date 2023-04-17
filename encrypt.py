from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

def ncrypt(a):
    encMessage = fernet.encrypt(a.encode())
    encMessage_as_str = encMessage.decode()  # .decode() converts it to a normal string which is being returned
    return encMessage_as_str