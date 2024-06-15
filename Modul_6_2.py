class Vehicle:
    __COLOR_VARIANTS = ["red", "black", "blue", "silver"]

    def __init__(self,vl,modl,col,pow):
        self.owner = vl
        self.__model = modl
        self.engine_power = int(pow)
        self.__color = col
    def get_model(self):
        return self._Vehicle__model
    def get_horsepower(self):
        return self.engine_power
    def get_color(self):
        return self._Vehicle__color
    def print_info(self):
        print(f"Модель: {Vehicle.get_model(self)}")
        print(f"Мощность двигателя:  {Vehicle.get_horsepower(self)}")
        print(f"Цвет: {Vehicle.get_color (self)}")
        print(f"Владелец: {self.owner} .")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5




    # def get_model(self):
    #     return self._Vehicle__model
    # def get_horsepower(self):
    #     return self.engine_power
    # def get_color(self):
    #     return self._Vehicle__color
    def set_color(self,new_color):
        if new_color.lower() in self._Vehicle__COLOR_VARIANTS:
            self._Vehicle__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}.")


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
print(dir(vehicle1))
print(vehicle1.__dict__)
# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()