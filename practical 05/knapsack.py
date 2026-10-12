# 0/1 Knapsack Problem using Dynamic Programming

print("=" * 60)
print("0/1 KNAPSACK USING DYNAMIC PROGRAMMING")
print("=" * 60)

# Number of items
n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    p = int(input(f"Enter profit of item {i + 1}: "))
    weights.append(w)
    profits.append(p)

capacity = int(input("Enter knapsack capacity: "))

# DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Maximum profit
max_profit = dp[n][capacity]

# Find selected items
selected_items = []
w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i)
        w -= weights[i - 1]

selected_items.reverse()

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print("Maximum Profit:", max_profit)

print("Selected Items:", selected_items)

if selected_items:
    total_weight = sum(weights[i - 1] for i in selected_items)
    print("Total Weight:", total_weight)
else:
    print("Total Weight: 0")

print("\nTime Complexity: O(n × W)")
print("Space Complexity: O(n × W)")

print("=" * 60)
