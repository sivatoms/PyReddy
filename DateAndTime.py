from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    dt1 = dt.strptime(t1, "%a %d %b %Y %H:%M:%S %z")  # % a - Sun  %d day number    %b  month short  %Y full year  %z UTC time (-7000)
    dt2 = dt.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    print(int((dt1 - dt2).total_seconds()))

    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        time_delta(t1, t2)

#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 -0000
#Sat 02 May 2015 19:54:36 +0530
#Fri 01 May 2015 13:54:36 -0000

t = dt.strptime(input(),"%m %d %Y")
print(dt.strptime(t.weekday()))


# input 08 05 2019
t = dt.strptime(input(), "%m %d %Y")
#print(t)
print(t.strftime("%A"))   # %A prints weekday name   using strftime()




##  Convert 12 hour format to 24 hour
m2 = input()
in_time = dt.strptime(m2, "%I:%M:%S%p")
out_time = dt.strftime(in_time, "%H:%M:%S")
print(out_time)
