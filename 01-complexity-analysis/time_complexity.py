
# DSA in Python
# Topic: Time Complexity

# 1. O(1) - Constant Time
# Executes one operation regardless of n
n = 5
print(n)


# 2. O(n) - Linear Time
# The loop runs n times
n = 5
for i in range(n):
    print(i)


# 3. O(n^2) - Quadratic Time
# Both loops run n times
n = 3
for i in range(n):
    for j in range(n):
        print(i, j)


# 4. O(n^2) - Nested Loop with i iterations
# Total iterations = n * (n - 1) / 2
n = 5
for i in range(n):
    for j in range(i):
        print(i, j)