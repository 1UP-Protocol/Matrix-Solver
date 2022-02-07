import numpy
import sympy
import math
from functools import lru_cache

print("Enter the number of values (Variable coefficients and the result too)")
numbers = int(input())
dic0 = {}
dic1 = {}
dic2 = {}
dic3 = {}
dic4 = {}

fourtheq = False
fiftheq = False

print("Enter number of equations: ")
no_equations = int(input())

if no_equations == 5:
    fiftheq = True
elif no_equations == 4:
    fourtheq = True

while True:
    print("Enter the values of the variables: (Equation 1) ")
    list0 = list(map(int, input().split()))
    if len(list0) > numbers:
        print("Error: Entered more values than stated.\n")
        continue
    elif len(list0) < numbers:
        print("Error: Entered less values than stated.\n")
    else:
        break

for i in range(numbers):
    dic0[f"I{i}"] = list0[i]

while True:
    print("Enter the values of the variables: (Equation 2) ")
    list1 = list(map(int, input().split()))
    if len(list1) > numbers:
        print("Error: Entered more values than stated.\n")
        continue
    elif len(list1) < numbers:
        print("Error: Entered less values than stated.\n")
        continue
    else:
        break

for j in range(numbers):
    dic1[f"I{j}"] = list1[j]

while True:
    print("Enter the values of the variables: (Equation 3) ")
    list2 = list(map(int, input().split()))
    if len(list2) > numbers:
        print("Error: Entered more values than stated.\n")
        continue
    elif len(list2) < numbers:
        print("Error: Entered less values than stated.\n")
    else:
        break

for k in range(numbers):
    dic2[f"I{k}"] = list2[k]

if fourtheq:

    while True:
        print("Enter the values of the variables: (Equation 4) ")
        list3 = list(map(int, input().split()))
        if len(list3) > numbers:
            print("Error: Entered more values than stated.\n")
            continue
        elif len(list3) < numbers:
            print("Error: Entered less values than stated.\n")
            continue
        else:
            break

    for l in range(numbers):
        dic3[f"I{l}"] = list3[l]


if fiftheq:

    while True:
        print("Enter the values of the variables: (Equation 4) ")
        list3 = list(map(int, input().split()))
        for l in range(numbers):
            dic2[f"I{l}"] = list3[l]
        if len(list3) > numbers:
            print("Error: Entered more values than stated.\n")
            continue
        elif len(list3) < numbers:
            print("Error: Entered less values than stated.\n")
        else:
            break

    for l in range(numbers):
        dic3[f"I{l}"] = list3[l]

    while True:
        print("Enter the values of the variables: (Equation 5) ")
        list4 = list(map(int, input().split()))
        for m in range(numbers):
            dic2[f"I{m}"] = list4[m]
        if len(list4) > numbers:
            print("Error: Entered more values than stated.\n")
            continue
        elif len(list4) < numbers:
            print("Error: Entered less values than stated.\n")
        else:
            break
    for m in range(numbers):
        dic3[f"I{m}"] = list4[m]

if fiftheq:

    if numbers == 3:
        M = sympy.Matrix([[dic0["I0"], dic0["I1"], dic0["I2"]], [dic1["I0"], dic1["I1"], dic1["I2"]],
                          [dic2["I0"], dic2["I1"], dic2["I2"]], [dic3["I0"], dic3["I1"], dic3["I2"]],
                          [dic4["I0"], dic4["I1"], dic4["I2"]]])
        print(M.rref())

    elif numbers == 4:
        M = sympy.Matrix(
            [[dic0["I0"], dic0["I1"], dic0["I2"], dic0["I3"]], [dic1["I0"], dic1["I1"], dic1["I2"], dic1["I3"]],
             [dic2["I0"], dic2["I1"], dic2["I2"], dic2["I3"]], [dic3["I0"], dic3["I1"], dic3["I2"], dic3["I3"]],
             [dic4["I0"], dic4["I1"], dic4["I2"], dic4["I3"]]])
        print(M.rref())

    elif numbers == 5:
        M = sympy.Matrix([[dic0["I0"], dic0["I1"], dic0["I2"], dic0["I3"], dic0["I4"]],
                          [dic1["I0"], dic1["I1"], dic1["I2"], dic1["I3"], dic1["I4"]],
                          [dic2["I0"], dic2["I1"], dic2["I2"], dic2["I3"], dic2["I4"]],
                          [dic3["I0"], dic3["I1"], dic3["I2"], dic3["I3"], dic3["I4"]],
                          [dic4["I0"], dic4["I1"], dic4["I2"], dic4["I3"], dic4["I4"]]])
        print(M.rref())

elif fourtheq:

    if numbers == 3:
        M = sympy.Matrix([[dic0["I0"], dic0["I1"], dic0["I2"]], [dic1["I0"], dic1["I1"], dic1["I2"]],
                          [dic2["I0"], dic2["I1"], dic2["I2"]], [dic3["I0"], dic3["I1"], dic3["I2"]]])
        print(M.rref())

    elif numbers == 4:
        M = sympy.Matrix(
            [[dic0["I0"], dic0["I1"], dic0["I2"], dic0["I3"]], [dic1["I0"], dic1["I1"], dic1["I2"], dic1["I3"]],
             [dic2["I0"], dic2["I1"], dic2["I2"], dic2["I3"], [dic3["I0"], dic3["I1"], dic3["I2"], dic3["I3"]]]])
        print(M.rref())

    elif numbers == 5:
        M = sympy.Matrix([[dic0["I0"], dic0["I1"], dic0["I2"], dic0["I3"], dic0["I4"]],
                          [dic1["I0"], dic1["I1"], dic1["I2"], dic1["I3"], dic1["I4"]],
                          [dic2["I0"], dic2["I1"], dic2["I2"], dic2["I3"], dic2["I4"]],
                          [dic3["I0"], dic3["I1"], dic3["I2"], dic3["I3"], dic3["I4"]]])
        print(M.rref())

else:

    if numbers == 3:
        M = sympy.Matrix([[dic0["I0"], dic0["I1"], dic0["I2"]], [dic1["I0"], dic1["I1"], dic1["I2"]],
                          [dic2["I0"], dic2["I1"], dic2["I2"]]])
        print(M.rref())

    elif numbers == 4:
        M = sympy.Matrix(
            [[dic0["I0"], dic0["I1"], dic0["I2"], dic0["I3"]], [dic1["I0"], dic1["I1"], dic1["I2"], dic1["I3"]],
             [dic2["I0"], dic2["I1"], dic2["I2"], dic2["I3"]]])
        print(M.rref())

    elif numbers == 5:
        M = sympy.Matrix([[dic0["I0"], dic0["I1"], dic0["I2"], dic0["I3"], dic0["I4"]],
                          [dic1["I0"], dic1["I1"], dic1["I2"], dic1["I3"], dic1["I4"]],
                          [dic2["I0"], dic2["I1"], dic2["I2"], dic2["I3"], dic2["I4"]]])
        print(M.rref())


