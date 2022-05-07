import pandas as pd
import os.path

def createExcel():
        if not os.path.isfile('data.xlsx'):
                writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
                writer.save()


def readExcel(df):
        createExcel()

        df_excel = pd.read_excel('data.xlsx')
        result = pd.concat([df_excel, df], ignore_index=True)

        result.to_excel(f'data.xlsx', sheet_name='Sheet1',index=False, index_label=False)
