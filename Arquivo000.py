class GeradorCPNJ:
    def __init__(self, cnpj):
        self.cnpj = cnpj

    def off_caracteres(self):
        from re import sub

        return sub(r'[^0-9]', '', self.cnpj)

    def on_caracteres(self):
        return f'{self.cnpj[:2]}.{self.cnpj[2:5]}.{self.cnpj[5:8]}/{self.cnpj[8:12]}-{self.cnpj[12:]}'

    def test_cnpj(self, cnpj):
        self.cnpj = cnpj[:-2]
        for vez in range(2):
            total = 0
            for indice in range(12 + vez):
                if indice < (4 + vez):
                    posicao = (5 + vez) - indice
                else:
                    posicao = (13 + vez) - indice
                num = int(self.cnpj[indice])
                total += num * posicao

            digito = 11 - (total % 11)
            if digito > 9:
                digito = 0

            self.cnpj += str(digito)

        return self.cnpj


