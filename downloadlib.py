import wget 

def processa(lista):
    arquivos_lista = open(lista, "r")
    arquivos_lista_lines = arquivos_lista.readlines()
    arquivos_lista.close()

    for nomes in arquivos_lista_lines:
        url = str.rstrip(f'URLPARADOWNLOAD/{nomes}')
        print(f'{nomes}')
        wget.download(url)
        print('\n')
    print("Dowload Finalizado")



