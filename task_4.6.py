class House:
    furniture = {'bed':4, 'wardrobe':2, 'table':1.5}

    def __init__(self, dlina, wirina):
        self.dlina = dlina
        self.wirina = wirina

    def furniture_in_house(self, **args):
        furniture_in = {}
        self.furniture.update(furniture_in)
        print(self.furniture)


    def area(self):

        area_of_furniture = 0
        for value in self.furniture.values():
            area_of_furniture += value
        print('Площадь всей мебели: ', area_of_furniture)

        area_of_house = self.dlina * self.wirina
        print('Площадь всего дома: ', area_of_house)

        raznica = area_of_house - area_of_furniture
        print('Площадь дома без мебели: ', raznica)

h1 = House(10, 10)
h1.area()
h1.furniture_in_house()
