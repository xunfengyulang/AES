import pandas as pd
import re
import os

S_path='../De/S.csv'
IS_path='../De/IS.csv'
Rcon_path='../De/Rcon.csv'

def decrypt(text,keypath):
    pro_key=[]
    S=S_get(S_path)
    IS=S_get(IS_path)
    if not os.path.exists(keypath):
        assert False,"please put the key in %s" %keypath
    with open(keypath,'rb') as f:
        key=f.read()
        if len(key)!=16:
            assert False,"the length of key must be 16 bytes"
        for i in range(4):
            pro_key.append(key[i*4:i*4+4])
        for i in range(4,44):
            if i%4==0:
                prokey=bytes(a^b for a,b in zip(pro_key[i-4],T(pro_key[i-1],int(i/4-1),S)))
            else:
                prokey=bytes(a^b for a,b in zip(pro_key[i-4],pro_key[i-1]))
            pro_key.append(prokey)
    text=bytes(a^b for a,b in zip(text,b''.join(pro_key[40:44])))
    for i in range(9,-1,-1):
        r0 = text[0::4]
        r1 = text[1::4]
        r2 = text[2::4]
        r3 = text[3::4]
        r1 = r1[3:] + r1[:3]
        r2 = r2[2:] + r2[:2]
        r3 = r3[1:] + r3[:1]
        text1 = bytes([r0[0], r1[0], r2[0], r3[0], r0[1], r1[1], r2[1], r3[1], r0[2], r1[2], r2[2], r3[2], r0[3], r1[3], r2[3],r3[3]])
        text2=b''
        for b in text1:
            prokey2=IS[b>>4][b&0x0F]
            text2+=prokey2
        text3=bytes(a^b for a,b in zip(text2,b''.join(pro_key[i*4:i*4+4])))
        if i!=0:
            text4 = b''
            for c in range(4):
                a0,a1,a2,a3=text3[c*4],text3[c*4+1],text3[c*4+2],text3[c*4+3]
                b0 = (x14(a0) ^ x11(a1) ^ x13(a2) ^ x9(a3)) & 0xff
                b1 = (x9(a0) ^ x14(a1) ^ x11(a2) ^ x13(a3)) & 0xff
                b2 = (x13(a0) ^ x9(a1) ^ x14(a2) ^ x11(a3)) & 0xff
                b3 = (x11(a0) ^ x13(a1) ^ x9(a2) ^ x14(a3)) & 0xff
                text4 += bytes([b0, b1, b2, b3])
            text=text4
        else:
            text=text3
    return text

def T(key,round_index,S):
    Rcon=Rcon_get(Rcon_path)
    key1=key[1:]+key[:1]
    key2=b''
    for b in key1:
        prokey2=S[b>>4][b&0x0F]
        key2+=prokey2
    key3=bytes(a^b for a,b in zip(key2,Rcon[round_index]))
    return key3

def S_get(path):
    S=[]
    data=pd.read_csv(path,header=None,dtype=str)
    data=data.iloc[1:, 1:].values.tolist()
    for r in data:
        row=[]
        for item in r:
            item_processed = re.sub(r'[^0-9A-F]', '', item)
            item_final = bytes.fromhex(item_processed)
            row.append(item_final)
        S.append(row)
    return S

def Rcon_get(path):
    Rcon=[]
    data=pd.read_csv(path,header=None,dtype=str)
    data=data.iloc[1:,1:].values.tolist()
    for r in data:
        row=b''
        for item in r:
            item_processed = re.sub(r'[^0-9A-F]', '', str(item))
            item_final = bytes.fromhex(item_processed)
            row+=item_final
        Rcon.append(row)
    return Rcon

def x2(x):
    if x&0x80:
        return ((x<<1)^0x1b)& 0xff
    else:
        return (x<<1)& 0xff

def x9(x):
    return (x2(x2(x2(x)))^x)& 0xff

def x11(x):
    return (x2(x2(x2(x)))^x2(x)^x)& 0xff

def x13(x):
    return (x2(x2(x2(x)))^x2(x2(x))^x)& 0xff

def x14(x):
    return (x2(x2(x2(x)))^x2(x2(x))^x2(x))& 0xff