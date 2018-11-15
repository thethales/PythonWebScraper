#lib import
import data_controller
import tools

import urllib.request
import datetime
from bs4 import BeautifulSoup


#scope definition
page_url = "https://www.sciencedaily.com/releases/2018/11/181114132000.htm"
site_name= "ScienceDaily"
grab_date = datetime.datetime.now()

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
page_content = opener.open(page_url).read()
page_content_soup = BeautifulSoup(page_content,'html.parser')
#----------------------------------------------------------------


##Page
page_summary = page_content_soup.find_all('dd')
page_date = page_summary[0]
page_source = page_summary[1]
page_abstract = page_summary[2]
page_article = ''


##DB SITE
db_novo_site = (site_name,grab_date)
db_nova_pagina = (1,page_url,str(page_content_soup),str(page_abstract),page_article)

db_connection = data_controller.initialize_database()
#new_row = data_controller.inserir_site(db_connection, db_novo_site)
data_controller.inserir_webpage(db_connection,db_nova_pagina)
db_connection.commit()

