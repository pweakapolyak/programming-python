# --------------------- Конвертер памяти  ---------------------

# Пользователь вводит с клавиатуры количество байт
# Напечатать в одну строчку через пробел:
# 1) (Кол-во гигабайт)
# 2) (Кол-во мегабайт в оставшихся байтах)
# 3) (Количество килобайт в оставшихся байтах)
# 4) (Количество оставшихся байт)

# Пример, если ввести значение - 646039237 байт
# То выведется: "0 616 113 709"

# --------------------- Конвертер времени ---------------------

def task():
    bait = int(input('Введите кол-во байт: '))
    gb = bait//(2**30)
    mb = bait%(2**30)//(2**20)
    kb = ((bait%(2**30))-(mb*(2**20)))//1024
    baits = ((bait%(2**30))-(mb*(2**20)))%1024
    print(gb, mb, kb, baits)


if __name__ == "__main__":
    task()