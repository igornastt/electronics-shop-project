import csv


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
            print("Файл не найден")

    @staticmethod
    def string_to_number(line):
        '''
        Возвращает число из числа-строки
        '''
        line = float(line)
        return int(line)

