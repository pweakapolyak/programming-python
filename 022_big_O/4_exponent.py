


def hanoi(n, fr, to, spare):
    if n == 1:
        print('From', fr, 'To', to)
    else:
        hanoi(n-1, fr, spare, to)
        hanoi(1, fr, to, spare)
        hanoi(n-1, spare, to, fr)


hanoi(60, 'P1', 'P3', 'P2')