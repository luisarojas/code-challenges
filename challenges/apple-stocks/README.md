# <p align="center">Apple Stocks</p>

<p align="center">
	    <a href="#execution">Execution</a>
    &nbsp; • &nbsp;
    <a href="#problem">Problem</a>
    &nbsp; • &nbsp;
    <a href="#solution">Solution</a>
</p>

### Execution

Run `solution.py`:

```bash
$ make
```

Test solution with `pytest`:

```bash
$ make test
```

### Problem

**Description**

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

* The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
* The values are the price (in US dollars) of one share of Apple stock at that time. So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

**Examples**

```python
stock_prices = [10, 7, 5, 8, 11, 9]
get_max_profit(stock_prices) # Returns 6 (buying for $5 and selling for $11)
```

*Note: No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.*

### Solution

| **Time Complexity** |  `O(n)` |
|-------|-------------|
I'm using python's `max()` function, which has this complexity. I needs to interate through the whole list to find the maximum value in it.

| **Space Complexity** |  `O(1)` |
|-------|-------------|
Constant, since there is no change in the space that is being taken up by the algorithm.


```python
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
```
