# Entendendo o que é uma Classe - Programação Orientada a Objetos

class Pessoa: # Em termos de hierarquia, a class sempre virá primeiro
    def __init__(self, nome, idiade):
        self.nome = nome # criação da variável self.nome e atribuição ao nome 
        self.idade = idade  # criação da variável self.idade e atribuição ao idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


p1 = Pessoa("Vinicius", 26)
p2 = Pessoa("Viviane", 22)
p1.apresentar()
p2.apresentar()



class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem/100)
        self.preco -= desconto
    
    def momstrar_produto (self):
        print(f"{self.nome} custa R$ {self.preco:2f}")

produto = Produto("Munitor", 1200)
produto.momstrar_produto()
produto.aplicar_desconto(10)
produto.momstrar_produto()