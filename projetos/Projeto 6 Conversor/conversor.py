
def lê_binario():
    try:
        with open('Projeto 6 Conversor/audio_TOP_SECRET.txt', 'rb') as arquivo:
            dados = arquivo.read()
            print(type(dados))
        with open('audio_TOP_SECRET.mp3', 'wb') as arquivo2 :
            arquivo2.write(dados)
    except FileNotFoundError as e:
        print("ARQUIVO NÂO ENCONTRADO", e)
        arquivo = open('audio_TOP_SECRET.txt', 'wb')
        arquivo.close()
    except IOError as e:
        print("DEU ERRADO")
    print("OK")

lê_binario()