import time


RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
END = '\u001b[0m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
BLACK = '\u001b[0;30m'
k = 10


def draw_japan():
    str3 = f'{WHITE}{"  " * (13 + k)}{END}'
    str4 = f'{WHITE}{"  " * (12 + k)}{END}'
    str5 = f'{WHITE}{"  " * (11 + k)}{END}'
    str6 = f'{WHITE}{"  " * (11 + k)}{END}'
    for i in range(-2, 15 + 1 + 2): 
        if i == 3 or i == 12: 
            print(f'{WHITE}{"  " * (13 + k)}{RED}{"  " * (9)}{str3}')
        elif i == 4 or i == 11:
            print(f'{WHITE}{"  " * (12 + k)}{RED}{"  " * (11)}{str4}')
        elif i == 5 or i == 10:
            print(f'{WHITE}{"  " * (11 + k)}{RED}{"  " * (13)}{str5}')
        elif 6 <= i <= 9:
            print(f'{WHITE}{"  " * (11 + k)}{RED}{"  " * (13)}{str6}')
        else:
            print(f'{WHITE}{"  " * (35 + 2 * k)}{END}')
        time.sleep(0.01)


def uzor():
    k = 4 # кол-во повторений
    str0 = f'{BLUE}{"  " * 3}{WHITE}{"  " * 4}{END}'
    str0_1 = f'{WHITE}{"  " * 8}{str0}'
    str1_1 = f'{BLUE}{"  " * 2}{WHITE}{"  " * 6}{BLUE}{"  " * 2}'
    str1_2 = f'{WHITE}{"  " * 1}{BLUE}{"  " * 2}{WHITE}{"  " * 3}{END}'
    str1_3 = f'{WHITE}{"  " * 1}{str1_1}{str1_2}'
    str2_1 = f'{BLUE}{"  " * 2}{WHITE}{"  " * 4}{BLUE}{"  " * 2}'
    str2_2 = f'{WHITE}{"  " * 3}{BLUE}{"  " * 2}{WHITE}{"  " * 2}{END}'
    str2_3 = f'{WHITE}{"  " * 3}{str2_1}{str2_2}'
    str3_1 = f'{BLUE}{"  " * 2}{WHITE}{"  " * 2}{BLUE}{"  " * 2}'
    str3_2 = f'{WHITE}{"  " * 5}{BLUE}{"  " * 2}{WHITE}{"  " * 1}{END}'
    str3_3 = f'{WHITE}{"  " * 5}{str3_1}{str3_2}'
    str4_1 = f'{WHITE}{"  " * 7}{BLUE}{"  " * 2}{END}'
    str4_2 = f'{BLUE}{"  " * 4}{str4_1}'
    str5_1 = f'{WHITE}{"  " * 9}{BLUE}{"  " * 1}{END}'
    str5_2 = f'{BLUE}{"  " * 2}{str5_1}'
    for j in range(1, k + 1):
        for i in range(0, 12):
            if i == 0 or i == 10:
                print(f'{WHITE}{"  " * 4}{BLUE}{"  " * 3}{str0_1}')
            elif i == 1 or i == 9:
                print(f'{WHITE}{"  " * 3}{BLUE}{"  " * 2}{str1_3}')
            elif i == 2 or i == 8:
                print(f'{WHITE}{"  " * 2}{BLUE}{"  " * 2}{str2_3}')
            elif i == 3 or i == 7:
                print(f'{WHITE}{"  " * 1}{BLUE}{"  " * 2}{str3_3}')
            elif i == 4 or i == 6:
                print(f'{BLUE}{"  " * 2}{WHITE}{"  " * 7}{str4_2}')
            elif i == 5:
                print(f'{BLUE}{"  " * 1}{WHITE}{"  " * 9}{str5_2}')
            time.sleep(0.01)


def graph(): 
    s = ' '
    print('График функции', " " * 2, 'y = 3 * x')
    print()
    
    for i in range(0, 11):
        str7 = f'{GREEN}{"  " * 1}{WHITE}{"  " * i}{END}'
        str8 = f'{GREEN}{"  " * 1}{WHITE}{"  " * i}{END}'
        if i < 7:
            print(str(30 - 3 * i)," ",f'{WHITE}{"  " * (10 - i)}{str7}')
        else:
            print(str(30 - 3 * i),"  ",f'{WHITE}{"  " * (10 - i)}{str8}')
        s = s + str(i) + " "
    print(" " * 4, s)


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

    s1 = str(per_b) + '%'
    s2 = str(per_m) + '%'
    for i in range(2): 
        if i == 0: 
            print('Больше -5:', f'{GREEN}{"  " * per_b}{END}', s1)
        else: 
            print('Меньше -5:', f'{YELLOW}{"  " * per_m}{END}',s2 )

draw_japan()
print()
uzor()
print()
graph()
print()
diag()