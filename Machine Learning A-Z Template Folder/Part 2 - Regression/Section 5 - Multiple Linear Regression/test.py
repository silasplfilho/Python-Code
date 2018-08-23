import numpy as np
import pandas as pd
import psycopg2

conn = psycopg2.connect(database="db_rais", user="i3geoconsulta", password="i3geoconsulta", host="10.3.40.10", port="5432")
cur = conn.cursor()
#------
query="""
    (select v.cbo2002, v.rem_med_r, v.grau_instr
        from tb_vinculos_2016 as v
        where ceiling(v.cbo2002/100) = (1113)
        limit 100)
"""
select (2018 - cast(s.ano_ing_spub as integer)) as experiencia, v.rem_med_r, s.situacao_funcional
    from tb_siape_v02 as s
        join tb_vinculos_2016 as v
        on s.cpf_servidor = v.cpf
    where s.ano = 2017 and (v.cbo2002/100) = 1113
    limit 2

select * from tb_siape_v02 limit 2
