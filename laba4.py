class Human:
    __default_name = "No name"
    __default_age = 0

    def __init__(self, name=__default_name, age=__default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name} \nAge: {self.age} \nMoney: {self.__money} \nHouse: {self.__house}")

    @staticmethod
    def default_info(default_name=__default_name, default_age=__default_age):
        print(f"default_name: {default_name} \ndefault_age: {default_age}")

    def __make_deal(self, small_house_price):  # покупка дома
        self.__money = self.__money - small_house_price
        self.__house = Bob_Home

    def earn_money(self):  # увеличение кол-ва значения денег
        print(f"Earned {1000} money!", end="")
        self.__money = self.__money + 1000
        print(f" Current value {self.__money}")

    def buy_house(self):
        print(f"Final price: {Bob_Home.final_price()}")
        small_house_price = Bob_Home.final_price()
        if self.__money < small_house_price:
            print("Not enough money!")
        else:
            Bob.__make_deal(small_house_price)


class House:
    def __init__(self, area=0, price=0):
        self._area = area
        self._price = price

    def final_price(self):
        self._price = self._area * 30
        return self._price


class SmallHouse(House):
    def __init__(self, obj=40):
        self._area = obj


Human.default_info()
Bob = Human("Bob", 25)
Bob.info()
Bob_Home = SmallHouse()
Bob.buy_house()
Bob.earn_money()
Bob.buy_house()
Bob.earn_money()
Bob.buy_house()
Bob.info()