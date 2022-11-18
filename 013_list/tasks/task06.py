# --------------------- Анализ dataset ---------------------

# Есть dataset c запрплатами в data science(data_science.csv)
# строка - это 1 запись в нем.
# колонки разделены запятой. информация о колонках есть здесь - https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries?resource=download

# Задача найти среднюю зарплату(просуммировать все элементы и разделить на их количество) в USD
# за 2021e(1 колонка) у "Data Scientist"(4 колонка), значение зарпалты в USD(7 колонка)

# Подсказка: посмотрите в python функцию split она разделяет строку на список строк по разделителю.
# "1,2,3".split(",") -> ["1","2","3"]

# --------------------- Анализ dataset ---------------------

def load_dataset():
    with open('data_science.csv', 'r') as file:
        rows = file.readlines()
        for index, row in enumerate(rows):
            rows[index] = row.rstrip()
        return rows


def find_avg_salary():
    dataset = load_dataset()
    sum_salary = 0
    num_records = 0
    for element in dataset:
        row = element.split(",")
        if row[0] == "2021e" and row[3] == "Data Scientist":
            sum_salary += float(row[6])
            num_records += 1

    return sum_salary / num_records


if __name__ == "__main__":
    print(find_avg_salary())
