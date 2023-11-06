def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    for i in range(n+1):
        for j in range(W + 1):
            print(K[i][j], end=" ")

        print("\n")
    # print(len(K))

    return K[n][W]


# Driver code
if __name__ == '__main__':
    profit = [7, 6, 9]
    weight = [4, 6, 8]
    W = 14
    n = len(profit)
    print(knapSack(W, weight, profit, n))
