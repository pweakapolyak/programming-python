# --------------------- Накопления на первоначальный взнос  ---------------------

# Условия задачи на сайте.

# --------------------- Накопления на первоначальный взнос ---------------------

def task():
   # por = 0.25
   # ann = 0.04
   # monthly = ann / 12
   # save = 0
   # cost = int(input('Price: '))
   # salary = int(input('Salary: '))
   # procent = int(input('% от 1 до 100: '))
   # msal = salary / 12
   # paym = cost * por
   # nummonth = 0
   #
    #while save < paym:
     #   save += save * monthly
      #  save += msal * (procent/100)
       # nummonth += 1

    # print('Number of months:', nummonth)

   cost = int(input('Price: '))
   salary = int(input('Salary: '))
   procent = int(input('% от 1 до 100: '))
   price = cost / 4
   invest = 0.04 / 12
   month_salary = salary / 12
   otlogeno = month_salary * (procent/100)
   nakoplenie = 0
   months = 0
   while nakoplenie < price:
       nakoplenie += nakoplenie * invest
       nakoplenie += otlogeno
       months += 1

   print('Number of months:', months)

if __name__ == "__main__":
    task()
