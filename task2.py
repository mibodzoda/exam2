def squares(N):
    i = 1
    while i ** 2 < N:
        print(i ** 2)
        i += 1
a = int(input())
squares(a)