import duckdb
import argparse

parser = argparse.ArgumentParser(description='Executar consulta por número da questão')
parser.add_argument('questao', type=int, help='Número da questão (1 a 7)')
args = parser.parse_args()

con = duckdb.connect('db/dados_rjsmtr.duckdb')

def run_query(query):
    df = con.execute(query).fetchdf()
    print(df)

if args.questao == 1:
    query = """
    SELECT 
        d.data, 
        v.consorcio, 
        SUM(v.quantidade_passageiros) AS total_passageiros
    FROM viagens_rjsmtr v
        JOIN datahora d 
        ON v.transaction = d.Transaction_ID
    GROUP BY d.data, v.consorcio
    ORDER BY d.data, v.consorcio;
    """
    run_query(query)

elif args.questao == 2:
    query = """
    SELECT 
        STRFTIME(STRPTIME(d.data, '%d/%m/%Y'), '%w') AS dia_semana,
        d.hora,
        v.consorcio,
        SUM(v.quantidade_passageiros) AS total_passageiros
    FROM viagens_rjsmtr v
        JOIN datahora d 
        ON v.transaction = d.Transaction_ID
    WHERE d.data IS NOT NULL
    GROUP BY dia_semana, d.hora, v.consorcio
    ORDER BY total_passageiros DESC;
    """
    run_query(query)

elif args.questao == 3:
    query = """
    SELECT 
        STRFTIME(STRPTIME(d.data, '%d/%m/%Y'), '%Y') AS ano,
        v.consorcio,
        SUM(v.quantidade_passageiros) AS total_passageiros
    FROM viagens_rjsmtr v
        JOIN datahora d 
        ON v.transaction = d.Transaction_ID
    WHERE STRFTIME(STRPTIME(d.data, '%d/%m/%Y'), '%Y') = '2023'
    GROUP BY ano, v.consorcio
    ORDER BY total_passageiros DESC;
    """
    run_query(query)

elif args.questao == 4:
    query = """
    SELECT 
        STRFTIME(STRPTIME(d.data, '%d/%m/%Y'), '%Y') AS ano,
        v.descricao_servico,
        SUM(v.quantidade_passageiros) AS total_pagantes
    FROM viagens_rjsmtr v
        JOIN datahora d 
        ON v.transaction = d.Transaction_ID
    WHERE v.tipo_usuario = 'Pagante'
    GROUP BY ano, v.descricao_servico
    QUALIFY ROW_NUMBER() OVER (PARTITION BY ano ORDER BY SUM(v.quantidade_passageiros) DESC) = 1
    ORDER BY ano;
    """
    run_query(query)

elif args.questao == 5:
    query = """
    SELECT 
        STRPTIME(d.data, '%d/%m/%Y') AS data,
        SUM(v.quantidade_passageiros) AS total_passageiros
    FROM viagens_rjsmtr v
        JOIN datahora d 
        ON v.transaction = d.Transaction_ID
    WHERE v.meio_pagamento LIKE '%Riocard%'
    GROUP BY data
    QUALIFY ROW_NUMBER() OVER (ORDER BY SUM(v.quantidade_passageiros) DESC) = 1
    ORDER BY total_passageiros DESC;
    """
    run_query(query)

elif args.questao == 6:
    query = """
    SELECT 
        d.hora,
        SUM(v.quantidade_passageiros) AS total_passageiros
    FROM viagens_rjsmtr v
        JOIN datahora d 
        ON v.transaction = d.Transaction_ID
    WHERE d.hora IS NOT NULL
    GROUP BY d.hora
    ORDER BY total_passageiros DESC;
    """
    run_query(query)

elif args.questao == 7:
    query = """
    SELECT 
        STRFTIME(STRPTIME(d.data, '%d/%m/%Y'), '%Y') AS ano, 
        STRFTIME(STRPTIME(d.data, '%d/%m/%Y'), '%d') AS dia,
        SUM(v.quantidade_passageiros) AS quantidade_passageiros,
        SUM(SUM(v.quantidade_passageiros)) OVER (
            ORDER BY STRPTIME(d.data, '%d/%m/%Y')
        ) AS total_acumulado
    FROM viagens_rjsmtr v
        JOIN datahora d 
        ON v.transaction = d.Transaction_ID
    WHERE STRFTIME(STRPTIME(d.data, '%d/%m/%Y'), '%Y') = '2024'
    GROUP BY ano, dia, STRPTIME(d.data, '%d/%m/%Y')
    ORDER BY STRPTIME(d.data, '%d/%m/%Y');
    """
    run_query(query)

else:
    print("Questão inválida. Use um número de 1 a 7.")

con.close()
