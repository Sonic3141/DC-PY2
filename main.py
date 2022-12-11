import doctest

class Fish:
    def __init__(self, type: str, num_fish: int): #type- порода рыбки, num_fish - число рыбок такой породы
        fish = Fish("Clown", 2)# инициализация экземпляра класса

        if not isinstance(type, (str)):
            raise TypeError("Порода рыбки должна быть str")
        if num_fish < 0:
            raise ValueError("Количество рыбок не может быть отрицательным числом")
        self.num_fish = num_fish

    def bubble(self) -> bool:

        """Функция, которая позволяет рыбам пускать пузыри
        Пример:
        fish = Fish('Clown',3)
        fish.bubble()
        :return:  сообщение, что выбранные  рыбки пускают пузырьки
        """
    def stop_bubble(self) -> bool:
        """
        Функция для того, чтобы выбранные рыбки не пускали пузыри
        Пример:
        fish = Fish('Clown', 3)
        fish.stop_bubble()
        :return: сообщение,что выбранные рыбки больше не пускают пузырьки

        """
    def eat_fish(self, num_to_eat) -> None:
        """
        Функция, в которой можно указать какую рыбу съедят другие рыбы
        Пример:
        fish = Fish('Clown', 3)
        fish.eat_fish(2)
        :raise ValueError: Если количество съеденных рыб > их количества или отрицательное, то выдаётся ошибка
        ...
        """
class Telegram:
    def __init__(self, name: str, surname: str, phone: str): #имя фамилия и телефон пользователя
        person = Telegram("Pavel","Durov", "+7 971 4 4099000")# инициализация экземпляра класса

        if not isinstance(phone, (str)):
            raise TypeError("Номер телефона должен быть типа str")
        if name == None or surname == None :
            raise ValueError("Имя и фамилия должны быть указаны")
        ...

    def сhange(self) -> bool:

        #Функция, которая меняет имя или фамилию
        ...
        """Примеры:
        >>> person = Telegram("Pavel","Durov", "+7 971 4 4099000")
        >>> person.change("Alisher", "Usmanov")"""
    def message(self, sms: str) -> bool:

        #Отправляет сообщение указанному пользователю
        ...
        """:param sms:  само сообщение пользователю

        Примеры:
        >>> person = Telegram('dadya', 'stepa','89213027777')
        >>> person.message("hello!World...")"""
        ...
        return "Сообщение отправлено"



class Guitar:
    def __init__(self, type: str, num_string: int): #вид гитары и число ее струн
        guitar = Guitar("Bass Ural", 4)# инициализация экземпляра класса

        if not isinstance(type, (str)):
            raise TypeError("Вид гитары должен быть str")
        if num_string < 0:
            raise ValueError("Число струн не может быть меньше нуля")
        self.num_string = num_string

   def out_of_tune(self, number) -> None:
       """
       :param number: какая струна расстроется
       :raise ValueError: Если номер струны больше общего количества струн или номер <= 0, то выдаётся ошибка
       :return: выводит сообщение, что выбранная струна расстроена
       Примеры:
       >>> guitar = Guitar("Bass Ural", 4)
       >>>guitar.out_of_tune(2)
        """
       ...

   def play_music(self, time:int) -> None
       """
               #Функция которая позволяет гитаре издавать мелодию
               :param time: длительность игры в минутах
                :raise ValueError: Если время не integer выдаёт ошибку
               Пример:
               >>> guitar = Guitar("Bass Ural", 4)
               >>> guitar.play_music(5)
               :return:  сообщение, что гитара играет 5 минут
               """

if __name__ == "__main__":
   doctest.testmod()  # тестирование примеров, которые находятся в документации
   ...