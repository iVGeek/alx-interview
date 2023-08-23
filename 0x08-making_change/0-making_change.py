#!/usr/bin/python3
"""
Changes come from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values determine,
    the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]


if __name__ == "__main__":
    coins = [1, 2, 25]
    total = 37
    result = makeChange(coins, total)
    print(result)
