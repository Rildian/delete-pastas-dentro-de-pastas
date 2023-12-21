import os

def validacao(path):
    return os.path.exists(path)

def apagadorDeArquivos(path):
    lista = os.listdir(path) # pegar tudo dessa pasta e botar numa lista
    if len(lista) == 0:
        print("Nenhum arquivo encontrado, a pasta será apagada.\n")
        apagadorDePasta(path)
    else:
        for item in lista:
            arquivo = os.path.join(path, item)
            if os.path.isdir(arquivo): # é diretorio? Então vamos apagar essa pasta
                apagadorDePasta(arquivo)
            else: # vou assumir q ou é dir ou é txt
                    os.remove(arquivo) # como é txt, ent delete

def apagadorDePasta(path):
    lista = os.listdir(path)
    if len(lista) != 0:
        apagadorDeArquivos(path)
    else:
        print("Pasta deletada.\n")
        os.rmdir(path)

def main():
    path = "C:\\Users\\TGRM\\Documents\\material de estudo\\Teste"

    if validacao(path):
        apagadorDeArquivos(path)
        apagadorDePasta(path)
        if not validacao(path):
            print("Pasta foi deletada com sucesso")
    else:
        print("Pasta não encontrada.\n")
main()
