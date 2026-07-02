# 环境安装
`pip install pandas`
# 项目结构
```
AES
├── README.md
├── De
│   ├── de.py
│   └── IS.csv
|   └── Rcon.csv
|   └── S.csv
├── En
│   ├── en.py
│   ├── Rcon.csv
│   └── S.csv
├── main.py
|   └── decrypt.py
|   └── encrypt.py
|   └── mix.py
└── Utils
    └── key.txt
```
# 项目说明
执行加密：运行encrypt.py  
执行解密：运行decrypt.py  
执行加解密：运行mix.py
# 参数修改
在key.txt中修改密钥。  
在encrypt.py中修改输入文件路径、输出文件路径、密钥路径。  
在decrypt.py中修改输入文件路径、输出文件路径、密钥路径。  
在mix.py中修改输入文件路径、输出加密文件路径、输出解密文件路径、密钥路径。
# 常见报错
`the length of key must be 16 bytes`  
密钥长度必须是16字节。  
`please put the key/file in %s`  
文件路径错误。
# 使用说明
### encrypt.py
把待加密文件命名为encrypt_test.txt并放在Utils目录下，运行encrypt.py，加密后的文件在main目录下，文件名为encrypted.txt  
### decrypt.py
把待解密文件命名为decrypt_test.txt并放在Utils目录下，运行decrypt.py，解密后的文件在main目录下，文件名为decrypted.txt  
### mix.py
把待加密文件命名为encrypt_test.txt并放在Utils目录下，运行mix.py，加密后的文件在main目录下，文件名为mix_encrypted.txt，解密后的文件在main目录下，文件名为mix_decrypted.txt  
# 常见问题
### 加密后的文件解密得到的结果和原文件不一致
待解密文件需要直接复制已经加密好的文件，不能将加密好的文件中的内容复制粘贴到待解密文件中。
### 生成的解密文件末尾有NULL字符
这是由于AES是分组加密算法，每组16字节，长度不足会导致末尾补0。若有需要可以在encrypt.py和decrypt.py中进行如下的代码修改。  
  
原代码：
```
            text=text+(b"\x00"*(16-len(text)%16))
```
修改后的代码：
```
            text=text+(b" "*(16-len(text)%16))
```