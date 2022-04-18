from os import popen, path, listdir
from platform import platform
from hurry.filesize import size

class Montagem():

    def montar(ponto_de_montagem, servidor, mapeamento, usuario, senha):

        try:
            if platform() == 'Windows':
                # TENTA MONTAR O MAPEAMENTO # LEMBRAR DE MONTAR NA ESSAO QUE VAI SER EXECUTADO
                # TODO O COMANDO ABAIXO ESTA ERRADO
                monta = f"net use {ponto_de_montagem} \\{servidor}\{mapeamento} {usuario} {senha}"
                montando = popen(monta)
                if montando:
                    return True
            else:
                print(f"net use {ponto_de_montagem} \\{servidor}\{mapeamento} {usuario} {senha}")
                return False

        except Exception as erro_montar:
            print(erro_montar)
    
    def searquivos(ponto_de_montgem, tipo):
        # SE TIVEREM ARQUIVOS NO DISCO LOCAL, ONDE FOI FEITO O BACKUP
        # SERÁ CRIADO UM DICIONARIO COM NOME_DO_ARQUIVO[TAMANHO_DO_ARQUIVO]
        try:
            if platform() == 'Windows':
                if path.exists(f"{ponto_de_montgem}\\{tipo}"):
                    arquivos = listdir(f"{ponto_de_montgem}\\{tipo}")

                    try:
                        dicionario_arquivos = {}
                        for arquivo in arquivos:
                            tamanho = path.getsize(f"{ponto_de_montgem}\\{tipo}\\{arquivo}")
                            dicionario_arquivos[arquivo] = [tamanho]

                        return dicionario_arquivos

                    except Exception as erro_for:
                        print(erro_for)

        except Exception as erro_searquivos:
            print(erro_searquivos)