from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """Возвращает атрибут количества сим-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_number):
        if sim_number > 0 and isinstance(sim_number):
            self.__number_of_sim = sim_number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")


