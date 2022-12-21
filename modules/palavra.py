class GamaException(Exception):
    #Tratamento de erro#
    def __init__(self, msg) -> None:
        super().__init__(msg)

class Palavra:
    '''
    Classe que armazena as informações sobre uma palavra. Tais informções são:
    peso e termo. O peso é a dificuldade da palavra e o termo é a string em si.
    '''
    #Classe palavra é estruturada como tupla, [0] é seu peso e [1] é termo, este termo é a string da palavra propriamente dita
    def __init__(self, peso:int, termo:str):
        try:
            assert peso > 0 and termo != ''
            self.__peso = peso
            self.__termo = termo
        except AssertionError:
            raise GamaException('Entradas (peso e/ou termo) inválidas!')

    def __str__(self):
        return f'{self.__termo} : {self.__peso}'

    def __lt__(self, other) -> bool:
        return self.__peso < other.__peso 

    def __le__(self, other) -> bool:
        return self.__peso <= other.__peso 

    def __eq__(self, other) -> bool:
        return self.__peso == other.__peso 

    def __ne__(self, other) -> bool:
        return self.__peso != other.__peso 

    def __gt__(self, other) -> bool:
        return self.__peso > other.__peso 

    def __ge__(self, other) -> bool:
        return self.__peso >= other.__peso 

    @property
    def peso(self) -> int:
        return self.__peso

    @property
    def termo(self) -> int:
        return self.__termo

    @peso.setter
    def peso(self, peso:int) -> int:
        try:
            assert peso > 0
            self.__peso = peso
        except AssertionError:
            raise GamaException('Entradas (peso) inválidas!')

    @termo.setter
    def termo(self, termo:int) -> int:
        try:
            assert termo != ''
            self.__termo = termo
        except AssertionError:
            raise GamaException('Entradas (termo) inválidas!')