import matplotlib as plt

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1


# des - descritisation
# Sv - ресурс
# Xv - возможные варианиты распределения ресурса
# fResidualA() - функция остатка
# profitA() - функция профита
# Smin, Smax - возможный диапазон распределения ресурса на этапе в зависимости от функции остатка

mainResouce = 140

# словарь для мемоизации
cache = {}

des = 8

discretS = des
discretX = des

mass1Q = []
mass2Q = []
mass3Q = []
mass4Q = []

mass1X = []
mass2X = []
mass3X = []
mass4X = []

mass1I = []
mass2I = []
mass3I = []
mass4I = []

Wmaxs1 = []
Wmaxs2 = []
Wmaxs3 = []
Wmaxs4 = []

def profitA(x):
    print("Profit a x:")
    print(x)
    return (90 + 1.4*(pow(x,3/4)))

def profitB(x):
    print("Profit b x:")
    print(x)
    return (110 + 0.7*(pow(x,3/4)))

def fResidualA(period,localRes):
    return pow(0.95,period)*localRes

def fResidualB(period,localRes):
    return pow(0.77,period)*localRes


def termFunc(Sv):
    print("after test start term")
    print(Sv)
    Smin = fResidualB(3,mainResouce)
    Smax = fResidualA(3,mainResouce)
    Sdistance = np.linspace(Smin, Smax, discretS)
    print("Smin" + str(Smin))
    print("Smax" + str(Smax))

    Xmaxs = []
    IintoX = []
    print("SDis" + str(Sdistance))

    AllW = []
    Wmax = []

    for i in Sdistance:
        Xv = np.linspace(0, i, discretX)
        for x in Xv:

            # главный кеш мемоизации
            global cache
            if ((4, Sv) in cache):
                print("терминальный кеш от средств "+str(Sv))
                return cache[4, Sv]

            profitAx = profitA(x)
            profitBx = profitB(i - x)

            if ((profitAx >= 0) and (profitBx >= 0)):
                AllW.append(profitAx+profitBx)
            else:
                AllW.append(0)
        plt.figure(4)
        plt.plot(Xv, AllW)
        Wmax.append(round(max(AllW), 2))
        Xmax = Xv[AllW.index(max(AllW))]
        Xmaxs.append(round(Xmax, 2))
        IintoX.append(i)
        global mass4X
        global mass4I
        global mass4Q
        mass4Q = max(Wmax[:])
        mass4I = IintoX[:]
        mass4X = Xmaxs[:]
        AllW = []
    global Wmaxs4
    Wmaxs4.append(max(Wmax))
    cache[4, Sv] = max(Wmaxs4[:])
    print("Term before func result")
    print(Wmax)
    print("return term Wmax" + str(max(Wmax)))
    return cache[4,Sv]

def mainF(n,Sv):
    if(n==4):
        if (Sv <= 0.0):
            return 0
        print(Sv)

        Sv = round(Sv, 4)
        print("start main function quarter " + str(n))

        result = termFunc(Sv)
        print("start mainF 4")
        print(result)
        return result
    else:
            if (Sv <= 0.0):
                return 0
            global cache
            print("start main function quarter " + str(n))
            AllW = []
            Wmax = []
            Xmaxs = []
            IintoX = []
            if(n==1):
                Sv = round(Sv, 4)
                # на первом этапе мы можем вложить в первый цех от 1 до 140 без функции остатка, так как 140 это уже условный остаток
                Smin = 0
                Smax = 140
                Sdistance = np.linspace(Smin, Smax, discretS)
            else:
                Sv = round(Sv, 4)
                # расчет возможных вкладов в следующий этап
                Smin = fResidualB(n-1, mainResouce)
                Smax = fResidualA(n-1, mainResouce)
                Sdistance = np.linspace(Smin, Smax, discretS)
            print("Smax " + str(Smax))
            print("Smin " + str(Smin))
            print("Sdis " + str(Sdistance))


            for i in Sdistance:
                # мы можем вложить в первый цех x средств от 0 до i, во второй i-x средств
                Xv = np.linspace(0, i, discretX)
                for x in Xv:

                    # МЕМОИЗАЦИЯ
                    print("Test before cache")
                    if (((n,Sv) in cache) and n!=1):
                        return cache[n, Sv]
                    #####КОНЕЦ МЕМОИЗАЦИИ######
                    else:

                        profitAx = profitA(x)
                        profitBx = profitB(i-x)

                        if((profitAx>=0) and (profitBx>=0)):
                            if(n==1):
                                resudualA = fResidualA(n , x)
                                resudualB = fResidualB(n , i - x)
                                resultResidual = resudualA + resudualB
                            else:
                                resudualA = fResidualA(n-1, x)
                                resudualB = fResidualB(n-1, i - x)
                                resultResidual = resudualA + resudualB
                            # тут мы считаем профит на этапе + отдаем на след. этап остаточные средства после этого этапа.
                            # поэтому здесь сначала считаются профиты от средст, пришедших с этапа раньше, а затем остатки этих средств после периода
                            AllW.append(round((profitAx + profitBx + mainF(n+1,resultResidual)),3))
                        else:
                            print("NEGATIVE PROFIT ON STEP " + str(n))
                            # если один из цехов отдает отрицательный доход, то мы обнуляем весь доход.
                            AllW.append(0)

                #внутри for i (Для каждого возможного вложения в следующий этап (Sdistance) пробегаемся по возможным вкладам x  в первый цех от 0 до (i))

                #Рисуем графики для каждого этапа
                if(n==1):
                    plt.figure(n)
                    plt.plot(Xv,AllW)
                if (n == 2):
                    plt.figure(n)
                    plt1.plot(Xv, AllW)
                if (n == 3):
                    plt.figure(n)
                    plt.plot(Xv, AllW)

                Wmax.append(round(max(AllW), 2))

                # из всех Доходов выбираем максимальный, фиксируем при нем икс
                #  тут подвох в том, что максимум может быть не один , их может быть 2 и они могут быть равны
                Xmax = Xv[AllW.index(max(AllW))]
                # Xmax = Xv[lastIndexWmax(max(AllW),AllW)]

                IintoX.append(i)
                # добавляем этот xmax в массив максимумов
                Xmaxs.append(round(Xmax, 2))

                # Буфер значений для графики
                if (n == 1):
                    global mass1X
                    global mass1I
                    global mass1Q
                    # идея взять индекс максимаму Wmax и по нему получить x, так как количество Wmax соотносится с X
                    mass1Q = max(Wmax[:])
                    # mass1I = IintoX[:]
                    mass1I.append(i)
                    mass1X = Xmaxs[:]
                if (n == 2):
                    global mass2X
                    global mass2I
                    global mass2Q
                    mass2Q = max(Wmax[:])
                    mass2I = IintoX[:]
                    mass2X = Xmaxs[:]
                if (n == 3):
                    global mass3X
                    global mass3I
                    global mass3Q
                    mass3Q = max(Wmax[:])
                    mass3I = IintoX[:]
                    mass3X = Xmaxs[:]
                # обнуляем все доходы на возможном этапе i in Sdist
                AllW = []

            if(n==1):
                global  Wmaxs1
                Wmaxs1.append(max(Wmax))
                cache[n, Sv] = max(Wmaxs1[:])
            if (n == 2):
                global Wmaxs2
                Wmaxs2.append(max(Wmax))
                cache[n, Sv] = max(Wmaxs2[:])
            if (n == 3):
                global Wmaxs3
                Wmaxs3.append(max(Wmax))
                cache[n, Sv] = max(Wmaxs3[:])

            print("RETURN MAIN F QUARTER " + str(n))
            # для отрисовки всех возможных этапов на 1 графике
            if(n == 1):
                print("")
            elif(n==2):
                return max(Wmaxs2)
            elif(n == 3):
                return max(Wmaxs3)


mainF(1,mainResouce)

print("X")
print(mass1X)
print("I")
print(mass1I)
print("Q")
print(mass1Q)
print("_____")
print(mass2X)
print(mass2I)
print(mass2Q)
print("_____")
print(mass3X)
print(mass3I)
print(mass3Q)
print("_____")
print(mass4X)
print(mass4I)
print(mass4Q)

print("_____")
print(max(Wmaxs1))
print(max(Wmaxs2))
print(max(Wmaxs3))
print(max(Wmaxs4))

plt.xlabel('X')
plt.ylabel('W')

plt.show()


plt1.show()



