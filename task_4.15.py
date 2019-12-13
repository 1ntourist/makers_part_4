from random import shuffle

class Cart(object):
    '''колода карт(52)'''

    carts = ['hA', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10',
            'hV', 'hD', 'hK', 'dA', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7',
            'd8', 'd9', 'd10', 'dV', 'dD', 'dK', 'cA', 'c2', 'c3', 'c4',
            'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'cV', 'cD', 'cK', 'sA','s2',
            's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10','sV', 'sD', 'sK']

    def decorator_print(func): #Декоратор
        def wrapper(str):
            print(func(str))
        return wrapper

    def init(self):
        pass

    @decorator_print
    def mix(self):   #Функция перемешивания
        shuffle(self.carts)
        str = 'Колода перемешана!!!'
        return str

    @decorator_print
    def distribution(self):    #Функция раздачи карты
        str = 'Вытащена случайная карта: ' + self.carts[0]
        return str

    @decorator_print
    def delete(self):
        del self.carts[0]
        str = f'Теперь в колоде {len(self.carts)} карт!!!'
        return str

c = Cart()
c.mix()
c.distribution()
c.delete()
