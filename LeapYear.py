

# check if the entered year is leap or or not - here in this program   if it is printing 12.09 then leap year else not a leap  (this program is for Day of the programmer (09:12-(leap)| (09:13)-(non-leap) in Russia)
n = int(input())
if n>1918  and n<=2700:
    if (n%4 == 0):  # georgian calender
        if (n%100 == 0):
            if n%400 == 0:
                print('12.09.' + str(n).strip())
            else:
                print('13.09.' + str(n).strip())
        else:
            print('12.09.' + str(n).strip())
    else:
        print('13.09.' + str(n).strip())
elif n<1918:
    if n%4 == 0:    # julian calender
        print('12.09.'+str(n).strip())
        #print('Leap')
    else:
        print('13.09.' + str(n).strip())
else:
    print('26.09.'+str(n).strip())

#print(n%400, n%4, n%100)