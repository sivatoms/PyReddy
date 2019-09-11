


import re
def print_formatted(number):
    bl = len('{0:b}'.format(n))
    # your code goes here
    for i in range(0,n):
        #print(len(str(bin(i + 1))))
        #print("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=bl))
        dec = i+1
        ocn = re.sub(r'0o','',str(oct(i+1)))
        hen = re.sub(r'0x','',str(hex(i+1)))



        binn = re.sub(r'0b','',str(bin(i+1)))
        d = '{0: >{w}}'.format(dec, w = bl)

        o = '{0: >{w}}'.format(ocn, w = bl)
        h = '{0: >{w}}'.format(hen, w = bl)

        b = '{0: >{w}}'.format(binn, binn, w = bl)
        print(d,o,h.upper(),b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)