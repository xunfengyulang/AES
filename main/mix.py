import encrypt
import decrypt

def mix(textpath,keypath,encryptpath,decryptpath):
    encrypt.encrypt(textpath,keypath,encryptpath)
    decrypt.decrypt(encryptpath,keypath,decryptpath)

if __name__ == '__main__':
    textpath = '../Utils/encrypt_test.txt'
    keypath = '../Utils/key.txt'
    encryptpath = './mix_encrypt.txt'
    decryptpath = './mix_decrypt.txt'
    mix(textpath,keypath,encryptpath,decryptpath)