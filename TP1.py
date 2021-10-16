# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#jogo dos 21 fósforos
import random
k = str("s")
while k in "Ss":
    f = 21
    v = 0
    j = int(input("Escolha a posição em que quer começar a jogar 1 ou 2."))
    while j != 1 and j != 2:
        j = int(input("Escolha a posição em que quer começar a jogar 1 ou 2."))
    while f != 1:
        if j == 1:
            a = int(input("Digite o número de fósforos que deseja retirar de 1 a 4."))
            while a != 1 and a != 2 and a != 3 and a != 4:
                a = int(input("Digite o número de fósforos que deseja retirar de 1 a 4."))
            if a == 1:
                b = 4
            if a == 2:
                b = 3
            if a == 3:
                b = 2
            if a == 4:
                b = 1
            print (f"Eu retirei {b} fósforos. Ainda exitem {f-a-b}.")
            f = f-a-b
        if f == 1:
            print ("Ganhei pois ficaste com o último fósforo.")
        if j == 2:
            while v == 0:
                l = [1,2,3,4]
                b = random.choice(l)
                print (f"Eu retirei {b} fósforos. Ainda exitem {f-b}.")
                f = f - b
                a = int(input("Digite o número de fósforos que deseja retirar de 1 a 4."))
                while a != 1 and a != 2 and a != 3 and a != 4:
                    a = int(input("Digite o número de fósforos que deseja retirar de 1 a 4."))
                print (f"Tu retiraste {a} fósforos. Ainda exitem {f-a}.")
                f = f - a
                if (a+b) > 5:
                    c = 10 - b - a
                    print (f"Eu retirei {c} fósforos. Ainda exitem {f-c}.")
                if (a+b) < 5:
                    c = 5 - b - a
                    print (f"Eu retirei {c} fósforos. Ainda exitem {f-c}.")
                if (a+b) == 5:
                    c = random.choice(l)
                    print (f"Eu retirei {c} fósforos. Ainda exitem {f-c}.")
                f = f - c
                v = 1
            a = int(input("Digite o número de fósforos que deseja retirar de 1 a 4."))
            while a != 1 and a != 2 and a != 3 and a != 4:
                a = int(input("Digite o número de fósforos que deseja retirar de 1 a 4."))
            if a == 1:
                b = 4
            if a == 2:
                b = 3
            if a == 3:
                b = 2
            if a == 4:
                b = 1
            print (f"Tu retiraste {a} fósforos. Ainda exitem {f-a}.")
            f = f - a
            if f == 1 :
                print ("Muitos parabéns ganhaste eu fiquei com o último fósforo.")
                break
            print (f"Eu retirei {b} fósforos. Ainda exitem {f-b}.")
            f = f - b
            if f == 1 :
                print ("Ganhei pois ficaste com o último fósforo.")
                break
    k = str(input("Desejas jogar novamente? [S/N]"))
    while k not in "SsNn":
        k = str(input("Desejas jogar novamente? [S/N]"))
    if k in "Nn":
        break



