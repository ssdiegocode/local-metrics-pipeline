import duckdb
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

con = duckdb.connect('db/dados_rjsmtr.duckdb')
df = con.execute("""
    SELECT meio_pagamento, quantidade_passageiros
    FROM viagens_rjsmtr
""").fetchdf()
con.close()

def categorize(row):
    meio = row['meio_pagamento'].lower().strip()
    qtd = row['quantidade_passageiros']
    if 'qr' in meio:
        categoria = 'QRCode'
    elif 'cart' in meio:
        categoria = 'Cartao'
    elif 'riocard' in meio:
        categoria = 'Riocard'
    else:
        categoria = 'Outros'
    return (categoria, qtd)

def run():
    pipeline_options = PipelineOptions()
    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | 'Create Input' >> beam.Create(df.to_dict(orient='records'))
            | 'Categorize' >> beam.Map(categorize)
            | 'Sum Per Category' >> beam.CombinePerKey(sum)
            | 'Print Results' >> beam.Map(print)
        )

if __name__ == '__main__':
    run()
