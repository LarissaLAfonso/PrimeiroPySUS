from pysus.onlinedata import SINAN

df = parquets_to_dataframe(SINAN.download("Hanseniase", 2019))
df.to_csv("Hanseniase-2019.csv")
