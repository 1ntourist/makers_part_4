class Airplane:

    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        if self.is_flying == False:
            print('Самолет {} взлетает!!!'.format(self.model))
        else:
            print('Самолет {} в полете!!!'.format(self.model))

    def fly(self, km, from2, where):
        self.odometer += km
        print('Самолет пролетел {} км. c максимальной скоростью {} км.час\
        from {} to {}!!!'.format(self.odometer, self.max_speed, from2, where))

    def land(self):
        if self.is_flying == True:
            print('Самолет {} в полете !!!'.format(self.model))
        else:
            print('Самолет {} приземляется !!!'.format(self.model))

air1 = Airplane('USA', 'Boeing 777', '2017', '965')
air1.take_off()
air1.fly(300, "Bishkek", "Almata")
air1.fly(500, "Almata", "Tashkent")
air1.fly(355, "Tashkent", "Bishkek")
air1.land()
