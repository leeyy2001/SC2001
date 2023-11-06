def unboundedKnapsack(W, index, val, wt):

    # Base case of recursion when only one element is there.
    if index == 0:
        return (W//wt[0])*val[0]
    # If the element with referred by index is doesn't occur even once in the required solution
    notTake = 0+unboundedKnapsack(W, index-1, val, wt)
    # If the element is occur atleast once in the required solution
    take = -100000
    if wt[index] <= W:
        take = val[index]+unboundedKnapsack(W-wt[index], index, val, wt)
    return max(take, notTake)


# Driver program
W = 14
wt = [4, 6, 8]
val = [7, 6, 9]
n = len(val)

print(unboundedKnapsack(W, n-1, val, wt))
