import camelot
import pandas as pd
import time
import datetime

START_PAGE = 25
END_PAGE = 26
df = pd.DataFrame()

startProcess = datetime.datetime.now()
print(f"{startProcess} - Started reading PDF...")
for page in range(START_PAGE, END_PAGE + 1):
    print(f"{datetime.datetime.now()} - Started reading page {page}...")
    tables = camelot.read_pdf("Catalogo_de_Servicos_do_SFN_Volume_IV_Versao_501.pdf", pages=str(page))
    if len(tables) > 0:
        df = tables[0].df
        if page != START_PAGE:
            df = df.drop(0)
        df.to_csv('foo.csv',mode='a',header=False,index=False)
end = datetime.datetime.now()
print(f"{end} - Ended reading PDF")

endProcess = datetime.datetime.now()
print(f"{endProcess} - Total time elapsed: {(endProcess - startProcess).total_seconds()} seconds.")