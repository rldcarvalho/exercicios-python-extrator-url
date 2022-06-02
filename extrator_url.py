import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip() if type(url) == str else ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao + 1:]

    def get_valor_parametro(self, parametro_busca):
        url_parametros = self.get_url_parametros()
        indice_parametro = url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = url_parametros.find('&', indice_valor)
        return url_parametros[indice_valor:] if indice_e_comercial == -1 else url_parametros[indice_valor:indice_e_comercial]

    def converter_moeda(self):
        valor_dolar = 4.7
        moeda_origem = self.get_valor_parametro('moedaOrigem')
        moeda_destino = self.get_valor_parametro('moedaDestino')
        quantidade = int(self.get_valor_parametro('quantidade'))
        if moeda_origem == 'dolar' and moeda_destino == 'real':
            return 'Valor da conversão: ' + str(quantidade * valor_dolar) + ' reais'
        elif moeda_origem == 'real' and moeda_destino == 'dolar':
            return 'Valor da conversão: ' + str(quantidade / valor_dolar) + ' dólares'
        else:
            raise ValueError('Moedas de origem e destino não suportadas')

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

extrator_url = ExtratorURL("https://bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real")
# extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
valor_convertido = extrator_url.converter_moeda()
print('Quantidade: ' + valor_quantidade)
print(valor_convertido)