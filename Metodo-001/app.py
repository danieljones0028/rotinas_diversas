import configparser
from shutil import move

from lib.montagem import Montagem
# #############################################################################
config = configparser.ConfigParser()
config.read('bak.config')
# Autenticação
usuario = config['autenticacao']['usuario_mapeamento']
senha = config['autenticacao']['senha_usuario_mapeamento']
# Mapeamento
servidor = config['unidade.mapeamento']['servidor']
mapeamento = config['unidade.mapeamento']['mapeamento']
# Local
unidade_local = config['unidade.local']['unidade_local']
tipo = config['unidade.local']['tipo_backup']
# Remoto
unidade_remoto = config['unidade.remoto']['unidade_remoto']
# #############################################################################

def executa():
    if Montagem.montar(unidade_local, servidor, mapeamento, usuario, senha) == True:
        arquivos = Montagem.searquivos(unidade_local, tipo)
        if arquivos:
            try:
                # MOVE ARQUIVOS PARA O MAPEAMENTO COMEÇANDO PELO MENOR ARQUIVO.
                for arquivo in sorted(arquivos.items(), key=lambda item: item[1]):
                    print(f"Movendo {unidade_local}\\{tipo}\\{arquivo} para {unidade_remoto}\\{tipo}\\{arquivo}")
                    move(f"{unidade_local}\\{tipo}\\{arquivo}", f"{unidade_remoto}\\{tipo}\\{arquivo}")
            except Exception as erro_arquivos:
                print(erro_arquivos)

executa()