
from pulp import *
import time
import numpy as np
start = time.time()

x1 = pulp.LpVariable("x1", lowBound=0,cat = 'Integer')
x2 = pulp.LpVariable("x2", lowBound=0,cat = 'Integer')
x3 = pulp.LpVariable("x3", lowBound=0,cat = 'Integer')
x4 = pulp.LpVariable("x4", lowBound=0,cat = 'Integer')
x5 = pulp.LpVariable("x5", lowBound=0, cat = 'Integer')
x6 = pulp.LpVariable("x6", lowBound=0, cat = 'Integer')

# всего 600
# 1 - 450  1                  450
# 2 - 290  2 + 4 = 6         1740
# 3 - 140  8+1 = 9 ; 140*9 = 1260
# проверочное значение 10 брусков - работает
# 1:6:9


print(" ")
print("3.1")
problem = pulp.LpProblem('0',pulp.LpMaximize)

problem += x4 ,"Целевая функция"

problem += 1*x1 + 0*x2 + 0*x3 - 1*x4 == 0,"1"
problem += 0*x1 + 2*x2 + 1*x3 - 6*x4 == 0, "2"
problem += 1*x1 + 0*x2 + 2*x3 - 9*x4 == 0, "3"
problem += 1*x1 + 1*x2 + 1*x3  <= 100, "4"


problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Целевая функция:")
print (abs(value(problem.objective)))
stop = time.time()

print(" ")
print("3.2")

problem = pulp.LpProblem('0',pulp.LpMinimize)
problem += 10*x1 + 20*x2 + 30*x3 ,"ostatok"

problem += 1*x1 + 0*x2 + 0*x3 - 1*x4 == 0,"1"
problem += 0*x1 + 2*x2 + 1*x3 - 6*x4 == 0, "2"
problem += 1*x1 + 0*x2 + 2*x3 - 9*x4 == 0, "3"
problem += 1*x1 + 1*x2 + 1*x3  == 100,"4"

problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Целевая функция:")
print (abs(value(problem.objective)))
stop = time.time()

#выясняем необходимое приращение
print("3.3")
print("3.3")
problem = pulp.LpProblem('0',pulp.LpMaximize)
buffer = []
for i in range(21):
    problem = pulp.LpProblem('0', pulp.LpMaximize)
    global bugger
    problem += 1*x1 + 1*x2 + 1*x3  , "целевая функция"
    problem += 1*x1 + 0*x2 + 0*x3 - 1*x4 == 0,"1"
    problem += 0*x1 + 2*x2 + 1*x3 - 6*x4 == 0, "2"
    problem += 1*x1 + 0*x2 + 2*x3 - 9*x4 == 0, "3"
    problem += 1*x4 ==i, "4"
    problem.solve()
    buffer.append(abs(value(problem.objective)))
print(buffer)
# при изменении параметра колмплектов, видим линейное приращение полуфабрикатов. на каждую ед. комплекта требуется 6 ед. полуфабриката.




