#Imports

#Glob é uma lib para pegar arquivos e pastas
from glob import glob

#CSV é uma lib para ler e escrever arquivos CSV
from csv import writer


#Listas com os domínios de cada tipo
#Popular
popular = ['google.com','youtube.com','facebook.com','a-msedge.net','microsoft.com','netflix.com',
             'epicgames.com','akamaiedge.net','gtld-servers.net' ,'twitter.com','instagram.com','baidu.com',
             'amazonaws.com','apple.com','linkedin.com','cloudflare.com','wikipedia.org','yahoo.com','qq.com','akamai.net']

#Médio
medium = ['tabsite.com','yuukagetsu.com','kafene.com','yuzu-tosou.com','lotzadollars.com','ywproperty.com',
               'yxbabe.com','gtd4xzbo4mycmst.com','joyfulhour.net','bentoncollections.com',
               'yyfxgzs.com','bonpost.ru','notary.net','yywater.tw','shopiro.ca','facetfiez.space','yztown.vip','openhealthnews.com','euniverse.com','freestart.hu']

#Novo
new = ['domain1.tche.br','domain2.tche.br','domain3.tche.br','domain4.tche.br','domain5.tche.br','domain6.tche.br',
       'domain7.tche.br','domain8.tche.br','domain9.tche.br','domain10.tche.br','domain11.tche.br','domain12.tche.br',
       'domain13.tche.br','domain14.tche.br','domain15.tche.br','domain16.tche.br','domain17.tche.br','domain18.tche.br','domain19.tche.br','domain20.tche.br']

#Obtém a pasta com os dias
collection_folders = glob('*day*')


#Abre o arquivo csv para escrita, caso não exista, cria
with open('data_agg_.csv', 'w') as f_object:
    writer_object = writer(f_object)
    
    #Escreve o cabeçalho
    writer_object.writerow(['Domain','Time','Server','Country','GMT Time','Local Time','Type of Domain'])
    
    #Percorre as pastas por dia
    for item in collection_folders:
        
        country = item.split('_')[1]

        #Obtém as pastas por hora dentro de cada dia
        execution_files = sorted(glob(item + '/*'))
            
        #Percorre os arquivos de execução
        for file in execution_files:
            
            
            day_split = (file.split('/')[1]).split('.')[0]
        
            local_time = day_split.split('-')[0]
            gmt_time = day_split.split('-')[1]
    
            
            #Abre o arquivo de execução
            with open(file, 'r') as f:
                #Lê as linhas do arquivo
                lines = f.readlines()
                #Percorre cada uma das linhas do arquivo
                for line in lines:
                    #Verifica se a linha não é o cabeçalho
                    if not  "domain,google,quad9,cloudflare,comodosecuredns,opendns\n" == line:
                        #Se não for cabeçalho, separa os valores por |
                        split = line.split(',')
                        #Testa o indice 0 do split para saber o tipo de domínio
                        if split[0] in popular:
                            type_of_domain = 'Popular'
                        elif split[0] in medium:
                            type_of_domain = 'Medium'
                        elif split[0] in new:
                            type_of_domain = 'New'
                        #Escreve no arquivo csv no seguinte formato: [domínio, tempo, servidor, dia, hora, tipo]
                        sec2mili = 1000
                        if country == "brasil": 
                        #if True: # Remove to make other filters as above
                            writer_object.writerow([split[0], sec2mili*float(split[1]),'Google', country, gmt_time, local_time, type_of_domain,])
                            writer_object.writerow([split[0], sec2mili*float(split[2]),'Quad9', country, gmt_time, local_time, type_of_domain,])
                            writer_object.writerow([split[0], sec2mili*float(split[3]),'OpenDNS', country, gmt_time, local_time, type_of_domain,])
                            writer_object.writerow([split[0], sec2mili*float(split[4]),'CloudFlare', country, gmt_time, local_time, type_of_domain,])
                            writer_object.writerow([split[0], sec2mili*float(split[5]),'Comodo DNS', country, gmt_time, local_time, type_of_domain,])
