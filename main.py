import time

RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
END = '\u001b[0m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
BLACK = '\u001b[0;30m'

#Япония
k = 10

def Japan():
    for i in range(-2, 15 + 1 + 2): 
        if i == 3 or i == 12: 
            print(f'{WHITE}{"  " * (13 + k)}{RED}{"  " * (9)}{WHITE}{"  " * (13 + k)}{END}')
        elif i == 4 or i == 11:
            print(f'{WHITE}{"  " * (12 + k)}{RED}{"  " * (11)}{WHITE}{"  " * (12 + k)}{END}')
        elif i == 5 or i == 10:
            print(f'{WHITE}{"  " * (11 + k)}{RED}{"  " * (13)}{WHITE}{"  " * (11 + k)}{END}')
        elif 6 <= i <= 9:
            print(f'{WHITE}{"  " * (11 + k)}{RED}{"  " * (13)}{WHITE}{"  " * (11 + k)}{END}')
        else:
            print(f'{WHITE}{"  " * (35 + 2 * k)}{END}')

#Узор
def uzor():
    n = 4
    for j in range(1, n + 1):
        for i in range(0, 12):
            if i == 0 or i == 10:
                print(f'{WHITE}{"  " * 4}{BLUE}{"  " * 3}{WHITE}{"  " * 8}{BLUE}{"  " * 3}{WHITE}{"  " * 4}{END}')
            elif i == 1 or i == 9:
                print(f'{WHITE}{"  " * 3}{BLUE}{"  " * 2}{WHITE}{"  " * 1}{BLUE}{"  " * 2}{WHITE}{"  " * 6}{BLUE}{"  " * 2}{WHITE}{"  " * 1}{BLUE}{"  " * 2}{WHITE}{"  " * 3}{END}')
            elif i == 2 or i == 8:
                print(f'{WHITE}{"  " * 2}{BLUE}{"  " * 2}{WHITE}{"  " * 3}{BLUE}{"  " * 2}{WHITE}{"  " * 4}{BLUE}{"  " * 2}{WHITE}{"  " * 3}{BLUE}{"  " * 2}{WHITE}{"  " * 2}{END}')
            elif i == 3 or i == 7:
                print(f'{WHITE}{"  " * 1}{BLUE}{"  " * 2}{WHITE}{"  " * 5}{BLUE}{"  " * 2}{WHITE}{"  " * 2}{BLUE}{"  " * 2}{WHITE}{"  " * 5}{BLUE}{"  " * 2}{WHITE}{"  " * 1}{END}')
            elif i == 4 or i == 6:
                print(f'{BLUE}{"  " * 2}{WHITE}{"  " * 7}{BLUE}{"  " * 4}{WHITE}{"  " * 7}{BLUE}{"  " * 2}{END}')
            elif i == 5:
                print(f'{BLUE}{"  " * 1}{WHITE}{"  " * 9}{BLUE}{"  " * 2}{WHITE}{"  " * 9}{BLUE}{"  " * 1}{END}')

#График

def graph(): 
    s = ' '
    print('График функции', " " * 2, 'y=3*x')
    print()
    for i in range(0, 11):
        if i < 7:
            print(str(30 - 3 * i)," ",f'{WHITE}{"  " * (10 - i)}{GREEN}{"  " * 1}{WHITE}{"  " * i}{END}')
        else:
            print(str(30 - 3 * i),"  ",f'{WHITE}{"  " * (10 - i)}{GREEN}{"  " * 1}{WHITE}{"  " * i}{END}')
        s=s + str(i) + " "
    print(" " * 4, s)

#Диаграммма

def diag():
    file = open('sequence.txt', 'r')
    bolshe = 0
    menshe = 0
    for el in file:
        el = float(el)
        if el <= 0:
            if abs(el) < 5:
                bolshe += 1
            elif abs(el) != 5:
                menshe += 1
    per_b = int(bolshe * 100 / (bolshe + menshe))
    per_m = 100 - per_b
    file.close()

    for i in range(2): 
        if i == 0: 
            print('Больше -5:', f'{GREEN}{"  " * per_b}{END}', str(per_b) + '%')
        else: 
            print('Меньше -5:', f'{YELLOW}{"  " * per_m}{END}', str(per_m) + '%')

Japan()
print()
uzor()
print()
graph()
print()
diag()