class PreciousStone:
    def __init__(self, name='', carats=0, price=0.0, numeric_field=0, string_field=''):
        self.__name = name
        self.__carats = carats
        self.__price = price
        self.__numeric_field = numeric_field
        self.__string_field = string_field

    def get_name(self):
        return self.__name

    def get_carats(self):
        return self.__carats

    def get_price(self):
        return self.__price

    def get_numeric_field(self):
        return self.__numeric_field

    def get_string_field(self):
        return self.__string_field

    def set_name(self, name):

        self.__name = name

    def set_carats(self, carats):
        self.__carats = carats

    def set_price(self, price):
        self.__price = price

    def set_numeric_field(self, numeric_field):
        self.__numeric_field = numeric_field

    def set_string_field(self, string_field):
        self.__string_field = string_field

    def __str__(self):
        return f"Name: {self.__name}, Carats: {self.__carats}, Price: {self.__price}, Numeric Field: {self.__numeric_field}, String Field: {self.__string_field}"

    def __repr__(self):
        return f"PreciousStone({self.__name}, {self.__carats}, {self.__price}, {self.__numeric_field}, {self.__string_field})"

    def __del__(self):
        print(f"The precious stone {self.__name} was destroyed!")

if __name__ == '__main__':
    stone1 = PreciousStone('Diamond', 5, 10000, 42, 'Beautiful')
    stone2 = PreciousStone('Ruby', 3, 5000, 30, 'Red')
    stone3 = PreciousStone('Sapphire', 4, 8000, 35, 'Blue')

    print(stone1)
    print(stone2)
    print(stone3)


