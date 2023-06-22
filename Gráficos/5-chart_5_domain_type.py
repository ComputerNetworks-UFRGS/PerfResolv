#Imports
import pandas as pd
from altair import pipe, limit_rows, to_values
import altair as alt

#Definições do Altair
t = lambda data: pipe(data, limit_rows(max_rows=500000), to_values)
alt.data_transformers.register('custom', t)
alt.data_transformers.enable('custom')

#alt.renderers.enable('altair_viewer')

#Lê o arquivo CSV
df = pd.read_csv('data_agg_brasil.csv')
print(df)

#Cria as barras
bars = alt.Chart().mark_bar().encode(
    x=alt.X('Type of Domain:N', sort=['Popular', 'New', 'Medium'], title='Type of Domain'),
    y=alt.Y('mean(Time):Q', title='Mean Response Time (ms)'),
    #Descomentar caso queira colorido e com legenda
    color=alt.Color('Type of Domain'),
)
    
#Cria as barras de erro
error_bars = alt.Chart().mark_errorbar(extent='stderr').encode(
    y=alt.Y('mean(Time):Q', title='Mean Response Time (ms)'),
    x=alt.X('Type of Domain:N', sort=['Popular', 'New', 'Medium'], title='Type of Domain'),
)


#Junta o gráfico de barras com o de erro
chart = alt.layer(bars, error_bars, data=df).properties(
    width=120,
    height=250
).facet(
    column='Server:N'
)

#Mostra o gráfico
chart.save('chart-tipo-brasil.svg', embed_options={'renderer':'svg'})



        
