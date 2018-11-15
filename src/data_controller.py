import tools

import sqlite3
from sqlite3 import Error
 

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def initialize_database():
    """Inicializa o banco de dados"""
    db_file = 'd:\\GitHub\\PythonWebScraper\\database\\webdata.db'
    #Problemas com caminho relativo, ajustar later
    sql_statments_srcfile = 'd:\\GitHub\\PythonWebScraper\\src\\database_def\\tables.json' #tools.lerArquivo('\\src\\database_def\\tables.sql')
    sql_statments = tools.lerArquivoJSON(sql_statments_srcfile)
    if sql_statments is not None:
        conn = create_connection(db_file)
        if conn is not None:
            for i in range (0,len(sql_statments["CREATE_TABLE"])):
                create_table(conn, sql_statments["CREATE_TABLE"][i])
        else:
            print("Erro, não foi possível criar conexão com o banco de dados")
    else:
        print("Erro, não foi possível obter a estrutura de inicialização do banco de dados")
    return conn

def inserir_site(conn, site):
    """
    Inserir um novo site na tabela apropridada
    :param site (name[string],data_inclusao[date]):
    :return (ID do novo registro):
    """
 
    sql = ''' INSERT INTO web_site(name,data_inclusao) 
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, site)
    return cur.lastrowid

def inserir_webpage(conn, page):
    """
    Inserir um nova pagina web na tabela apropridada
    :param page (address[string],raw_content[string],article_summary[string],article_content[string]):
    :return (ID do novo registro):
    """
 
    sql = ''' INSERT INTO web_page(id_web_site,address,raw_content,article_summary,article_content) 
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, page)
    return cur.lastrowid