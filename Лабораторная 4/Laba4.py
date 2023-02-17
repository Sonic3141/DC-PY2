if __name__ == "__main__":
    # Write your solution here
    pass

class Table:
    """ Базовый класс, описывающий таблицу """

    def __init__(self, name: str, colour: str):
        self.name = name #название таблицы
        self.colour = colour #цвет ячеек таблицы
        self.num_add_element = 0 #число  добавленных элементов

    def add_element(self, num_element: int) -> int: #добавление элементов в таблицу
        """
        Метод увеличивает число добавленных элементов
        :param num_element: количество элементов(которых хотят добавить)
        :return: 
        """
        self.num_add_element += num_element
    def extract_element(self, num: int) -> int: #вызов заданного числа элементов таблицы
        ...
        """
        Метод вызывает заданное количество элементов таблицы
        :param num число элементов 
        :return: 
        """
    def change_colour(self, el1: int, el2: int) -> None: #el1 и el2 указанные номера ячеек
        ...
    """ 
    Метод меняет цвет элементов(ячеек)
    """

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'

    def __str__(self):
        return f'Таблица "{self.name}"'

class Mendeleev(Table):
    """Дочерний класс Таблиц, Периодическая система Менделеева """
    def __init__(self, name: str, period: int, group: int, typ: str = "неметалл" ):
        super().__init__(name) #расширение производного класса(наследование)
        self.period = period #период хим. элемента
        self.group = group  #группа хим. элемента
        self.typ = typ #тип элемента(металл - неметалл)

    def add_element(self, num_element: int) -> int:
        super().add_element(num_element) # наследование метода

    def extract_element(self, period: int, group: int) -> int:
        super().extract_element(period, group) #наследование метода и перегрузка, так как выделяются не элементы а периоды и группы из таблицы

    def __repr__(self) -> str: #перегрузка магического метода repr
        return f'{self.__class__.__name__}({self.name!r}, {self.period!r}, {self.group!r}, {self.type!r}) '

    def __str__(self):
        return f'Таблица Менделеева "{self.name}"' #перегрузка метода str



class Bradis(Table):
    """Дочерний класс, Таблица Брадиса
    содержит значения тригонометрических формул"""
    def __init__(self, name: str, trig: str = "sin"):
        super().__init__(name) #наследование
        self.trig = trig #тригонометрическая формула, по умолчанию синус
    def add_element(self, num_element: int) -> int:
        super().add_element(num_element) # наследование метода

    def extract_element(self, trig: str) -> int:
        super().extract_element(trig) #наследование метода и перегрузка, так как выделяется триг. формула из таблицы Брадиса

    def __repr__(self) -> str: #перегрузка магического метода repr
        return f'{self.__class__.__name__}({self.name!r}, {self.trig!r})'

    def __str__(self):
        return f'Таблица Брадиса "{self.name}"' #перегрузка метода str, так как таблица имеет другое название

class Particles(Table):
    """Дочерниц класс, Таблица элементарных частиц"""
    def __init__(self, name: str, spin: int, colour: str, charge: str = "+"):
        super().__init__(name, colour) #наследование
        self.charge = charge #заряд частицы
        self.spin = spin #спин частицы

    def change_colour(self, spin1: int, spin2: int) -> None:
        super().change_colour(spin1, spin2) #наследование и перегрузка метода, меняются цвета частиц с указанными спинами

    def __repr__(self) -> str: #перегрузка магического метода repr
        return f'{self.__class__.__name__}({self.name!r}, {self.charge!r}, {self.spin!r})'
    def __str__(self):
        return f'Таблица элементарных частиц "{self.name}"' #перегрузка метода str

