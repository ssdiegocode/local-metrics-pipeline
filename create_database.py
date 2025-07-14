import pandas as pd
import duckdb

df_viagens = pd.read_csv('files/dados_rjsmtr.csv')
df_datetime = pd.read_csv('files/datetime.csv')

con = duckdb.connect('db/dados_rjsmtr.duckdb')

con.execute("""
    CREATE TABLE IF NOT EXISTS viagens_rjsmtr AS SELECT * FROM df_viagens
""")

con.execute("""
    CREATE TABLE IF NOT EXISTS datahora AS SELECT * FROM df_datetime
""")

con.close()
