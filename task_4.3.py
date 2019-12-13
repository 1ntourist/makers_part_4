class Car:

    def __init__(self, make, model, year):
        self.odometr = 0
        self.fuel = 70
        self.make = make
        self.model = model
        self.year = year

    def _add_distance(self, distance):
        self.odometr += distance

    def _subtract_fuel(self, fuel):
        self.fuel = self.fuel - self.distance / 10

    def drive(self, distance):
        self.distance = distance
        if self.fuel * 10 >= self.distance:
            self._add_distance(self.distance)
            self._subtract_fuel(self.fuel)
            print('Проехали {} километров!'.format(self.odometr))
            print('Осталось {} литров бензина!'.format(self.fuel))
        else:
            print("Need more fuel, please, fill more!")

a = Car('USA', 'LEXUS', '2009')
a.drive(10)
a.drive(50)
