# Problem:
# Print numbers from 1000 down to 1 without using any loops or range().
# Recursion depth is increased to avoid RecursionError.

# solution:
# - Increase recursion limit
# - Use recursion to print and call the next number.

#look note here:
# Default recursion limit is = ~1000,so we are tasks like printing 1000 numbers, setting 1500 is fine.

import sys
sys.setrecursionlimit(1500)  # Increase recursion limit

def reverse_count(n):
    if n < 1:
        return
    print(n)
    reverse_count(n - 1)

# Start
reverse_count(1000)
