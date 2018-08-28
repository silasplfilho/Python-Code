import numpy as np
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
conn = psycopg2.connect(database="db_rais", user="i3geoconsulta", password="i3geoconsulta", host="10.3.40.10", port="5432")
cur = conn.cursor()
#------
query= """
    SELECT s.ano AS serie_temporal, s.cod_cargo AS cod_cargo, s.cargo AS cargo,s.subfaixa AS subfaixa, s.remun AS variavel_remuneracao,
    ( s.ano::INTEGER )-( s.ano_ing_spub::INTEGER ) AS anos_servico
    FROM public.tb_siape_v02 AS s
    WHERE s.ano=2016 AND s.cod_cargo='422069' AND s.ano_ing_spub NOT IN ( 's/info' ) limit 200;
    """

query2 = """
    select (2018 - cast(s.ano_ing_spub as numeric)) as experiencia, v.rem_med_r, s.subfaixa, s.remun, s.faixa_remun
    from tb_siape_v02 as s join tb_vinculos_2016 as v
    on s.cpf_servidor = v.cpf
    where s.ano = 2016 and s.ano_ing_spub != 's/info'
    and v.cbo2002 in (10105, 10110, 10115, 10215, 10210, 10205, 10310, 10315, 10305,
    20115, 20105, 20110, 20205, 20305, 20310, 21105, 21110, 21205, 21210, 30115, 30105,
    30110, 30205, 30305, 31105, 31110, 31210, 31205)
    limit 200
"""

query3 = """
    SELECT s.ano AS serie_temporal, s.cod_cargo AS cod_cargo, s.cargo AS cargo,s.subfaixa AS subfaixa, s.remun AS variavel_remuneracao, s.orgao_superior AS ministerios,
    (s.ano::INTEGER )-( s.ano_ing_spub::INTEGER ) AS anos_servico
    FROM public.tb_siape_v02 AS s
    WHERE s.ano=2016 AND s.cod_cargo='422069' AND s.ano_ing_spub NOT IN ('s/info')
    AND s.orgao_superior LIKE 'm%' AND s.uf_da_organizacao='rj' AND s.situacao_funcional='est-01'
    ;
    """

cur.execute(query3)
data = pd.DataFrame(cur.fetchall(), columns=['serie_temporal', 'cod_cargo', 'cargo', 'subfaixa', 'variavel_remuneracao', 'ministerio', 'ano_servico'])
data = pd.DataFrame(cur.fetchall(), columns=['experiencia', 'rem_med_r', 'situacao_funcional'])
cur.close()
conn.close()
#----
path = r"C:\\Users\\b247857261\\Desktop\\Scripts\\silas\\Python-Codes\\Machine Learning A-Z Template Folder\\Part 2 - Regression\\Section 5 - Multiple Linear Regression\\data.csv"
data.to_csv(path, sep=",")
#------
data = pd.read_csv(r"C:\\Users\\b247857261\\Desktop\\Scripts\\silas\\Python-Codes\\Machine Learning A-Z Template Folder\\Part 2 - Regression\\Section 5 - Multiple Linear Regression\\data.csv",
    index_col=0) # index_col = 0 retira o indice que vem na leitura do CSV
dataset = data.iloc[0:3000, :]
#----- Criando os vetores de variaveis dependentes e independentes
X = pd.DataFrame(dataset.iloc[:, 6].values)
y = dataset.iloc[:, 3].values

# dividindo o dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 1/3, random_state = 0)

#---Fitting simple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting
y_pred = regressor.predict(X_test)

# Visualização do Train Set
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of experience')
plt.ylabel('Faixa Salarial')
plt.show()

# Visualização do Test Set
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

regressor.score(X_train, y_train)
regressor.score(X_test, y_test)
