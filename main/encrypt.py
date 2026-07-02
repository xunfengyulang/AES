from En import en
import os

def encrypt(textpath,keypath,outputpath):
    if not os.path.exists(textpath):
        assert False,"please put the file in %s" %textpath
    pro_test = b''
    with open (textpath,"rb") as f:
        text=f.read()
        if len(text)%16!=0:
            text=text+(b"\x00"*(16-len(text)%16))
        for i in range(int(len(text)/16)):
            pro_test+=en.encrypt(text[i*16:i*16+16],keypath)
    with open(outputpath,"wb") as f:
        f.write(pro_test)

if __name__ == '__main__':
    keypath='../Utils/key.txt'
    textpath='../Utils/encrypt_test.txt'
    outputpath='./encrypted.txt'
    encrypt(textpath,keypath,outputpath)