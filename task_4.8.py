import moneyfmt

cach_user = moneyfmt.Moneyfmt(123456.78901)
print(cach_user.str())

cach_user.update(234567.345678)
print(cach_user.str())
