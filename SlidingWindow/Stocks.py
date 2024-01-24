
# todo: BEST TIME TO BUY AND SELL STOCKS(NEETCODE 150, PROBLEM NUMBER - , EASY)

# ? Here we are given a list of stock prices on different days, we have to calculate the maximum profit, and when we have to buy and sell the stock

# * To solve this we can use the sliding window, and iterate through the list and add each of them and calculate the maximum profit and then return the max profit

# * Time Complexity - O(n)

# * Space Complexity - O(1)

from inputs import stocksInput1, stocksInput2


def bestStocks(prices: list[int]) -> int:
    L, R = 0, 1  # ! Here we are assigning two pointers for sliding through the window
    maxProfit = 0

    while R < len(prices):
        if prices[L] < prices[R]:
            # ! This statement is self explanatory, we calculate the profit, and update the maxProfit
            profit = prices[R] - prices[L]
            maxProfit = max(profit, maxProfit)
        else:
            # ! If the left price is less than the right price, there is no point in increasing it by just one, we can rather make them equal because adding the others are pretty worthless.
            L = R
        R += 1
    print(maxProfit)
    return maxProfit


bestStocks(stocksInput1)
bestStocks(stocksInput2)
