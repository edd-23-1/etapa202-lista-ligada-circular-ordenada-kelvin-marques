# -*- coding:UTF-8 -*-
from no import No

class ListaLigadaCircularOrdenada:
    """
    Implementação de Lista Ligada Circular Ordenada com Capacidade
    A lista a ser implementada deverá ser em ordem crescente
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Lista Ligada Circular com capacidade: {capacidade}")


    # Retorna True se a lista ligada está vazia, False caso contrário
    def is_empty(self) -> bool:
        # implementação do método
        return self.__qtdItens == 0

    
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
            novoNo.prox = novoNo 
            self.__inicio = novoNo
        else:
            noAtual = self.__inicio
            noAnterior = None

            if valor <= noAtual.dado:
                while noAtual.prox != self.__inicio:
                    noAtual = noAtual.prox
                noAtual.prox = novoNo
                novoNo.prox = self.__inicio
                self.__inicio = novoNo
            else:
                while noAtual.prox != self.__inicio and valor > noAtual.prox.dado:
                    noAtual = noAtual.prox
                novoNo.prox = noAtual.prox
                noAtual.prox = novoNo

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
            if self.__inicio.prox == self.__inicio:
                self.__inicio = None
            else:
                noAtual = self.__inicio
                while noAtual.prox != self.__inicio:
                    noAtual = noAtual.prox
                noAtual.prox = self.__inicio.prox
                self.__inicio = self.__inicio.prox
            self.__qtdItens -= 1
            return True

        noAtual = self.__inicio
        noAnterior = None

        while noAtual.prox != self.__inicio and noAtual.dado != valor:
            noAnterior = noAtual
            noAtual = noAtual.prox

        if noAtual.prox == self.__inicio:
            return False

        noAnterior.prox = noAtual.prox
        self.__qtdItens -= 1

        # Atualiza o ponteiro do último nó para o novo início da lista
        if noAtual == self.__inicio:
            while noAnterior.prox != self.__inicio:
                noAnterior = noAnterior.prox
            noAnterior.prox = self.__inicio

        return True


    # retornar True caso o elemento esteja presente na lista ligada
    # ou False caso contrário
    def contains(self, valor) -> No:
        # implementação do método
        if self.is_empty():
            return False

        noAtual = self.__inicio

        while noAtual.prox != self.__inicio:
            if noAtual.dado == valor:
                return True
            noAtual = noAtual.prox

        if noAtual.dado == valor:
            return True

        return False


    # retorna uma lista de string com valores dos elementos da lista ligada
    # imprima os elementos da lista ligada do primeiro para o último
    # caso a lista ligada esteja vazia, imprime uma mensagem informando
    # que a lista ligada está vazia e retorna uma lista vazia
    def display(self) -> list[str]:
        # implementação do método
        if self.is_empty():
            print("Lista ligada circular vazia.")
            return []

        elementos = []
        pointer = self.__inicio
        while pointer.prox != self.__inicio:  # Verifica se o ponteiro chegou novamente ao início
            elementos.append(pointer.dado)
            pointer = pointer.prox

        elementos.append(pointer.dado)  # Adiciona o último elemento (início)
        return elementos
    

    # retorna a quantidade de elementos na lista ligada
    # se a lista ligada estiver vazia, retorna ZERO
    def size(self) -> int:
        # implementação do método
        count = 0

        if self.is_empty():
            return count

        atual = self.__inicio
        count += 1

        while atual.prox != self.__inicio:
            count += 1
            atual = atual.prox

        return count
