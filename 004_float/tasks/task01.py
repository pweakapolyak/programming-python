# --------------------- Отнсоительность расстояний  ---------------------

# условия задачи описаны в уроке

# --------------------- Отнсоительность расстояний ---------------------

def task():
    import math
    l0 = float(input('Введите l0: '))
    v = float(input('Ведите v: '))
    c = 299792458
    l = l0 * math.sqrt(1-(v**2)/(c**2))
    print(round(l, 8))


if __name__ == "__main__":
    task()
