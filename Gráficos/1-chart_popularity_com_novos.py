#Imports
import pandas as pd
from altair import pipe, limit_rows, to_values
import altair as alt

#Definições do Altair
t = lambda data: pipe(data, limit_rows(max_rows=50000000), to_values)
alt.data_transformers.register('custom', t)
alt.data_transformers.enable('custom')

alt.renderers.enable('altair_viewer')

#Mudar o nome do País para o que deseja plotar
df = pd.read_csv('com-novos_Australia.csv')
print(df)

#Cria as barras
bars = alt.Chart().mark_bar().encode(
    x=alt.X('Resolvedor:N', title='Resolvedor'),
    y=alt.Y('mean(Tempo):Q', title='Tempo de resposta (ms)'),
    #Descomentar caso queira colorido e com legenda
    color=alt.Color('Resolvedor', scale=alt.Scale(scheme='greys'))
)

#Cria as barras de erro
error_bars = alt.Chart().mark_errorbar(extent='stderr').encode(
    y=alt.Y('mean(Tempo):Q', title='Tempo de resposta (ms)'),
    x=alt.X('Resolvedor:N', title='Resolvedor'),
)

#Junta o gráfico de barras com o de erro
chart = alt.layer(bars, error_bars, data=df).properties(
    width=120,
    height=250
).facet(
    column=alt.Row('Tipo de Domínio:N', sort=['Popular', 'Médio', 'Novo']), 
)

#Mostra o gráfico
chart.show()


        