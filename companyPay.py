# calculating the users gross pay.

def companypay (hrs, hrly_pay):
    if hrs > 40:
        reg = hrs*hrly_pay
        otp = (hrs-40)*(hrly_pay*.5)
        fp = reg+otp
        print("Regular pay:",reg)
        print("Overtime pay:",otp)
    else:
        fp = hrs*hrly_pay
    print("Total pay: ",fp)
    return fp

hw = float(input("Enter hours worked: "))
hp = float(input("Enter hourly pay: "))

xp = companypay(hw,hp)
