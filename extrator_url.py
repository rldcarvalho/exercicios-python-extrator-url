class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip() if type(url) == str else ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        if not self.url.startswith('https'):
            raise ValueError("A URL não começa com https")
        if not self.get_url_base().endswith('/cambio'):
            raise ValueError("A URL não pertence a página câmbio")

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

extrator_url = ExtratorURL("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
# extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)