from primeiropysus import *
import matplotlib.pyplot as plt
from pandas.plotting import table


plt.scatter(por_municipio_2019()["Município"], por_municipio_2019()["Quantidade"])
plt.savefig("plot_municipio.png")

ax = plt.subplot(111, frame_on=False) 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False) 
table(ax, por_municipio_2019().head(), loc='center') 
plt.savefig("tabela_municipio.png")


estado = plt.figure()
plt.bar(por_estado()["Estado"], por_estado()["Quantidade"])
plt.savefig("plot_estado.png")

ax = plt.subplot(111, frame_on=False) 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)
table(ax, por_estado().head(), loc='center') 
plt.savefig("tabela_estado.png")


mes = plt.figure()
plt.bar(por_mes()["Meses"], por_mes()["Quantidade"])
plt.savefig("plot_mes.png")

ax = plt.subplot(111, frame_on=False) 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)
table(ax, por_mes().head(12), loc='center') 
plt.savefig("tabela_mes.png")


por_faixa_etaria().plot()
plt.savefig("por_idade.png")

ax = plt.subplot(111, frame_on=False) 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)
table(ax, por_faixa_etaria().head(12), loc='center') 
plt.savefig("tabela_idade.png")


sexo = plt.figure()
plt.bar(por_sexo()["Sexo"], por_sexo()["Quantidade"])
plt.savefig("plot_sexo.png")

ax = plt.subplot(111, frame_on=False) 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)
table(ax, por_sexo().head(12), loc='center') 
plt.savefig("tabela_sexo.png")


cor = plt.figure()
plt.bar(por_cor()["Cor"], por_cor()["Quantidade"])
plt.savefig("plot_cor.png")

ax = plt.subplot(111, frame_on=False) 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)
table(ax, por_cor().head(12), loc='center') 
plt.savefig("tabela_cor.png")


