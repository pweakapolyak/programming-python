

limit_buy = 12.25
limit_sell = 16.32

current_stock_price = 11.12

if current_stock_price <= limit_buy:
    print('Buy!')
else:
    if current_stock_price >= limit_sell:
        print('Sell!')
    else:
        print('Nothing')


print('End')
