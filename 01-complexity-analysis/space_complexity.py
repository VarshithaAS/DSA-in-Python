
# DSA in Python
# Topic: Space Complexity and Auxiliary Space

# Example 1: O(1) - Constant Auxiliary Space
# Uses a fixed number of extra variables
n = 5
total = 0

for i in range(n):
    total += i

print("Total:", total)

# Example 2: O(n) - Linear Auxiliary Space
# Creates an extra list containing n elements
n = 5
numbers = []

for i in range(n):
    numbers.append(i)

print("Numbers:", numbers)