# Solution
def get_max_profit(stock_prices):

	if len(stock_prices) < 2: return 0

	max_profit = 0 # Shouldn't make less than 0
	min_price = stock_prices[0]

	for price in stock_prices:
		if price < min_price:
			min_price = price
		if (price - min_price) > max_profit:
			max_profit = (price - min_price)
			
	return max_profit