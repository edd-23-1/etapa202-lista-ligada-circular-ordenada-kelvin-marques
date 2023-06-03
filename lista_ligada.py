# -*- coding:UTF-8 -*-
from no import No

class ListaLigada:
    """
    Implementação de Lista Ligada Ordenada com Capacidade
    A lista a ser implementada deverá ser em ordem crescente
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Lista Ligada com capacidade: {capacidade}")


    # retorna True se a lista ligada está vazia, False caso contrário
    def is_empty(self) -> bool:
        # implementação do método
        return self.__inicio is None

    
    # retorna True se a lista ligada está cheia, False caso contrário
    def is_full(self) -> bool:
        # implementação do método
        return self.__qtdItens == self.__capacidade


    # insere um elemento na lista ligada em ordem crescente em seguida retorna True
    # se a lista ligada estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
    def add(self, valor) -> bool:
        # implementação do método
        if self.is_full():
            raise Exception("Lista ligada cheia")
        
        novoNo = No(valor)

        if self.is_empty():
            self.__inicio = novoNo

        else:
            noAtual = self.__inicio
            noAnterior = None
            
            while noAtual is not None and noAtual.dado < valor:
                noAnterior = noAtual
                noAtual = noAtual.prox
            
            if noAnterior is None:
                novoNo.prox = self.__inicio
                self.__inicio = novoNo
            
            else:
                noAnterior.prox = novoNo
                novoNo.prox = noAtual

        self.__qtdItens += 1
        return True

    
    # remove um elemento da lista ligada retornando True caso ele seja removido
    # se o elemento não estiver na lista ligada, retorne False
    # se a lista ligada estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove(self, valor) -> bool:
        # implementação do método
        if self.is_empty():
            raise Exception("Lista ligada vazia")

        if self.__inicio.dado == valor:
            self.__inicio = self.__inicio.prox
            self.__qtdItens -= 1
            return True

        noAtual = self.__inicio
        noAnterior = None

        while noAtual is not None and noAtual.dado != valor:
            noAnterior = noAtual
            noAtual = noAtual.prox

        if noAtual is None:
            return False

        noAnterior.prox = noAtual.prox
        self.__qtdItens -= 1
        return True


    # retornar True caso o elemento esteja presente na lista ligada
    # ou False caso contrário
    def contains(self, valor) -> No:
        # implementação do método
        if self.is_empty():
            return False
        
        noAtual = self.__inicio

        while noAtual is not None:
            if noAtual.dado == valor:
                return True
            
            noAtual = noAtual.prox

        return False


    # retorna uma lista de string com valores dos elementos da lista ligada
    # imprima os elementos da lista ligada do primeiro para o último
    # caso a lista ligada esteja vazia, imprime uma mensagem informando
    # que a lista ligada está vazia e retorna uma lista vazia
    def display(self) -> list[str]:
        # implementação do método
        if self.is_empty():
            print("Lista ligada vazia")
            return []

        valores = []
        noAtual = self.__inicio
        while noAtual is not None:
            valores.append(noAtual.dado)
            noAtual = noAtual.prox

        return valores
    

    # retorna a quantidade de elementos na lista ligada
    # se a lista ligada estiver vazia, retorna ZERO
    def size(self) -> int:
        # implementação do método
        return self.__qtdItens
