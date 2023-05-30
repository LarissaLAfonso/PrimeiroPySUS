import pandas as pd

hanseniase_2019 = pd.read_csv('Hanseniase-2019.csv', low_memory=False)

doencas = [hanseniase_2019]

for doenca in doencas:
    doenca["DT_NOTIFIC"] = pd.to_datetime(doenca["DT_NOTIFIC"]) 
    doenca.set_index("DT_NOTIFIC", inplace=True)
