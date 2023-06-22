import dns.resolver
import time
from datetime import datetime
from datetime import date
import glob
import os

from csv import writer

today = datetime.today()

day = today.strftime("%d%m%Y") # Local time
hour = time.strftime("L%H")
hour_utc = datetime.utcnow().strftime("%d%m%YT%H") # Get GMT-0

def resolver_dns(dominio, tipo):
    try:
        resposta = dns.resolver.resolve(dominio, tipo)
        print(dominio)
    except Exception as e:     
        print(e)
        
        
if __name__ == "__main__":

    resolvers = ["8.8.8.8","9.9.9.9","1.1.1.1","8.26.56.26","208.67.222.222"]
    
    domains = ['google.com','youtube.com','facebook.com','a-msedge.net','microsoft.com','netflix.com','epicgames.com','akamaiedge.net','gtld-servers.net','twitter.com','instagram.com','baidu.com'
,'amazonaws.com','apple.com','linkedin.com','cloudflare.com','wikipedia.org','yahoo.com','qq.com','akamai.net','domain1.tche.br','domain2.tche.br','domain3.tche.br','domain4.tche.br','domain5.tche.br',
'domain6.tche.br','domain7.tche.br','domain8.tche.br','domain9.tche.br','domain10.tche.br','domain11.tche.br','domain12.tche.br','domain13.tche.br','domain14.tche.br','domain15.tche.br',
'domain16.tche.br','domain17.tche.br','domain18.tche.br','domain19.tche.br','domain20.tche.br','tabsite.com','yuukagetsu.com','kafene.com','yuzu-tosou.com','lotzadollars.com',
'ywproperty.com','yxbabe.com','gtd4xzbo4mycmst.com','joyfulhour.net','bentoncollections.com','yyfxgzs.com','bonpost.ru','notary.net','yywater.tw','shopiro.ca','facetfiez.space','yztown.vip',
'openhealthnews.com','euniverse.com','freestart.hu']
    

    print('results/' + str(day + hour + '-' + hour_utc) + '.csv')
    current = os.getcwd()   
    directory_root = '/home/mffranco'
    with open(directory_root + '/results/' + str(day + hour + '-' + hour_utc) + '.csv', 'w') as f_object:
        writer_object = writer(f_object, delimiter=",")
        writer_object.writerow(["domain","google","quad9","cloudflare","comodosecuredns","opendns"])
        for i in range(0,30):
            for domain  in domains:
                    times = []
                    
                    times.append(domain)

                    for resolver in resolvers:
                        dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
                        dns.resolver.default_resolver.nameservers = [resolver]
                        dns.resolver.timeout = 5
                        
                        tipo = 'NS'
                        if "tche" in domain:	 
                            tipo = 'A'   
                        start_time = time.time()
                        resolver_dns(domain, tipo)                 
                        end_time = time.time() - start_time                  
                        times.append(str(end_time))
                       

                    
                    writer_object.writerow(times)
