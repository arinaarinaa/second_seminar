#Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
n = int(input())
result = []
vremennaya = 1
i = 0
for i in range(1, n+1):
    vremennaya *=i
    result.append(vremennaya)
print(result)
