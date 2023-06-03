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
            raise Exception("Lista cheia")
        
        novoNo = No(valor)

        if self.is_empty():
            novoNo.prox = novoNo
            self.__inicio = novoNo

        else:
            noAtual = self.__inicio
            noAnterior = None

            while noAtual.prox != self.__inicio and noAtual.dado < valor:
                noAnterior = noAtual
                noAtual = noAtual.prox

            if noAnterior is None:
                novoNo.prox = self.__inicio
                self.__inicio = novoNo

            else:
                novoNo.prox = noAtual
                noAnterior.prox = novoNo

        self.__qtdItens += 1
        return True
    
    # remove um elemento da lista ligada retornando True caso ele seja removido
    # se o elemento não estiver na lista ligada, retorne False
    # se a lista ligada estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove(self, valor) -> bool:
        # implementação do método
        pass


    # retornar True caso o elemento esteja presente na lista ligada
    # ou False caso contrário
    def contains(self, valor) -> No:
        # implementação do método
        if self.is_empty():
            return False

        # O nó atual como primeiro da lista
        noAtual = self.__inicio

        # Percorre a lista até encontrar novamente o primeiro nó
        # garantindo percorrer todos os nós da lista
        while noAtual.prox != self.__inicio:
            # Verifica se o valor do nó noAtual é igual ao valor procurado
            if noAtual.dado == valor:
                return True
            # Avançando para o prox nó da lista
            noAtual = noAtual.prox

        # Verificando o último nó da lista (primeiro nó)
        if noAtual.dado == valor:
            return True

        # return False caso o valor(elemento) não tenha sido encontrado em nenhum nó
        return False


    # retorna uma lista de string com valores dos elementos da lista ligada
    # imprima os elementos da lista ligada do primeiro para o último
    # caso a lista ligada esteja vazia, imprime uma mensagem informando
    # que a lista ligada está vazia e retorna uma lista vazia
    def display(self) -> list[str]:
        # implementação do método
        pass
    

    # retorna a quantidade de elementos na lista ligada
    # se a lista ligada estiver vazia, retorna ZERO
    def size(self) -> int:
        # implementação do método
        return self.__qtdItens
