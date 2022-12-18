from structures.arvoreAVL import AVLTree
from modules.palavra import Palavra
import random

class GamaException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)

class Tema:
    def __init__(self, nome:str, palavras:list[Palavra]):
        try:
            assert nome != '' and len(palavras) > 0  #and teto <= len(palavras)
            self.__nome = nome
            self.__avlPalavras = AVLTree()
            #self.__tetoSorteio = teto  # pode ser passado no sorteio em si
            self.__preencherPalavras(palavras)
        except AssertionError:
            raise GamaException('Entradas (nome, teto e/ou palavras) inválidas!')


    def __str__(self):
        return f'{self.__nome} : {self.__strPalavras()}'

    # @property
    # def tetoSorteio(self) -> int:
    #     '''Retorna o número de palavras a serem sorteadas'''
    #     return self.__tetoSorteio

    @property
    def avlPalavras(self) -> list[Palavra]:
        '''Retorna a lista de palavras que está na árvore'''
        return self.__avlPalavras.getNodes()

    # @tetoSorteio.setter
    # def tetoSorteio(self, teto:int) -> int:
    #     '''Altera o número de palavras a serem sorteadas'''
    #     self.__tetoSorteio = teto
    #     return self.__tetoSorteio

    def __preencherPalavras(self, palavras:list[Palavra]):
        '''Insere novas palavras na lista de palavras'''
        for palavra in palavras:
            self.__avlPalavras.insert(palavra)

    def __strPalavras(self):
        '''Método auxiliar utilizado no método especial __str__'''
        palavras = self.__avlPalavras.getNodes()
        temp = []
        for i in palavras:
            temp.append(str(i))
        return temp

    def sortearPalavras(self, teto:int) -> list:
        try:
            assert teto > 0 and teto <= len(self.__strPalavras())
            palavras = self.__avlPalavras.getNodes()
            random.shuffle(palavras)
            return palavras[:teto]
        except:
            raise GamaException('Entradas (teto) inválidas!')
