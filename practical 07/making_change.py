# Making Change Problem using Dynamic Programming

print("=" * 50)
print("MAKING CHANGE USING DYNAMIC PROGRAMMING")
print("=" * 50)

# Input coin denominations
n = int(input("Enter number of coin denominations: "))

coins = []
for i in range(n):
    coin = int(input(f"Enter coin {i + 1}: "))
    coins.append(coin)

# Input amount
amount = int(input("Enter the amount: "))

# dp[i] = minimum number of coins needed to make amount i
dp = [float('inf')] * (amount + 1)

# 0 coins are needed to make amount 0
dp[0] = 0

# Dynamic Programming
for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# Display result
if dp[amount] == float('inf'):
    print("Change cannot be made for the given amount.")
else:
    print("Minimum number of coins required:", dp[amount])

print("=" * 50)
