class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self):
        print(complex(self.real, self.imaginary) + complex(self.real, self.imaginary))

    def __sub__(self):
        print(complex(self.real, self.imaginary) - complex(self.real, self.imaginary))

    def __mul__(self):
        print(complex(self.real, self.imaginary) * complex(self.real, self.imaginary))


    def __truediv__(self):
        print(complex(self.real, self.imaginary) / complex(self.real, self.imaginary))


    def mod(self):
        print(abs( complex(self.real, self.imaginary)))

a = Complex(2,1)
a.__add__()
a.__mul__()
a.__sub__()
a.mod()
a.__truediv__()

#######   NOT  ######  WORK  #######  SUKA  ###########  BLEAT ###########
