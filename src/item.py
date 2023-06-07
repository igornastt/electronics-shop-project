import csv


class InstantiateCSVError(Exception):
    """Класс исключения, если файл поврежден"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return int(self.quantity) + int(other.quantity)
        raise ValueError("Складывать можно только экземпляры классов Item и Phone")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):

        try:
            self.__name = name
            if len(self.name) <= 10:
                return True
        except Exception:
            return "Длина наименования товара превышает 10 символов"

    @classmethod
    def instantiate_from_csv(cls):
        '''
        Инициализирует экземпляры класса,
        получает обЪекты из файла  csv
        '''

        cls.all.clear()
        try:
            with open('../src/items.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])


        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError:
            print("Файл item.csv поврежден")


    @staticmethod
    def string_to_number(line):
        '''
        Возвращает число из числа-строки
        '''
        line = float(line)
        return int(line)
