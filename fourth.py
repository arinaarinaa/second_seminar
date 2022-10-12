#ДОП. задача на алгоритмы с реальных собеседований
#Даны два массива:
#[1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
#Надо вернуть их пересечение
#[1, 2, 2, 3]

array1 = [1,2,3,2,0]
array2 = [5,1,2,7,3,2]

resultarray = []
i = 0

for i in array2:
    for j in array1:
        if i==j:
            resultarray.append(i)
            break

print(resultarray)

