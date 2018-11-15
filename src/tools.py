#ththales
#Coleção de Funções acessórias
import os.path
import json


from pathlib import Path

def lerArquivoJSON(caminho_arquivo):
    """
    Retorna conteúdo de um arquivo JSON de comandos SQL, delegando tratamento para bloco de função reservado
    :param caminho_arquivo:
    :return: data (JSON)
    """
    with open(caminho_arquivo, "r") as read_file:
         data = json.load(read_file)
    if caminho_arquivo is not None:
        return data
    else:
        return None

    


def getFileAbsolutePath(rel_path):
    """
    Retorna o caminho absoluto de um arquivo a partir de seu caminho relativo no projeto
    :param rel_path:
    :return: absolute_path
    """
    data_folder = Path("PythoWebScraper/src")
    file_to_open = data_folder / rel_path

    return file_to_open