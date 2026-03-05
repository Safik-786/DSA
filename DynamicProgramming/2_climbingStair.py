# Problem Statement: Climbing Stairs (Dynamic Programming)
# You are climbing a staircase that has n steps.
# At each step, you can choose to climb either 1 step or 2 steps.
# Your task is to determine the total number of distinct ways you can reach the top of the staircase.


# Explanation
# This problem follows the Fibonacci pattern:
# ways(n) = ways(n - 1) + ways(n - 2)
# Because to reach step n, you must come from:
# step n-1 (1 step move)
# step n-2 (2 step move)



