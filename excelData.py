import pandas as pd

def readExcel(new_data):
        df = pd.read_excel('data.xlsx')
        df = df.append(new_data, ignore_index=True)

        df.to_excel(f'data.xlsx', index=False, index_label=False, header=False)
