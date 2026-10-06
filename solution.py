import requests
from datetime import datetime, timedelta

def cotar():
    cotacoes = []
    data = datetime.now()

    for i in range(365):
        dia = data - timedelta(i)
        data_formatada = datetime.strftime(dia, "%m-%d-%Y")

        url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_formatada}'&$top=100&$format=json&$select=cotacaoCompra"

        res = requests.get(url)
        res = res.json()

        if res['value']:
            cotacoes.append(res['value'][0]['cotacaoCompra'])
        else:
            dia_anterior = dia - timedelta(1)
            
            while not res['value']:
                data_anterior = datetime.strftime(dia_anterior, "%m-%d-%Y")
                
                url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_anterior}'&$top=100&$format=json&$select=cotacaoCompra"

                res = requests.get(url)
                res = res.json()

                dia_anterior = dia_anterior - timedelta(1)

            cotacoes.append(res['value'][0]['cotacaoCompra'])

    return cotacoes

#print(cotar()) // usei para testar 