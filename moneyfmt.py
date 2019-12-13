class Moneyfmt:
    '''Create function dollarize() that takes Float and returns\
       dollarized format/'''
    def __init__(self, cach):
        self.cach = cach

    def update(self, cach):
        self.cach = cach

    def repr(self, cach):
        self.cach = cach
        self.cach = float(input('Enter your money: '))

    def str(self):
        if self.cach >= 0:
            return '${:,.2f}'.format(self.cach)
        else:
            return '-${:,.2f}'.format(-self.cach)
