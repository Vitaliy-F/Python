# EX2
number = input("Введіть числа ")
list=[]
for num in number:
    list.append(int(num))
num=sorted(list)
print("Найменше число", num[0])
print("Найбільше число", num[-1])