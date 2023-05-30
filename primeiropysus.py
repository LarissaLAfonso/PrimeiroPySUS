import Hanseniase as hans
import pandas as pd 


def qtd_total_2019():
    return hans.hanseniase_2019.shape[0]
  

def por_municipio_2019():
    contagem_municipio = hans.hanseniase_2019["ID_MUNICIP"].value_counts()
    df_contagem_municipio = contagem_municipio.to_frame().reset_index()
    df_contagem_municipio.columns = ["Municipio", "Quantidade"]
    df_contagem_municipio.sort_values("Municipio", inplace = True)
    df_contagem_municipio = pd.DataFrame(data=df_contagem_municipio)


    #por_municipio = hans.hanseniase_2019.groupby("ID_MUNICIP")
    #counts = por_municipio.size()
    #counts = pd.DataFrame(data=counts)

    return df_contagem_municipio


def por_estado():
    contagem_estado = hans.hanseniase_2019["SG_UF_NOT"].value_counts()
    df_contagem_estado = contagem_estado.to_frame().reset_index()
    df_contagem_estado.columns = ["Estado", "Quantidade"]
    df_contagem_estado.sort_values("Estado", inplace = True)
    df_contagem_estado = pd.DataFrame(data=df_contagem_estado)

    return df_contagem_estado
  
    
def por_mes():
    mes = hans.hanseniase_2019.resample("M").size()
    df_contagem_mes = mes.to_frame().reset_index()
    df_contagem_mes.columns = ["Meses", "Quantidade"]
    df_contagem_mes.sort_values("Meses", inplace = True)
    df_contagem_mes = pd.DataFrame(data=df_contagem_mes)

    return df_contagem_mes


def por_faixa_etaria():
    hans.hanseniase_2019['NU_IDADE_N'] = hans.hanseniase_2019['NU_IDADE_N'].astype(str).str[-3:]
    contagem_idades = hans.hanseniase_2019['NU_IDADE_N'].value_counts()
    df_contagem_idades = contagem_idades.to_frame().reset_index()
    df_contagem_idades.columns = ['Idade', 'Quantidade']
    df_contagem_idades.sort_values("Idade", inplace = True)
    df_contagem_idades = pd.DataFrame(data=df_contagem_idades)

    return df_contagem_idades
  

def por_sexo():
    contagem_sexo = hans.hanseniase_2019['CS_SEXO'].value_counts()
    df_contagem_sexo = contagem_sexo.to_frame().reset_index()
    df_contagem_sexo.columns = ['Sexo', 'Quantidade']
    df_contagem_sexo = pd.DataFrame(data=df_contagem_sexo)
    
    return df_contagem_sexo
  

def por_cor():
    racas = hans.hanseniase_2019.groupby("CS_RACA")

    contagem_cor = hans.hanseniase_2019['CS_RACA'].value_counts()
    df_contagem_cor = contagem_cor.to_frame().reset_index()
    df_contagem_cor.columns = ['Cor', 'Quantidade']
    
    df_contagem_cor = pd.DataFrame(data = df_contagem_cor)

    print(df_contagem_cor.columns)
    print(df_contagem_cor['Quantidade'].shape)
    
    return df_contagem_cor  
