from abc import ABC, abstractmethod

class Pedido():
    def __init__(self, numero, cliente):
        self.__numero = numero
        self.__cliente = cliente
        self.__listaItens = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def listaItens(self):
        return self.__listaItens

    def addItem(self, item):
        self.__listaItens.append(item)

    #Verifica se o pedido está completo a partir do código dos produtos
    def maquinaOk(self):
        categorias = {
            'gabinete': False,
            'placa_mae': False,
            'processador': False,
            'ssd': False,
            'memoria': False,
            'sistema': False
        }

        for item in self.listaItens:
            cod = item.produto.codigo
            if 100 <= cod <= 199:
                categorias['gabinete'] = True
            elif 200 <= cod <= 299:
                categorias['placa_mae'] = True
            elif 300 <= cod <= 399:
                categorias['processador'] = True
            elif 400 <= cod <= 499:
                categorias['ssd'] = True
            elif 500 <= cod <= 599:
                categorias['memoria'] = True
            elif 600 <= cod <= 699:
                categorias['sistema'] = True

        return all(categorias.values())

    def imprimePedido(self):
        if not self.maquinaOk():
            print("Pedido está incompleto")
            return False

        
        print(f"Cliente: {self.cliente.nome} ")
        print()
        print("\nQuant - Produto - Preço Unit - Preço Total ")

        total_pedido = 0
        for item in self.listaItens:
            produto = item.produto
            imposto = produto.calculaImposto()
            preco_com_imposto = produto.preco + imposto
            total_item = preco_com_imposto * item.quant
            total_pedido += total_item

            print(f"{item.quant}     -  {produto.desc} -  {preco_com_imposto:.2f} - {total_item:.2f}")

        print(f"\nValor total: {total_pedido:.2f}")
        return True


class ItemPedido():
    def __init__(self, nroItem, produto, quant):
        self.__nroItem = nroItem
        self.__produto = produto
        self.__quant = quant

    @property
    def nroItem(self):
        return self.__nroItem

    @property
    def produto(self):
        return self.__produto

    @property
    def quant(self):
        return self.__quant


class Produto(ABC):
    def __init__(self, codigo, desc, preco):
        self.__codigo = codigo
        self.__desc = desc
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo

    @property
    def desc(self):
        return self.__desc

    @property
    def preco(self):
        return self.__preco

    @abstractmethod
    def calculaImposto(self):
        pass


class ProdutoSoftware(Produto):
    def __init__(self, codigo, desc, preco, versao):
        super().__init__(codigo, desc, preco)
        self.__versao = versao

    @property
    def versao(self):
        return self.__versao

    def calculaImposto(self):
        if self.preco <= 399.99:
            return self.preco * 0.05
        else:
            return self.preco * 0.07


class ProdutoHardware(Produto):
    def __init__(self, codigo, desc, preco, nroSerie):
        super().__init__(codigo, desc, preco)
        self.__nroSerie = nroSerie

    @property
    def nroSerie(self):
        return self.__nroSerie

    def calculaImposto(self):
        if self.preco <= 499.99:
            return self.preco * 0.06
        else:
            return self.preco * 0.09


class Cliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email



if __name__ == "__main__":    
    #Exemplo de uso
    prod1 = ProdutoHardware(101, 'Gabinete Padrão', 200, '12345')
    prod2 = ProdutoHardware(102, 'Gabinete Gamer', 300, '23451')
    prod3 = ProdutoHardware(201, 'Placa Mãe ASUS ROG', 1400, '345123')
    prod4 = ProdutoHardware(202, 'Placa Mãe Gigabyte Elite', 1800, '45123')
    prod5 = ProdutoHardware(301, 'Intel Core I5', 900, '51234')
    prod6 = ProdutoHardware(302, 'AMD Ryzen 7', 700, '67890')
    prod7 = ProdutoHardware(401, 'SSD 256', 200, '78906')
    prod8 = ProdutoHardware(402, 'SSD 512', 300, '89067')
    prod9 = ProdutoHardware(501, 'Pente memória 8GB', 180, '90678')
    prod10 = ProdutoSoftware(601, 'Windows 11 Home Edition', 250, '23H2')

    cliente1 = Cliente('João Santos', 'santos@gmail.com')
    cliente2 = Cliente('Maria Souza', 'souza@gmail.com')

    pedido1 = Pedido(1001, cliente1)
    pedido1.addItem(ItemPedido(1, prod1, 1))
    pedido1.addItem(ItemPedido(2, prod3, 1))
    pedido1.addItem(ItemPedido(3, prod7, 1))
    pedido1.addItem(ItemPedido(4, prod9, 2))
    if not pedido1.imprimePedido():
        print("\nPedido está incompleto")

    pedido2 = Pedido(1002, cliente2)
    pedido2.addItem(ItemPedido(1, prod2, 1))
    pedido2.addItem(ItemPedido(2, prod4, 1))
    pedido2.addItem(ItemPedido(3, prod6, 1))
    pedido2.addItem(ItemPedido(4, prod8, 1))
    pedido2.addItem(ItemPedido(5, prod9, 2))
    pedido2.addItem(ItemPedido(6, prod10, 1))
    if not pedido2.imprimePedido():
        print("\nPedido está incompleto")
