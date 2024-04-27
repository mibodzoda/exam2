list = input().split()

min = list.index(min(list))
max = list.index(max(list))

list[min], list[max] = list[max], list[min]

print(list)