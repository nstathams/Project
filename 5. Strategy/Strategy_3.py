def max_profit(prices):
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        if price < min_price:
            min_price = price
    return max_profit

gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]

print(max_profit(gold_prices_1))
print(max_profit(gold_prices_2))
print(max_profit(gold_prices_3))
print(max_profit(gold_prices_4))
print(max_profit(gold_prices_5))
