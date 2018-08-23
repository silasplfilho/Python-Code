import numpy as np
import pandas as pd
import psycopg2

conn = psycopg2.connect(database="db_rais", user="i3geoconsulta", password="i3geoconsulta", host="10.3.40.10", port="5432")
cur = conn.cursor()
#------
query= """select (2018 - cast(s.ano_ing_spub as numeric)) as experiencia, v.rem_med_r, s.situacao_funcional
    from tb_siape_v02 as s join tb_vinculos_2016 as v
    on s.cpf_servidor = v.cpf
    where s.ano = 2016 and s.ano_ing_spub != 's/info'
    limit 200"""

cur.execute(query)
data = pd.DataFrame(cur.fetchall(), columns=['experiencia', 'rem_med_r', 'situacao_funcional'])
cur.close()
conn.close()
#----
path = r"C:\\Users\\b247857261\\Desktop\\Scripts\\silas\\Python-Codes\\Machine Learning A-Z Template Folder\\Part 2 - Regression\\Section 5 - Multiple Linear Regression\\data.csv"
data.to_csv(path, sep=",")
