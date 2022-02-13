"""
    ## Adapter
            - é um padrão de projeto estrutural que permite objetos com interfaces incompatíveis colaborarem entre si.

            ### Quando usar?
                - Utilize a classe Adaptador quando você quer usar uma classe existente, mas sua interface não for compatível com o resto do seu código.
                - Utilize o padrão quando você quer reutilizar diversas subclasses existentes que não possuam alguma funcionalidade comum que não pode ser adicionada a superclasse.
        
            ### Vantagens:
                - Utiliza o Princípio de responsabilidade única. Você pode separar a conversão de interface ou de dados da lógica primária do negócio do programa.
                - Utiliza o Princípio aberto/fechado. Você pode introduzir novos tipos de adaptadores no programa sem quebrar o código cliente existente, desde que eles trabalhem com os adaptadores através da interface cliente.
                
            ### Desvantagens:
                - A complexidade geral do código aumenta porque você precisa introduzir um conjunto de novas interfaces e classes. Algumas vezes é mais simples mudar a classe serviço para que ela se adeque com o resto do seu código.
"""
from estructural.Adapter.Adaptee import Adaptee
from estructural.Adapter.Adapter import Adapter
from estructural.Adapter.Target import Target

"""
O cliente não sabe o alvo que irá passar por ele. Não é preciso alterar nada aqui sem passar pelos adapters
"""


def client_code(target) -> None:
    print(target.request())


def start():
    print("Cliente: Eu consigo trabalhar bem com os objetos do Target")

    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: A Classe Adaptee tem uma interface estranha e incompreensível")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: Mas que funciona bem com o Adapter")
    adapter = Adapter()
    client_code(adapter)
