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
    num_of_bytes_in_kb = 1024
    num_of_kb_in_mb = 1024
    num_of_mb_in_gb = 1024

    num_of_bytes_in_gb = num_of_mb_in_gb * num_of_kb_in_mb * num_of_bytes_in_kb
    num_of_bytes_in_mb = num_of_kb_in_mb * num_of_bytes_in_kb

    full_bytes = int(input('Enter num of bytes: '))

    num_gb = full_bytes // num_of_bytes_in_gb
    remaining_bytes = full_bytes % num_of_bytes_in_gb

    num_mb = remaining_bytes // num_of_bytes_in_mb
    remaining_bytes = remaining_bytes % num_of_bytes_in_mb

    num_kb = remaining_bytes // num_of_bytes_in_kb
    remaining_bytes = remaining_bytes % num_of_bytes_in_kb

    print(num_gb, num_mb, num_kb, remaining_bytes)


if __name__ == "__main__":
    task()