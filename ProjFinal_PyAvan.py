import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.set_page_config(page_icon="Oi", page_title="Análise Multiplos")



#### Parte da sidebar, e como está sendo feita
st.sidebar.image("./fgv_logo_menor.png", use_column_width=False)

st.sidebar.text('Aluno: Lucas da Costa')
st.sidebar.text('Projeto: Análise de Fundamentos')



#### PUXAR QUAIS SÃO OS TICKERS ATUAIS DA B3

t1 = pd.read_excel("./t1.xlsx", engine="openpyxl")






#### CRIANDO A BASE DEOS MULTIPLOS DOS TICKERS: ACHAR OS MÚLTIPLOS DOS TICKERS

# Por enquanto somente usar a base já baixada
fundamentos = pd.read_excel("./fundamentos.xlsx", engine="openpyxl")
#fundamentos = fundamentos.set_index('Papel')            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            




#### A PARTR DAQUI, O QUE ESTÁ SENDO FEITA NA PÁGINA PRINCIPAL


### Parte da sidebar com interação com a principal


var1 = st.sidebar.selectbox("Selecione a empresa para analisar:", 
                     t1.columns)


var2 = st.sidebar.selectbox("Selecione a variável para analisar:", 
                     fundamentos.columns)


#var3 = st.sidebar.selectbox("Selecione a variável para analisar:", 
 #                    fundamentos.columns)




### Parte principal


st.image( "./headimg.png", use_column_width=False)



st.markdown(
    """# **Comparativo de Fundamentos** 
O objetivo deste trabalho é, em tempo real, fazer um webscrappling na internet e achar os multiplos de várias empresas da bolsa. Neste caso, os dados foram dispostos em uma tabela abaixo, e, assim, os valores foram postos para análise.

Seguinto a caça aos dados, foram feitas as análises. Com duas opções à esquera, selecionadno a empresa disponível e o multiplo que se quer analisar, é possível encontrar um gráfico de pontos abaixo, o qual serviu para fazer uma analise exemplar e principal do trabalho acera, por exemplo, da máxima de 52 semanas da PETR4, em comparação com as outras empresas listas. Como visto, a PETR4 teve sua máxima acima da média das empresas. Este valor era esperado, dado que esta possui uma preço médio acima do preço médio da bolsa. 

Lembrando que, como a atualização é feita ao vivo, então os valores e resultados podem mudar com o tempo. 
""" )

st.header("**Dados usados**")


fundamentos

















### Análise dos multiplos


st.header("**Análise do Múltiplo**")


st.markdown(
    """# 
A medida que fora montada a tabela com os valores de referência acerca dos multiplos das ações, a anáise agora é acerca da comparativadade entre estas ações.
Acima foi traça da uma reta que apresenta a média dentre todas as empresas para aquela variável. Neste caso, o intuíto deste trabalho é justamente medir esta comparação.
Como exemplo, para a máxima de 52 semanas, a PETR4 este acima da média de cotação das outras empresas, semente tendo algumas poucas empresas que obtiveram uma média acima dela.
""" )



# Gráfico de pontos
fig, ax = plt.subplots(figsize=(12, 6))




## df para grafico
oi = list(fundamentos[f'{var2}'])
oi_s = [float(elemento) for elemento in oi]
a = oi_s

b = fundamentos['Papel']

c = {'Papel': b, f'{var2}': a}

# Criar o DataFrame a partir do dicionário
d = pd.DataFrame(c)

ax.set_title('Gráfico Scatterplot')
sns.scatterplot(data=d, x='Papel' , y=var2 , ax=ax)
plt.xlabel('Papel')
plt.ylabel(f'{var2}')
plt.xticks(rotation=45, ha='right')  # Girar os rótulos e alinhá-los à direita

# Obter os rótulos do eixo x
ticks = d['Papel'].tolist()
# Exibir apenas um quarto dos rótulos no eixo x
plt.xticks(range(0, len(ticks), len(ticks)//40), ticks[::len(ticks)//40])

values_y = d[f'{var2}'].tolist()
# Exibir apenas um quarto dos valores no eixo y
plt.yticks(range(0, len(values_y), len(values_y)//20), values_y[::len(values_y)//20])

# Encontrar o índice da linha que contém o valor de interesse em "Var2"
indice_interesse = d.index[d['Papel'] == var1].tolist()[0]

# Coordenadas do ponto de interesse
x_interesse = d.index.get_loc(indice_interesse)
y_interesse = d.iloc[[indice_interesse], 1]

# Adicionar a bola (destaque) ao redor do ponto de interesse
ax.add_patch(plt.Circle((x_interesse, y_interesse), radius=2, color='red', fill=True))
media_y = d[f'{var2}'].mean()
plt.axhline(y=media_y, color='red', linestyle='dashed', label='Média')



plt.tight_layout() 

st.pyplot(fig)















