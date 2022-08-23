# Hometask_13_3
# Напишите функцию которая
# принимает на вход список
# целых чисел, удаляет из него
# все нечётные значения, а
# чётные нацело делит на два.
# In: 852 85 784 58
# Out: [426, 382, 29]
nums = [int(i) for i in input().split()]

def even(nums):


    a = []

    for i in nums:
        if i % 2 == 0:
            i = i / 2
            a.append(int(i))
    return a

# Hometask_13_3
# Напишите функцию которая
# принимает на вход список
# целых чисел, удаляет из него
# все нечётные значения, а
# чётные нацело делит на два.
# In: 852 85 784 58
# Out: [426, 382, 29]
nums = [int(i) for i in input().split()]

def even(nums):


    a = []

    for i in nums:
        if i % 2 == 0:
            i = i / 2
            a.append(int(i))
    return a


print(even(nums))