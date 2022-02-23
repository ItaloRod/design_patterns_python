#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    ## Singleton
            - O Singleton é um padrão de projeto criacional que permite a você garantir que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para essa instância.
            - O padrão garante  que uma classe tenha apenas uma única instância e fornece um ponto de acesso global para aquela instância.

            ### Quando usar?
                - Utilize o padrão Singleton quando uma classe em seu programa deve ter apenas uma instância disponível para todos seus clientes; por exemplo, um objeto de base de dados único compartilhado por diferentes partes do programa.
                - Utilize o padrão Singleton quando você precisa de um controle mais estrito sobre as variáveis globais.

            ### Vantagens:
                - Você pode ter certeza que uma classe só terá uma única instância.
                - Você ganha um ponto de acesso global para aquela instância.
                - O objeto singleton é inicializado somente quando for pedido pela primeira vez.

            ### Desvantagens:
                - Viola o princípio de responsabilidade única. O padrão resolve dois problemas de uma só vez.
                - O padrão Singleton pode mascarar um design ruim, por exemplo, quando os componentes do programa sabem muito sobre cada um.
                - O padrão requer tratamento especial em um ambiente multithreaded para que múltiplas threads não possam criar um objeto singleton várias vezes.
                - Pode ser difícil realizar testes unitários do código cliente do Singleton porque muitos frameworks de teste dependem de herança quando produzem objetos simulados. Já que o construtor da classe singleton é privado e sobrescrever métodos estáticos é impossível na maioria das linguagem, você terá que pensar em uma maneira criativa de simular o singleton. Ou apenas não escreva os testes. Ou não use o padrão Singleton.

            ### Obs:
             - Muitos desenvolvedores consideram o padrão Singleton um antipadrão. É por isso que seu uso está diminuindo no código Python.
"""
from creational.singleton.singleton_monothread.main import monothread_start


def start(has_multithread: bool):

    if has_multithread:
        pass
    return monothread_start()