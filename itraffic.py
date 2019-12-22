from time import sleep
from random import randrange
print()
print('\033[7;31m                                         \033[m')
print('\033[7m        Intelligent Light Traffic        \033[m')
print('\033[7;32m                                         \033[m')
print()
rua1 = randrange(0, 20)
rua2 = randrange(0, 20)
rua3 = randrange(0, 20)
rua4 = randrange(0, 20)
while True:
    if rua1 > rua2 and rua1 > rua3 and rua1 > rua4:
        print('\033[7;32mRua 1\033[m')
        print('\033[7;31mRua 2\033[m')
        print('\033[7;31mRua 3\033[m')
        print('\033[7;31mRua 4\033[m')
        print(rua1, 'carros na fila, aguarde', rua1, 'segundos')
        sleep(rua1)
        rua1 = randrange(0, 20)
    else:
        if rua2 > rua1 and rua2 > rua3 and rua2 > rua4:
            print('\033[7;31mRua 1\033[m')
            print('\033[7;32mRua 2\033[m')
            print('\033[7;31mRua 3\033[m')
            print('\033[7;31mRua 4\033[m')
            print(rua2, 'carros na fila, aguarde', rua2, 'segundos')
            sleep(rua2)
            rua2 = randrange(0, 20)
        else:
            if rua3 > rua1 and rua3 > rua2 and rua3 > rua4:
                print('\033[7;31mRua 1\033[m')
                print('\033[7;31mRua 2\033[m')
                print('\033[7;32mRua 3\033[m')
                print('\033[7;31mRua 4\033[m')
                print(rua3, 'carros na fila, aguarde', rua3, 'segundos')
                sleep(rua3)
                rua3 = randrange(0, 20)
            else:
                if rua4 > rua1 and rua4 > rua3 and rua4 > rua2:
                    print('\033[7;31mRua 1\033[m')
                    print('\033[7;31mRua 2\033[m')
                    print('\033[7;31mRua 3\033[m')
                    print('\033[7;32mRua 4\033[m')
                    print(rua4, 'carros na fila, aguarde', rua4, 'segundos')
                    sleep(rua4)
                    rua4 = randrange(0, 20)
