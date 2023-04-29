

import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook

def write(item:str, date:str, color:str, location:str, note:str):
    df =pd.DataFrame({'Item':[item], 'Date':[date], 'Color':[color], 
                      'Location':[location], 'Note':[note]})
    wb = load_workbook(filename='Lost_and_Found.xlsx')
    ws = wb['Sheet1'] 
    for r in dataframe_to_rows(df, index=False, header=False):
        ws.append(r)
    wb.save('Lost_and_Found.xlsx')
    wb.close()
    # with pd.ExcelWriter('Lost_and_Found.xlsx', mode='a', engine='openpyxl') as writer:
    #     df.to_excel(writer,sheet_name='Sheet1')
    
    
def find(item:str, color:str):
    with open(r'Lost_and_Found.xlsx', 'rb') as f:
        df = pd.read_excel(f)
        res= df.loc[(df['Item'] == item) & (df['Color'] == color) & 
                (pd.isna(df['Check'])), ['Item', 'Date', 'Color', 'Location', 'Note', 'Check']]
        return res
    
    


