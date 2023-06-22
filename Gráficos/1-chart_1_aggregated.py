#Imports

#Pandas é usado para criar um dataframe
import pandas as pd

#Imports padrão do Altair
from altair import pipe, limit_rows, to_values
import altair as alt
import altair_viewer



#Definições do Altair
t = lambda data: pipe(data, limit_rows(max_rows=50000000

), to_values)
alt.data_transformers.register('custom', t)
alt.data_transformers.enable('custom')
#alt.renderers.enable('altair_viewer')
#alt.renderers.enable('html')

#Lê o arquivo CSV
df = pd.read_csv('data_agg_brasil.csv')
# print(df)

#Cria as barras
bars = alt.Chart().mark_bar().encode(
    x=alt.X('Server:N', title='Server'),
    y=alt.Y('mean(Time):Q', title='Mean Response Time (ms)'),
    #Descomentar caso queira colorido e com legenda
    #https://vega.github.io/vega/docs/schemes/ to see color schemes
    color=alt.Color('Server', scale=alt.Scale(scheme='pastel1'))
)
#Cria as barras de erro
error_bars = alt.Chart().mark_errorbar(extent='stderr').encode(
    y=alt.Y('Time:Q', title='Mean Response Time (ms)'),
    x='Server:N'
)

#Junta o gráfico de barras com o de erro
chart = alt.layer(bars, error_bars, data=df).properties(
    width=600,
    height=250
)
print(chart)

#Mostra o gráfico
chart.save('chart_brasil.svg', embed_options={'renderer':'svg'}) # Nome do grafico
#chart.show()


#altair_viewer.show(chart)
