class Soldier:
    def __init__(self, name):
        self.name = name

class Guns:
    def __init__(self, name, magazine, bullets):
        all_bullets = 0
        self.name = name
        self.magazine = magazine
        self.bullets = bullets

class Act_of_Shooting(Guns, Soldier):

    def __init__(self, bull, name, magazine, bullets):
        super().__init__(name, magazine, bullets)
        self.bull = bull

    def reload(self):
        if self.bullets > self.magazine:
            self.bull = self.magazine
            self.bullets -= self.magazine
            print('You reload your arm!\nYou have {} bull, you can shoot'.format(self.bull))
            print(self.bullets)
            self.shooting()
        elif self.bullets < self.magazine and self.bullets != 0:
            self.bull = self.magazine - self.bullets
            self.bullets = 0
            print('You reload your arm!\nYou have {} bull, you can shoot'.format(self.bull))
            self.shooting()
        else:
            print("\tYou have not bulls, you can't shooting!!!")

    def shooting(self):
        if self.bull :
            while self.bull != 0:
                print('You shooting! You have {} bulls!'.format(self.bull))
                self.bull -= 1
            self.reload()

st = Act_of_Shooting(3, 'AK-47', 10, 15)
st.shooting()
