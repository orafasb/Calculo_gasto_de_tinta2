class calculadora:
    area_parede: float
    area_teto: float

    def calcular_area_paredes(self, largura, altura, profundidade):
        self.area_parede = 2*(largura+profundidade)*altura
        return self.area_parede
    def calcular_area_teto(self, largura, profundidade):
        self.area_teto = largura*profundidade
        return self.area_teto
    def calculo_litragem_necessaria(self):
        return (self.area_parede+self.area_teto
                )/10

