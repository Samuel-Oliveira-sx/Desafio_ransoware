import os
import pyaes

## abrir o arquivo criptografado
nome_arquivo = "arquivo.txt.ransomwaretroll"
arquivo = open(nome_arquivo, "rb")
dados_arquivo = arquivo.read()
arquivo.close()

## chave para descriptografia
chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)
dados_descriptografar = aes.decrypt(dados_arquivos)

## remover o arquivo criptografado
os.remove(nome_arquivo)

## criar o arquivo descriptografado
novo_arquivo = "arquivo.txt"
novo_arquivo = open(f'{novo_arquivo}', "wb")
novo_arquivo.write(dados_descriptografar)
novo_arquivo.close()
