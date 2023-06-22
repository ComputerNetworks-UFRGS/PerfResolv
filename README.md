# Estrutura
__________________________________________________________________________________________________________________________________________________________________________________________

dados - Arquivos csv com dados coletados

mainpy- Todo o código-fonte para medir os tempos de resposta do DNS

graficos - Todo o código-fonte para gerar os graficos com o vega-Altair e lista de domínios

____________________________________________________________________________________________________________________________________________________________________________________________

# Dependências

Nosso código foi construído para rodar no Linux Ubuntu 22.04 LTS. Para construir a ferramenta de medição de tempo de resposta do DNS, primeiro Você também 
precisará instalar as seguintes dependências:

* dns.resolver
* time
* glob
* os
* pandas
* pip
* altair_viewer



_______________________________________________________________________________________________________________________________________________________________________________________________

# Instalação

Depois de instalar as dependências listadas acima, você  podera executar o scrip para as medições DNS:


Execute o seguinte script para iniciar a coleta

'''
python3 -m main.py
'''

____________________________________________________________________________________________________________________________________________________________________________________________________


#Executando uma medição


Este script executará carregamentos de página para cada site em Perfresolv-Medições DNS/list domains popular.txt
Esses carregamentos de página serão executados com o resolvedor da Cloudflare (1.1.1.1), resolvedor do Google (8.8.8.8), resolvedor do Quad9 (9.9.9.9), resolvedor do comodosecuredns (8.26.56.26), 
resolvedor do opendns(208.67.222.222).

Para cada resolvedor listado acima, os carregamentos de página serão executados com DNS tradicional ("Do53").

____________________________________________________________________________________________________________________________________________________________________________________________________

# Gráficos de exemplo

Temos alguns códigos de exemplo que são auto explicativos, para gerar plotagens para tempos de resposta DNS em Perfresolv-Medições DNS/Gráficos. O script '0-prepare_data.py' gerar automaticamente um conjunto de dados agregados para plotar os graficos. Primeiro, ele plotará csv para diferenças nos tempos de resposta entre cada protocolo DNS quando os resolvedores recursivos da Cloudflare, Google,Quad9,comodosecuredns e opendns se forem usados.

O script assume que seu arquivo de csv está localizado em Perfresolv-Medições DNS/data_agg_.csv. Ele também assume que você está medindo os sites listados list domains popular.txt. Se não for o caso, simplesmente modifique o script para apontar para os arquivos corretos.A lista de sites deve ter a forma de um nome de domínio por linha.

Nosso código que realmente gera os gráficos está localizado em arquivos diferentes. Descrevemos os arquivos abaixo:


Perfresolv-Medições DNS/Gráficos/1-chart_1_aggregated.py.  define funções comuns para fazer gráficos agregados dos arquivos csv.

Perfresolv-Medições DNS/Gráficos/5-chart_5_domain_type.py  define funções comuns para fazer gráficos. agregados dos nomes de domínios.



______________________________________________________________________________________________________________________________________________________________________________________________________

# Modificando nosso código

Se você deseja realizar medições com resolvedores diferentes, é necessário modificar Perfresolv-Medições DNS/main.py A classe "Resolvers" na parte superior do arquivo contém uma enumeração para nomes de resolvedores, endereços IP. Se você deseja adicionar novos resolvedores, basta adicionar novas entradas a esta classe.


































