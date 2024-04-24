# --------------------- Дерево решений  ---------------------

# Пример дерева решений и условия задачи представлены на сайте

# --------------------- Дерево решений ---------------------

def task():
    age = int(input('Age: '))
    stage = int(input('Stage: '))
    car = input('sport/minivan: ')
    crash = int(input('Crash 1/0: '))
    place = input('city/village: ')
    if age > 40:
        if place == "village" or stage > 10:
            print('allow')
        else: print('refuse')
    else:
        if crash == 0 or car == "multivan":
            print('allow')
        else: print('refuse')





if __name__ == "__main__":
    task()
