import os
from datetime import datetime
import pandas as pd

def save_dataframe(df: pd.DataFrame, questao_numero: int):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{questao_numero}_{timestamp}.txt'
    storage_path = os.path.join('storage', filename)

    os.makedirs('storage', exist_ok=True)
    
    df.to_csv(storage_path, index=False, sep=',')
    print(f'Arquivo salvo em: {storage_path}')
