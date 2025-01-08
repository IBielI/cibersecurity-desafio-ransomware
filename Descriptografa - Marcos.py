import os
import pyaes

def descriptografar_arquivos(diretorio, chave):
    
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".ransomwaretroll"):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            
            with open(caminho_arquivo, "rb") as file:
                file_data = file.read()
            
            os.remove(caminho_arquivo)

            aes = pyaes.AESModeOfOperationCTR(chave)
            
            decrypted_data = aes.decrypt(file_data)
            
            novo_nome = caminho_arquivo.replace(".ransomwaretroll", "")
            with open(novo_nome, "wb") as new_file:
                new_file.write(decrypted_data)
                
diretorio = r"C:\LocalImportante"

chave = b"testeransomwares"

descriptografar_arquivos(diretorio, chave)

