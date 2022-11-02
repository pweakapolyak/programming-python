# --------------------- Дерево решений  ---------------------

# Пример дерева решений и условия задачи представлены на сайте

# --------------------- Дерево решений ---------------------

def task():

    allow = "allow"
    refuse = "refuse"

    age = int(input('Возраст автовладельца: '))
    experience = int(input('Стаж в годах: '))
    auto_type = input('Тип автомобиля: ')
    is_accident_happened = int(input('Были ли аварии(1/0): ')) == 1
    place = input('Место эксплуатации: ')

    if age > 40:
        if place == "village":
            print(allow)
        elif experience > 10:
            print(allow)
        else:
            print(refuse)
    else:
        if not is_accident_happened:
            print(allow)
        elif auto_type == "sport":
            print(refuse)
        else:
            print(allow)


if __name__ == "__main__":
    task()
