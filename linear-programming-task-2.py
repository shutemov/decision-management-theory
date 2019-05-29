
from pulp import *
import time
import numpy as np
start = time.time()

x1 = pulp.LpVariable("x1", lowBound=0,cat = 'Integer')
x2 = pulp.LpVariable("x2", lowBound=0,cat = 'Integer')
x3 = pulp.LpVariable("x3", lowBound=0,cat = 'Integer')
x4 = pulp.LpVariable("x4", lowBound=0,cat = 'Integer')
x5 = pulp.LpVariable("x5", lowBound=0, cat = 'Integer')

# # 2.1
print("2.1")
problem = pulp.LpProblem('0',pulp.LpMaximize)

problem += 1000*x1  + 500*x2  +1100*x3 + 900*x4 + 1000*x5 , "Функция цели"
problem += 56*x1 + 25*x2 +53*x3+40*x4+46*x5 <= 559.2675,"1"

problem += 12*x1 + 30*x2 + 10*x3 + 24*x4 + 19*x5 <= 290, "2"


problem.solve()
print ("Результат (кол. определенного типа оборудования):")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Целевая функция:")
print (abs(value(problem.objective)))
stop = time.time()
print ("Время :")
print(stop - start)

# исследование 2.2.1
# при бесконечных средствах получаем оптимальный выбор = 29 ед 3 типа
# максимальный 29*53 = 1537 точка влияния на оптимальный выбор, меньше - не эффективно , больше - не выгодно
problem = pulp.LpProblem('0',pulp.LpMaximize)

problem += 1000*x1  + 500*x2  +1100*x3 + 900*x4 + 1000*x5 , "Функция цели"
problem += 56*x1 + 25*x2 +53*x3+40*x4+46*x5 <= 1537,"1"
problem += 12*x1 + 30*x2 + 10*x3 + 24*x4 + 19*x5 <= 290, "2"


problem.solve()
print ("")
print ("Результат (кол. определенного типа оборудования):")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Целевая функция:")
print (abs(value(problem.objective)))
stop = time.time()
print ("Время :")
print(stop - start)

# исследование 2.2.2
print("2.2.2")
print ("")
print ("результат")
test = []
for i in range(1537):
    problem = pulp.LpProblem('0', pulp.LpMaximize)
    problem += 1000 * x1 + 500 * x2 + 1100 * x3 + 900 * x4 + 1000 * x5, "Функция цели"
    problem += 56 * x1 + 25 * x2 + 53 * x3 + 40 * x4 + 46 * x5 <= i, "1"  # 86 - Значение
    problem += 12 * x1 + 30 * x2 + 10 * x3 + 24 * x4 + 19 * x5 <= 290, "2"
    problem.solve()
    buffer = problem.variables()[:]

    if(problem.variables()[0].varValue!=0 and problem.variables()[1].varValue==0 and problem.variables()[2].varValue==0 and problem.variables()[3].varValue==0 and problem.variables()[4].varValue==0):
        continue
    elif(problem.variables()[0].varValue==0 and problem.variables()[1].varValue!=0 and problem.variables()[2].varValue==0 and problem.variables()[3].varValue==0 and problem.variables()[4].varValue==0):
        continue
    elif(problem.variables()[0].varValue==0 and problem.variables()[1].varValue==0 and problem.variables()[2].varValue!=0 and problem.variables()[3].varValue==0 and problem.variables()[4].varValue==0):
        continue
    elif(problem.variables()[0].varValue==0 and problem.variables()[1].varValue==0 and problem.variables()[2].varValue==0 and problem.variables()[3].varValue!=0 and problem.variables()[4].varValue==0):
        continue
    elif(problem.variables()[0].varValue==0 and problem.variables()[1].varValue==0 and problem.variables()[2].varValue==0 and problem.variables()[3].varValue==0 and problem.variables()[4].varValue!=0):
        continue
    elif(problem.variables()[0].varValue==0 and problem.variables()[1].varValue==0 and problem.variables()[2].varValue==0 and problem.variables()[3].varValue==0 and problem.variables()[4].varValue==0):
        continue
    else:
        test.append(i)

print("COST")
print(test)






