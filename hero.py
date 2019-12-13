import random

class Soldat:
    def __init__(self):
        self.units_level_1 = list(range(1, 21))
        self.units_level_2 = list(range(1, 41))
        self.units_level_3 = list(range(1, 61))

        self.team_list_1 = []
        self.team_list_2 = []

    def distribution_level_1(self):
        '''Рандомное распределение юнитов на 1м уровне'''
        for u in self.units_level_1:
            random.choice([self.team_list_1, self.team_list_2]).append('unit_' + str(u))
            if len(self.team_list_1) == 20 or len(self.team_list_2) == 20:
                break
        # print(f'{len(self.team_list_1)}, {len(self.team_list_2)}')

    def distribution_level_2(self):
        '''Рандомное распределение юнитов на 2м уровне'''
        # print(print(f'{len(self.team_list_1)}, {len(self.team_list_2)}'))
        for u in self.units_level_2:
            random.choice([self.team_list_1, self.team_list_2]).append('unit_' + str(u))
            if len(self.team_list_1) == 50 or len(self.team_list_2) == 50:
                break
        # print(f'{len(self.team_list_1)}, {len(self.team_list_2)}')

    def distribution_level_3(self):
        '''Рандомное распределение юнитов на 3м уровне'''
        # print(print(f'{len(self.team_list_1)}, {len(self.team_list_2)}'))
        for u in self.units_level_3:
            random.choice([self.team_list_1, self.team_list_2]).append('unit_' + str(u))
            if len(self.team_list_1) == 100 or len(self.team_list_2) == 100:
                break
        # print(f'{len(self.team_list_1)}, {len(self.team_list_2)}')




class Hero(Soldat):
    '''создание героев'''
    def __init__(self, hero_1, hero_2):
        self.hero_1 = hero_1
        self.hero_2 = hero_2

    def level_of_hero_1(self):
        '''Функция контролирующая уровень 1го героя'''
        if len(self.team_list_1) < 20:
            str = f'{self.hero_1} stay on level 1!\tHe has {len(self.team_list_1)} units!'
            print(str)
        elif len(self.team_list_1) == 20:
            str = f'{self.hero_1} has level 2!\tHe has {len(self.team_list_1)} units!\tHe can have 50 units!'
            print(str)
        elif 50 > len(self.team_list_1) > 20:
            str = f'{self.hero_1} stay on level 2!\tHe has {len(self.team_list_1)} units!'
            print(str)
        elif len(self.team_list_1) == 50:
            str = f'{self.hero_1} has level 3!\tHe has {len(self.team_list_1)} units!\tHe can have 100 units!'
            print(str)
        elif 100 > len(self.team_list_1) > 50:
            str = f'{self.hero_1} stay on level 3!\tHe has {len(self.team_list_1)} units!'
            print(str)
        else:
            str = f'{self.hero_1} on maximum level!\tHe has {len(self.team_list_1)} units!'
            print(str)

    def level_of_hero_2(self):
        '''Функция контролирующая уровень 2го героя'''
        if len(self.team_list_2) < 20:
            str = f'{self.hero_2} stay on level 1!\tHe has {len(self.team_list_2)} units!'
            print(str)
        elif len(self.team_list_2) == 20:
            str = f'{self.hero_2} has level 2!\tHe has {len(self.team_list_2)} units!!!\tHe can have 50 units!'
            print(str)
        elif 50 > len(self.team_list_2) > 20:
            str = f'{self.hero_2} stay on level 2!\tHe has {len(self.team_list_2)} units!'
            print(str)
        elif len(self.team_list_2) == 50:
            str = f'{self.hero_2} has level 3!\tHe has {len(self.team_list_2)} units!'
            print(str)
        elif 100 > len(self.team_list_2) > 50:
            str = f'{self.hero_2} stay on level 3!\tHe has {len(self.team_list_2)} units!'
            print(str)
        else:
            str = f'{self.hero_2} on maximum level!\tHe has {len(self.team_list_2)} units!'
            print(str)

class Round(Soldat, Hero):

    def __init__(self):
        pass

    def round_1(self):
        '''Первый раунд, герой могут иметь максимум 20 юнитов.
        Первый, кто наберет 20 юнитов, попеждает.'''
        print('\n\t\t\t\t\tRound 1\n')
        self.distribution_level_1()
        self.level_of_hero_1()
        self.level_of_hero_2()
        if len(self.team_list_1) > len(self.team_list_2):
            print(f'\n\t\t\t\t\t{self.hero_1} WON!!!')
        else:
            print(f'\n\t\t\t\t\t{self.hero_2} WON!!!')

    def round_2(self):
        '''Второй раунд, герои могут иметь максимум 50 юнитов.
        Первый, кто наберет 50 юнитов, побеждает'''
        print('\n\t\t\t\t\tRound 2\n')
        self.distribution_level_2()
        self.level_of_hero_1()
        self.level_of_hero_2()
        if len(self.team_list_1) > len(self.team_list_2):
            print(f'\n\t\t\t\t\t{self.hero_1} WON!!!')
        else:
            print(f'\n\t\t\t\t\t{self.hero_2} WON!!!')

    def round_3(self):
        '''Третий и последний раунд, герои могут иметь максимум 100 юнитов.
        Первый, кто наберет 100 юнитов, побеждает'''
        print('\n\t\t\t\t\tRound 3\n')
        self.distribution_level_3()
        self.level_of_hero_1()
        self.level_of_hero_2()
        if len(self.team_list_1) > len(self.team_list_2):
            print(f'\n\t\t\t\t\t{self.hero_1} WON!!!')
        else:
            print(f'\n\t\t\t\t\t{self.hero_2} WON!!!')
