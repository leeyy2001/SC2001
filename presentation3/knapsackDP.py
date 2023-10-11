

# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP


def knapsack(wt, val, W, n):

    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1),
            knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]


# Driver code
if __name__ == '__main__':
    # Weights and profits for (1) and (2)
    weight = [4, 6, 8]
    profit = [7, 6, 9]

    # Weights and profits for (3) and (4)
    weight = [5, 6, 8]
    profit = [7, 6, 9]

    C = 14
    n = len(profit)

    # We initialize the matrix with -1 at first.
    t = [[-1 for i in range(C + 1)] for j in range(n + 1)]
    print(knapsack(weight, profit, C, n))
