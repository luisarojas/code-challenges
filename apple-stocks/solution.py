# Solution
def get_max_profit(stock_prices):
    
    if len(stock_prices) < 2:
        raise Exception('Not enough data in stock prices list')
    
    max_price = max(stock_prices)
    # Pick the max value furthest to the left if there is more than one
    max_price_index = max([i for i, price in enumerate(stock_prices) if price == max_price])
    
    # If the max price is the first in the list
    if max_price_index == 0:
        return max(stock_prices[max_price_index+1:]) - max_price
    
    # Look for the cheapest the stock was previous to the time it was at its max
    min_price = max_price
    for price in stock_prices[:max_price_index]:
        if price < min_price:
            min_price = price
    return max_price - min_price