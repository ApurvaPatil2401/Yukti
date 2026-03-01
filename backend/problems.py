problems = {
    "fibonacci": {
        "description": "Write a function to compute the nth Fibonacci number.",
        "concept": "recursion",
        "solution": """def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)"""
    },
    "two_sum": {
        "description": "Return indices of two numbers that add up to target.",
        "concept": "hash map",
        "solution": """def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i"""
    }
}