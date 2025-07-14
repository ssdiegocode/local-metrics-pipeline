import os
import subprocess

if not any(file.endswith('.duckdb') for file in os.listdir('db')):
    subprocess.run(['python', 'create_database.py'])

while True:
    questao = input('Digite o número da questão (1-8), ou "sair" para encerrar: ')
    if questao.lower() == 'sair':
        break
    if questao in [str(i) for i in range(1, 8)]:
        subprocess.run(['python', 'run_query.py', questao])
    elif questao == '8':
        subprocess.run(['python', 'run_beam.py'])
    else:
        print('Entrada inválida. Digite um número entre 1 e 8 ou "sair".')
