
h = int(input())
t = int(input())


num2words1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
num2words2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def number(Number):
    if 1 <= Number < 19:
        return num2words1[Number]
    elif 20 <= Number <= 99:
        tens, below_ten = divmod(Number, 10)
        if below_ten == 0:
            return num2words2[tens - 2]
        else:
            return num2words2[tens - 2] + ' ' + num2words1[below_ten]
    else:
        pass

if t == 0:
    hour = number(h)
    print("{0}:00 O' clock".format(hour))
elif t == 15:
    r1 = number(h)
    print("quarter past {0}".format(r1))
elif t == 30:
    r1 = number(h)
    print("half past {0}".format(r1))
elif t == 45:
    r1 = number(h+1)
    print("quarter to {0}".format(r1))
elif (t>0 and t<15) or (t>15 and t<30):
    hour = number(h)
    minute = number(t)
    if t == 1:
        print("{0} minute past {1}".format(minute, hour))
    else:
        print("{0} minutes past {1}".format(minute, hour))
elif (t>30 and t<45) or (t>45 and t<60):
    hour = number(h+1)
    minute = number(60-t)
    print("{0} minutes to {1}".format(minute, hour))


# input
# 6
# 35

# output
# twenty five minutes to seven