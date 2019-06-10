#!/usr/bin/python
import sys
import re
import math

def myprint(nbs, eqt):
    print('Reduced form: '),
    for i in range(len(nbs)):
        if i == 0:
            print(str(nbs[i]) + ' * X^0'),
        elif i > 0 and nbs[i] < 0:
            print('- ' + str(-nbs[i]) + ' * X^' + str(eqt[i])),
        elif i > 0 and nbs[i] >= 0:
            print('+ ' + str(nbs[i]) + ' * X^' + str(eqt[i])),
    print('= 0\nPolynomial degree: ' + str(eqt[-1]))

def count(nbs, eqt):
    myprint(nbs, eqt)
    if (len(nbs) > 3):
        print('The polynomial degree is stricly greater than 2, I can\'t solve.')
        exit()
    elif len(nbs) <= 3:
        while len(nbs) < 3:
            nbs.append(0)
        if nbs[0] == 0 and nbs[1] == 0 and nbs[2] == 0:
            print('All the real numbers are solution...')
            exit()
        elif nbs[1] == 0 and nbs[2] == 0:
            print('Equation is not solvable!')
            exit()
        elif nbs[2] == 0:
            print('The solution is:')
            print(-nbs[0] / nbs[1])
            exit()
        D = nbs[1] * nbs[1] - 4 * nbs[2] * nbs[0]
        if D == 0:
            print('Discriminant is equal to 0, so the solution is:')
            print(-nbs[1] / 2 / nbs[2])
        elif D > 0:
            print('Discriminant is strictly positive, the two solutions are:')
            print((-nbs[1] + math.sqrt(D)) / 2 / nbs[2])
            print((-nbs[1] - math.sqrt(D)) / 2 / nbs[2])
        elif D < 0:
            print('Discriminant is strictly negative, the two solutions are:')
            print(str(-nbs[1] / 2 / nbs[2]) +' + i * ' + str(math.sqrt(-D) / 2 / nbs[2]))
            print(str(-nbs[1] / 2 / nbs[2]) +' - i * ' + str(math.sqrt(-D) / 2 / nbs[2]))


            
def parse2(nbs, eqt):
    nbs1 = []
    eqt1 = []
    for e in range(max(eqt)+1):
        eqt1.append(e)
        nbs1.append(0)
        for i in range(len(eqt)):
            if e == eqt[i]:
                nbs1[e] += nbs[i]
    while nbs1[-1] == 0:
        nbs1.pop()
        eqt1.pop()
    count(nbs1, eqt1)

def parse(inp):
    nbs = []
    eqt = []
    index_of_eqw = inp.index("=")
    for i in range(len(inp)):
        if (i + 4) % 4 == 0:
            try:
                nbs.append(int(inp[i]))
            except:
                try:
                    nbs.append(float(inp[i]))
                except:
                    print('Wrong format of data!')
                    exit()
            if (i > 0 and inp[i - 1] == '-' and i < index_of_eqw) or \
                (i > 0 and (inp[i - 1] == '+' or inp[i - 1] == '=') and i > index_of_eqw):
                nbs[len(nbs) - 1] *= -1
        elif (i + 2) % 4 == 0:
           eqt.append(int(inp[i][2]))
    parse2(nbs, eqt)



def main():
    inp = 0
    if len(sys.argv) > 1:
        inp = sys.argv[1]
    else:
        while (inp == 0):
            try:
                inp = str(input('Please, enter equation with \'\': ' ))
            except:
                pass
    inp = inp.split(' ')
    parse(inp)

if __name__ == "__main__":
    main()
    
    